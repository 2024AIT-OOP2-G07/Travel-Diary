import datetime
from flask import Blueprint, render_template, request
from models import Place
from peewee import fn

# Blueprintの作成
trip_bp = Blueprint("trip", __name__, url_prefix="/trip")

@trip_bp.route('/', methods=['GET', 'POST'])
def list():

    # addressがクエリパラメータで指定されているかを確認
    address = request.args.get("address")

    if address:  # addressが指定されている場合
        trip_data = Place.select()\
            .where(Place.evaluation == 5, Place.address.contains(address))\
            .order_by(Place.day.desc())\
            .limit(5)
        
    else:  # 初回ロードまたはaddressが指定されていない場合
        trip_data = Place.select()\
            .where(Place.evaluation == 5)\
            .order_by(Place.day.desc())\
            .limit(5)

    return render_template("trip.html", trip_data = trip_data, address = address)