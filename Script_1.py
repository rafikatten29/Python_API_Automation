import requests

# test url
test_url = "http://www.techsckool.com/"

# call the request and store the results
v_response = requests.get(test_url)

# print response
print("----------RESPONSE-------")
print(v_response)
# print Status code
print("----------STATUSCODE-------")
print(v_response.status_code)
# print content
print("----------CONTENT-------")
print(v_response.content)
# print headers
print("----------HEADERS-------")
print(v_response.headers)
# print url
print("----------URL-------")
print(v_response.url)
# print cookies
print("----------COOKIES-------")
print(v_response.cookies)
# print encoding
print("----------ENCODING-------")
print(v_response.encoding)
# print text
print("----------TEXT-------")
print(v_response.text)