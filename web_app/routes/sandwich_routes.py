from flask import Blueprint, render_template, current_app #, session

from app.models.sandwich import Sandwich

sandwich_routes = Blueprint("sandwich_routes", __name__)

@sandwich_routes.route("/sandwiches")
def sandwiches():
    sandwiches = Sandwich.all()
    return render_template("sandwiches.html", sandwiches=sandwiches)