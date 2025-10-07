import requests

from schema import CreateAdvertisementRequest

response = requests.post("http://localhost:8000/advertisements",
                         json={
                             "title": "title",
                             "comment": "comment",
                             "price": 123,
                             "owner": "owner",
                         })


# response = requests.get("http://localhost:8000/advertisements/1")


# response = requests.patch("http://localhost:8000/advertisements/1",
#                           json={
#                               "title": "TITLE",
#                               "price": 234
#                           })

# response = requests.get("http://localhost:8000/advertisements/1",
#                         params={"price": 234})


# response = requests.delete("http://localhost:8000/advertisements/1")


print(response.text)
print(response.status_code)