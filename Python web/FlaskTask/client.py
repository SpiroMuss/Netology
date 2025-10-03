import requests

response = requests.get("http://127.0.0.1:5000/advertisements/2")


# response = requests.post("http://127.0.0.1:5000/advertisements/", json={
#     "header": "HEADER",
#     "comment": "COMMENT",
#     "owner": "OWNER",
# })


print(response.text)
print(response.status_code)