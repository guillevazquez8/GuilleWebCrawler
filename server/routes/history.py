from flask import abort, make_response
from server.model import History as History_cls
from flask_restx import Resource, Namespace


history_ns = Namespace("history",
                       description="Check all interactions with the api's filters")


@history_ns.route("/all")
class History(Resource):
    @history_ns.doc("Get all interactions with this api's filters")
    def get(self):
        all_history = History_cls.get_all()
        all_history_json = [history.to_dict() for history in all_history]
        return make_response(all_history_json)
