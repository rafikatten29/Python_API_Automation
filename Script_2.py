import json
import jsonpath

# read the data from the file
filepointer = open('C:\\D_DRIVE\\IMPORTANT\\UDEMY_COURSES\\API_Testing\\sample_json.json', mode='r')
data = filepointer.read()

# print Type of data variable
print("----------Type of data variable-------")
print(type(data))

# print data
print("----------data-------")
print(data)

json_data = json.loads(data)

# print type of json_data variable
print("----------type of json_data variable-------")
print(type(json_data))

# print json_data
print("----------json_data-------")
print(json_data)

# get the vales from JSON
d1 = jsonpath.jsonpath(json_data,'City')
d2 = jsonpath.jsonpath(json_data,'Students')
d3 = jsonpath.jsonpath(json_data,'Students[0]')
d4 = jsonpath.jsonpath(json_data,'Students[0].Name')
d5 = jsonpath.jsonpath(json_data,'Students[0,1,2].Name')
d6 = jsonpath.jsonpath(json_data,'Students[0:3]')
d7 = jsonpath.jsonpath(json_data,'Students[*].Name')

# print d1
print("----------d1-------")
print(d1)
# print d2
print("----------d2-------")
print(d2)
# print d3
print("----------d3-------")
print(d3)
# print d4
print("----------d4-------")
print(d4)
# print d5
print("----------d5-------")
print(d5)
# print d6
print("----------d6-------")
print(d6)
# print d7
print("----------d7-------")
print(d7)

assert d1[0] == 'Bangalore'