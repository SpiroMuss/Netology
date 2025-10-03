from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from models import DbSession, Advertisement
from errors import HttpError

app = Flask("app")

@app.before_request
def before_requests():
    session = DbSession()
    request.session = session

@app.after_request
def after_requests(response):
    request.session.close()
    return response

@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    http_response = jsonify({"error": error.message})
    http_response.status_code = error.status_code
    return http_response

def get_advertisement_by_id(adv_id):
    adv = request.session.get(Advertisement, adv_id)
    if adv is None:
        raise HttpError(404, "Advertisement not found")
    return adv

def add_advertisement(adv):
    try:
        request.session.add(adv)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, "Advertisement already exists")


class AdvView(MethodView):

    def get(self, adv_id: int):
        adv = get_advertisement_by_id(adv_id)
        return jsonify(adv.json)


    def post(self):
        json_data = request.json

        adv = Advertisement(
            header=json_data["header"],
            comment=json_data["comment"],
            owner=json_data["owner"],
        )
        add_advertisement(adv)
        return jsonify(adv.id_json)

    def patch(self, adv_id: int):
        json_data = request.json
        adv = get_advertisement_by_id(adv_id)
        if "header" in json_data:
            adv.header = json_data["header"]
        if "comment" in json_data:
            adv.comment = json_data["comment"]
        if "owner" in json_data:
            adv.owner = json_data["owner"]
        add_advertisement(adv)
        return jsonify(adv.id_json)

    def delete(self, adv_id: int):
        adv = get_advertisement_by_id(adv_id)
        request.session.delete(adv)
        request.session.commit()
        return jsonify({"message": "Advertisement deleted"})


adv_view = AdvView.as_view('adv_view')

app.add_url_rule(
    "/advertisements/", view_func=adv_view, methods=["POST"]
)

app.add_url_rule(
    "/advertisements/<int:adv_id>",
    view_func=adv_view,
    methods=["GET", "PATCH", "DELETE"]
)

app.run()