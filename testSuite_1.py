# importing Modules
import requests
from jsonpath_ng import jsonpath
import json


def test_getrestapi():
    # get rest API End point
    url = 'https://reqres.in/api/users?page=2'
    # Execute the rest GET API
    v_response = requests.get(url)
    # response code of the request
    v_responsecode = v_response.status_code
    # convert the data into JSON
    json_data = json.loads(v_response.text)
    # get the per_page value
    v_per_page = jsonpath.jsonpath(json_data, 'per_page')
    # get the number of students value
    v_student_records = jsonpath.jsonpath(json_data, 'data')
    v_count_records = len(v_student_records[0])
    # assert condition
    assert v_responsecode == 200
    assert v_per_page[0] == 3
    assert v_count_records == v_per_page[0]


def test_deleterestAPI():
    # get rest API End point
    url = 'http://reqres.in/api/users/2'
    # Execute the rest GET API
    v_response = requests.delete(url)
    # response code of the request
    v_responsecode = v_response.status_code
    # assert condition
    assert v_responsecode == 204
    assert len(v_response.text) == 0