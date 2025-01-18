import datetime
from flask import Blueprint, render_template, request
from models import Place
from peewee import fn

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")

@trip_bp.route('/', methods=['GET', 'POST'])
def list():

    keyword = request.args.get("q")

    if keyword: 
        trip_data = Place.select()\
            .where(Place.evaluation == 5, Place.name.contains(keyword) | Place.address.contains(keyword))\
            .order_by(Place.day.desc())
        
    else: 
        trip_data = Place.select()\
            .where(Place.evaluation == 5)\
            .order_by(Place.day.desc())

    return render_template("trip.html", trip_data = trip_data, keyword = keyword)