import logging
import json
from bson import ObjectId
from datetime import datetime


def logger_config():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("server.log")],
    )

    logger = logging.getLogger(__name__)
    return logger


logger = logger_config()


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, data):
        if isinstance(data, ObjectId):
            return str(data)
        if isinstance(data, datetime):
            return str(data)
        return json.JSONEncoder.default(self, data)
