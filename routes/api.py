from flask import Blueprint, jsonify
from models.prace import prace
from playhouse.shortcuts import model_to_dict

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/points", methods=["GET"])
def get_points():
    points = [model_to_dict(p) for p in prace().select()]
    return jsonify(points)
