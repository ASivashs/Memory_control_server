from flask import jsonify, request, Blueprint

from datetime import datetime
from bson.errors import InvalidId
from bson import ObjectId

from mongodb_config import collections
from validator import validate_data
from utils import MongoJSONEncoder, logger


reports = Blueprint("reports", __name__)


@reports.route("/", methods=["GET"])
def get_reports():
    logger.info("Requested all data.")
    data = [field for field in collections.find()]
    return jsonify(MongoJSONEncoder().encode(data))


@reports.route("/<id>", methods=["GET"])
def get_report_by_id(id):
    logger.info(f"Requested data with id={id}.")

    try:
        data = collections.find_one({"_id": ObjectId(id)})
    except InvalidId as exception:
        logger.error(f"Object with id={id} not found. {exception}")
        return jsonify({"Error": f"Object with this id not found. {exception}"})

    return jsonify(MongoJSONEncoder().encode(data))


@reports.route("/", methods=["POST"])
def create_report():
    if not request.data:
        logger.error(f"Request {request.url} is empty in POST.")
        return jsonify({"Error": "Provided request is empty."})

    if not request.is_json:
        logger.error(f"Invalid data type in POST request {request.url}.")
        return jsonify({"Error": "Invalid data type."})

    validate_result = validate_data(request=request)

    if not validate_result:
        logger.error("Incorrect data format in POST request.")
        return jsonify({"Error": "Incorrect data."})

    create_data = request.json
    create_data["time"] = datetime.now()
    collections.insert_one(create_data)
    logger.info("Added new report.")
    return jsonify(MongoJSONEncoder().encode(create_data))


@reports.route("/<id>", methods=["PUT"])
def update_report(id):
    logger.info(f"Update data with id={id}.")
    if not request.data:
        logger.error("Request is empty in PUT.")
        return jsonify({"Error": "Provided request is empty."})

    if not request.is_json:
        logger.error(f"Invalid data type in PUT request. {request.get_data()}")
        return jsonify({"Error": "Invalid data type."})

    try:
        request_id = ObjectId(id)
    except InvalidId as exception:
        logger.error(f"Invalid id type. {exception}")
        return jsonify({"Error": f"Invalid id type. {exception}"})

    validate_result = validate_data(request=request)

    if not validate_result:
        logger.error("Incorrect data format in PUT request.")
        return jsonify({"Error": "Incorrect data."})

    data = request.json
    logger.info(f"Request json: {data}")
    query = {"_id": request_id}
    new_data = {"$set": data}
    collections.update_many(query, new_data)

    result = collections.find_one(request_id)
    return jsonify(MongoJSONEncoder().encode(result))
