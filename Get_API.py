# importing Modules
import requests
import jsonpath
import json

# get rest API End point
url = 'https://reqres.in/api/users?page=2'

# Execute the rest GET API
v_response = requests.get(url)
print ("-----------API Response---------")
print(v_response.text)

# response code of the request
v_responsecode = v_response.status_code
print("-----------Response Code---------")
print(v_responsecode)

# convert the data into JSON
json_data = json.loads(v_response.text)
print("-----------JSON DATA---------")
print(json_data)

# get the per_page value
v_per_page = jsonpath.jsonpath(json_data,'per_page')
print("-----------Per page Value---------")
print(v_per_page[0])

# get the number of students value
v_student_records = jsonpath.jsonpath(json_data,'data')
v_count_records = len(v_student_records[0])
print("-----------number of students Value---------")
print(v_count_records)

# assert condition
assert v_responsecode == 200
assert v_per_page[0] == 3
assert v_count_records == v_per_page[0]