import requests
import json

body =[
        {
            "id": 201,
            "username": "abc",
            "firstName": "abc",
            "lastName": "khandelwal",
            "email": "abc@gmail.com",
            "password": "123456",
            "phone": "9876543211",
            "userStatus": 0
         },
        {
            "id": 202,
            "username": "def",
            "firstName": "def",
            "lastName": "khandelwal",
            "email": "def@gmail.com",
            "password": "123456",
            "phone": "9876543211",
            "userStatus": 0
        },
        {
            "id": 203,
            "username": "ghi",
            "firstName": "ghi",
            "lastName": "khandelwal",
            "email": "ghi@gmail.com",
            "password": "123456",
            "phone": "9876543211",
            "userStatus": 0
        }
      ]
my_url = "https://petstore.swagger.io/v2/user/createWithList"
cont_typ = {"Content-Type": "application/json"}
response = requests.post(my_url,headers=cont_typ, json=body)
print(response.status_code)
assert(response.status_code == 200)
print("Users are created!")
# verify the user created

new_response1 = requests.get("https://petstore.swagger.io/v2/user/abc")
new_response2 = requests.get("https://petstore.swagger.io/v2/user/def")
new_response3 = requests.get("https://petstore.swagger.io/v2/user/ghi")

print(new_response1.text, new_response2.text, new_response3.text)
