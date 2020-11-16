"""from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow"""

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import json
import copy

from classess.models.abstract_tableware import abstract_tableware

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bowl(abstract_tableware, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # garantee_in_days = db.Column(db.Integer, unique=False)
    style = db.Column(db.String(32), unique=False)
    wieght_in_grams = db.Column(db.Integer, unique=False)
    # ability_to_microwave = db.Column(db.Boolean, unique=False)
    # manufacturer = db.Column(db.String(32), unique=False)
    colour = db.Column(db.String(32), unique=False)
    # dessigned_for = db.Column(db.String(32), unique=False)
    # material = db.Column(db.String(32), unique=False)
    price = db.Column(db.Integer, unique=False)

    """def __init__(self, garantee_in_days=0.0, style="N/A", wieght_in_grams=0.0, ability_to_microwave=True,
                 manufacturer="N/A", colour="N\A", dessigned_for="N\A", material="N\A", price=0.0):
        super().__init__(garantee_in_days, style, wieght_in_grams, ability_to_microwave,
                         manufacturer, colour, dessigned_for, material, price)"""

    def __init__(self, style="N/A", wieght_in_grams=0.0, colour="N/A", price=0):
        super().__int__(self, style, wieght_in_grams, colour, price)


class BowlSchema(ma.Schema):
    class Meta:
        fields = ('id', 'style', 'wieght_in_grams',
                  'colour', 'price')
        """fields = ('id', 'garantee_in_days', 'style', 'wieght_in_grams', 'ability_to_microwave',
                  'manufacturer', 'colour', 'designed_for', 'material', 'price')"""


bowl_schema = BowlSchema()
bowls_schema = BowlSchema(many=True)


@app.route("/bowl", methods=["POST"])
def add_bowl():
    # garantee_in_days = request.json['garantee_in_days']
    style = request.json['style']
    wieght_in_grams = request.json['wieght_in_grams']
    # ability_to_microwave = request.json['ability_to_microwave']
    # manufacturer = request.json['manufacturer']
    colour = request.json['colour']
    # dessigned_for = request.json['dessigned_for']
    # material = request.json['material']
    price = request.json['price']
    bowl = Bowl(  # garantee_in_days,
        style,
        wieght_in_grams,
        # ability_to_microwave,
        # manufacturer,
        colour,
        # dessigned_for,
        # material,
        price)
    db.session.add(bowl)
    db.session.commit()
    return bowl_schema.jsonify(bowl)


@app.route("/bowl", methods=["GET"])
def get_bowls():
    all_bowls = Bowl.query.all()
    result = bowls_schema.dump(all_bowls)
    return jsonify({'bowls': result})


@app.route("/bowl/<id>", methods=["GET"])
def bowl_detail(id):
    bowl = Bowl.query.get(id)
    if not bowl:
        abort(404)
    return bowl_schema.jsonify(bowl)


@app.route("/bowl/<id>", methods=["PUT"])
def bowl_update(id):
    bowl = Bowl.query.get(id)
    if not bowl:
        abort(404)
    old_bowl = copy.deepcopy(bowl)
    # bowl.garantee_in_days = request.json['garantee_in_days']
    bowl.style = request.json['style']
    bowl.wieght_in_grams = request.json['wieght_in_grams']
    # bowl.ability_to_microwave = request.json['ability_to_microwave']
    # bowl.manufacturer = request.json['manufacturer']
    bowl.colour = request.json['colour']
    # bowl.dessigned_for = request.json['dessigned_for']
    # bowl.material = request.json['material']
    bowl.price = request.json['price']
    db.session.commit()
    return bowl_schema.jsonify(old_bowl)


@app.route("/bowl/<id>", methods=["DELETE"])
def bowl_delete(id):
    bowl = Bowl.query.get(id)
    if not bowl:
        abort(404)
    db.session.delete(bowl)
    db.session.commit()
    return bowl_schema.jsonify(bowl)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, host='0.0.0.0')
