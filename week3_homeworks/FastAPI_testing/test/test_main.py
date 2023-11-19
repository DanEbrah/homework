from fastapi.testclient import TestClient
import fastapi
from main import app


client = TestClient(app)

def test_put_api():
    put_response = client.put("/items/ora7", json={
    "name": "oranges",
    "quantity": 7,
    "serial_num": "ora7",
    "origin": {
        "country": "Ethiopia",
        "production_date": "2023"
    }
    })
    
    assert put_response.status_code == 200


def test_incorrect_put_api(): #wrong quantity, code 422
    response = client.put("/items/oranages1", json={
    "name": "oranges",
    "quantity": "asd",
    "serial_num": "oraanges1",
    "origin": {
        "country": "Ethiopia",
        "production_date": "2023"
    }
    })
    
    assert response.status_code == 422


def test_get_api(): #create/put another dict with different items, and get to compare which is the same
    another = { "name": "apples",
    "quantity": 8,
    "serial_num": "appl8",
    "origin": {
        "country": "Ethiopia",
        "production_date": "2023"}}
    client.put("/items/appl8", json = another)
    assert response_get.status_code == 200
    
    response_get = client.get("/items/appl8")
    assert response_get.json() == another
    # need to check the payload way or in another way


def test_delete_api(): # ora21 not found, 404 response.
    response = client.delete("/items/ora21")
    assert response.status_code == 404

def test_get_all_apis(): #get all api
    response = client.get("/items")
    assert response.status_code == 200
    print(response)
