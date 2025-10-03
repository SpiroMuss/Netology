import requests

response = requests.post("http://127.0.0.1:5000/users",
                         json={
                             "header": "header",
                             "comment": "comment",
                             "owner": "owner",
                         },
                         )


print(response.text)
print(response.status_code)