import requests

response = requests.delete("https://petstore.swagger.io/v2/user/abc")
print(response.status_code)

new_response = requests.get("https://petstore.swagger.io/v2/user/abc" )

print(new_response.text)