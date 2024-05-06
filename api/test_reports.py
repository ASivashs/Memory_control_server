import pytest
from datetime import datetime
from bson import ObjectId
import json

import mongomock

from api.app import create_app
from api.utils import MongoJSONEncoder


TEST_DATA = [
    {
        "total": "13824",
        "used": "11062",
        "used_percentage": 80.02,
        "free": "490",
        "shared": "351",
        "cache": "2947",
        "time": datetime.now(),
    },
    {
        "total": "13824",
        "used": "11059",
        "used_percentage": 80,
        "free": "526",
        "shared": "350",
        "cache": "2914",
        "time": datetime.now(),
    },
]


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client_app(app):
    yield app.test_client()


@pytest.fixture
def mongo_collections():
    client = mongomock.MongoClient()
    db = client["SystemMonitorReports"]
    collections = db.AlarmReports
    yield collections


def test_get_all_reports(mongo_collections, client_app):
    mongo_collections.insert_many(TEST_DATA)
    response = client_app.get("/reports")
    response_data = list(json.loads(response.data))[0]
    assert response_data["total"] == TEST_DATA[0]["total"]


def test_get_report_by_id(mongo_collections, client_app):
    mongo_collections.insert_many(TEST_DATA)
    data = [field for field in mongo_collections.find_one()]
    data = MongoJSONEncoder().encode(data)
    test_data_id = data
    response = client_app.get(f"/reports/{test_data_id}")
    response_data = list(json.loads(response.data))[0]
    assert response_data["total"] == TEST_DATA[0]["total"]


def test_get_report_by_invalid_id(mongo_collections, client_app):
    mongo_collections.insert_many(TEST_DATA)
    test_data_id = "invalid_id"
    response = client_app.get(f"/reports/{test_data_id}")
    response_data = list(json.loads(response.data).keys())[0]
    assert response_data == "Error"


def test_create_report(mongo_collections, client_app):
    report_data = {
        "total": "10",
        "used": "8",
        "used_percentage": 80,
        "free": "2",
        "shared": "0",
        "cache": "0",
    }
    response = client_app.post("/reports", json=report_data)
    data = [field for field in mongo_collections.find_one()]
    data = json.loads(MongoJSONEncoder().encode(data))
    assert data["total"] == report_data["total"]


def test_create_invalid_report(mongo_collections, client_app):
    report_data = "invalid_data"
    response = client_app.post("/reports", json=report_data)
    response_data = list(json.loads(response.data).keys())[0]
    assert response_data == "Error"


def test_update_report(mongo_collections, client_app):
    report_data = {
        "total": "10",
        "used": "8",
        "used_percentage": 80,
        "free": "2",
        "shared": "0",
        "cache": "0",
    }
    mongo_collections.insert_one(report_data)
    data = [field for field in mongo_collections.find_one()]
    data = MongoJSONEncoder().encode(data)
    test_data_id = data

    updated_report_data = {
        "total": "0",
        "used": "0",
        "used_percentage": 0,
        "free": "0",
        "shared": "0",
        "cache": "0",
    }
    response = client_app.put(f"/reports/{test_data_id}", json=updated_report_data)
    data = [field for field in mongo_collections.find_one()]
    data = json.loads(MongoJSONEncoder().encode(data))
    assert data["total"] == updated_report_data["total"]


def test_update_invalid_report(mongo_collections, client_app):
    report_data = {
        "total": "10",
        "used": "8",
        "used_percentage": 80,
        "free": "2",
        "shared": "0",
        "cache": "0",
    }
    mongo_collections.insert_one(report_data)
    data = [field for field in mongo_collections.find_one()]
    data = MongoJSONEncoder().encode(data)
    test_data_id = data

    updated_report_data = ""
    response = client_app.put(f"/reports/{test_data_id}", json=updated_report_data)
    response_data = list(json.loads(response.data).keys())[0]
    assert response_data == "Error"


def test_update_invalid_report_id(mongo_collections, client_app):
    report_data = {
        "total": "10",
        "used": "8",
        "used_percentage": 80,
        "free": "2",
        "shared": "0",
        "cache": "0",
    }
    mongo_collections.insert_one(report_data)
    test_data_id = "invalid_id"

    updated_report_data = {
        "total": "0",
        "used": "0",
        "used_percentage": 0,
        "free": "0",
        "shared": "0",
        "cache": "0",
    }
    response = client_app.put(f"/reports/{test_data_id}", json=updated_report_data)
    response_data = list(json.loads(response.data).keys())[0]
    assert response_data == "Error"
