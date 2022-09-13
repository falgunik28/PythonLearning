import json

import requests

body ={
        "id": 101,
        "username": "fals",
        "firstName": "falguni",
        "lastName": "sethi",
        "email": "fals@gmail.com",
        "password": "123456",
        "phone": "9876543211",
        "userStatus": 0
      }

cont_typ = {"Content-Type": "application/json"}

response = requests.put("https://petstore.swagger.io/v2/user/fals", headers=cont_typ, json=body)

print(response.status_code)
assert(response.status_code == 200)
print("User have been updated!")
# verify the user created

new_response = requests.get("https://petstore.swagger.io/v2/user/fals")
print(new_response.text)
js = json.loads(new_response.text)
assert(js == body)
