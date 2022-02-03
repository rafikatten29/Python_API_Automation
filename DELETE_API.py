# importing Modules
import requests
import jsonpath
import json

# get rest API End point
url = 'http://reqres.in/api/users/2'

# Execute the rest GET API
v_response = requests.delete(url)
print("-----------API Response---------")
print(v_response.text)
print("-----------API Response length---------")
print(len(v_response.text))

# response code of the request
v_responsecode = v_response.status_code
print("-----------Response Code---------")
print(v_responsecode)

# assert condition
assert v_responsecode == 204
assert len(v_response.text) == 0
