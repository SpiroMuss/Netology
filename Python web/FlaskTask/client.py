import requests

# response = requests.post("http://127.0.0.1:5000/advertisements/", json={
#     "header": "HEADER1234HEADER1234HEADER1234HEADER1234HEADER1234"
#               "HEADER1234HEADER1234HEADER1234HEADER1234HEADER1234HEADER1234",
#     "comment": "COMMENT",
#     "owner": "OWNER",
# })

response = requests.post("http://127.0.0.1:5000/advertisements/", json={
    "header": "HEADER1234",
    "comment": "COMMENT",
    "owner": "OWNER",
})

# response = requests.get("http://127.0.0.1:5000/advertisements/1")

# response = requests.patch("http://127.0.0.1:5000/advertisements/1", json={
#     "header": "HEADER1234HEADER1234HEADER1234HEADER1234HEADER1234"
#               "HEADER1234HEADER1234HEADER1234HEADER1234HEADER1234",
#     "comment": "COMMENT",
#     "owner": "OWNER",
# })

# response = requests.delete("http://127.0.0.1:5000/advertisements/2")


print(response.text)
print(response.status_code)