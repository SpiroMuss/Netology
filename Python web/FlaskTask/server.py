from flask import Flask, jsonify

app = Flask("app")

def hello():
    http_response = jsonify({"message": "hello"})
    return http_response

app.add_url_rule("/hello", view_func=hello, methods=["GET"])

app.run()