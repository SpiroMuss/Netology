from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from models import DbSession, Advertisement

app = Flask("app")


class UserView(MethodView):

    def get(self, adv_id):
        with DbSession() as session:
            adv = session.get(Advertisement, adv_id)
            if adv is None:
                http_response = jsonify({"error": "Advertisement not found"})
                http_response.status_code = 404
                return http_response

            return jsonify(adv.json)


    def post(self):
        json_data = request.json
        with DbSession() as session:
            adv = Advertisement(
                header=json_data["header"],
                comment=json_data["comment"],
                owner=json_data["owner"],
            )
            session.add(adv)
            try:
                session.commit()
            except IntegrityError:
                http_response = jsonify({"error": "Advertisement already exists"})
                http_response.status_code = 409
                return http_response
            return jsonify(adv.id_json)

    def patch(self, adv_id):
        json_data = request.json
        with DbSession() as session:
            adv = session.get(Advertisement, adv_id)
            if adv is None:
                http_response = jsonify({"error": "Advertisement not found"})
                http_response.status_code = 404
                return http_response
            if "header" in json_data:
                adv.header = json_data["header"]
            if "comment" in json_data:
                adv.comment = json_data["comment"]
            if "owner" in json_data:
                adv.owner = json_data["owner"]
            session.add(adv)
            try:
                session.commit()
            except IntegrityError:
                http_response = jsonify({"error": "Advertisement already exists"})
                http_response.status_code = 409
                return http_response
            return jsonify(adv.id_json)

    def delete(self, adv_id):
        with DbSession() as session:
            adv = session.get(Advertisement, adv_id)
            if adv is None:
                http_response = jsonify({"error": "Advertisement not found"})
                http_response.status_code = 404
                return http_response
            session.delete(adv)
            session.commit()
            return jsonify(adv.json)


user_view = UserView.as_view('user_view')

app.add_url_rule(
    "/users/", view_func=user_view, methods=["POST"]
)

app.add_url_rule(
    "/users/<int:user_id>",
    view_func=user_view,
    methods=["GET", "PATCH", "DELETE"]
)

app.run()