# importing Modules
import requests
import jsonpath
import json

# get rest API End point
url = 'https://reqres.in/api/users'

# read the data from the file
f_pointer = open('C:\\D_DRIVE\\IMPORTANT\\UDEMY_COURSES\\API_Testing\\Sample_Post_input.json',mode='r')
v_input_data = f_pointer.read()

# convert the data into json/dict
v_input_data_json = json.loads(v_input_data)

# print input data
print("-----------Input Data---------")
print(v_input_data_json)

# Execute the rest post API
v_response = requests.post(url,v_input_data_json)
print("-----------API Response---------")
print(v_response.text)

# response code of the request
v_responsecode = v_response.status_code
print("-----------Response Code---------")
print(v_responsecode)

# convert the data into JSON
json_data = json.loads(v_response.text)
print("-----------JSON DATA---------")
print(json_data)

# get the id of the response of students value
v_id = jsonpath.jsonpath(json_data,'id')
print("-----------ID is  of students Value---------")
print(v_id[0])

# assert condition
assert v_responsecode == 201
