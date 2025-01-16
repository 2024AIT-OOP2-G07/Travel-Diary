from flask import Blueprint, render_template,request
from models import Place
from peewee import fn

# Blueprintの作成
points_bp = Blueprint("points", __name__, url_prefix="/points")


@points_bp.route("/", methods=['GET', 'POST'])
def list():

    keyword = request.args.get("q")

    if keyword: 
        points_data = (
            Place.select()
            .where(Place.name.contains(keyword) | Place.address.contains(keyword))
            .group_by(Place.name)
            .order_by(fn.COUNT(Place.name).desc())
        )
     
        
    else: 
        points_data = (
            Place.select()
            .group_by(Place.name)
            .order_by(fn.COUNT(Place.name).desc())
        )

    points_data_comments = [
        {
            "id": p.id,
            "name": p.name,
            "address": p.address,
            "comments": [
                {"comment": p.comment, "day": p.day}
                for p in Place.select().where(Place.name == p.name)
            ],
        }
        for p in points_data
    ]

    return render_template("points.html", points_data=points_data_comments, keyword = keyword)
