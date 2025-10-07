import requests


response = requests.post("http://localhost:8000/v1/advertisements",
                         json={
                             "title": "title",
                             "comment": "comment",
                             "price": 123,
                             "owner": "owner",
                         })

print(response.text)
print(response.status_code)