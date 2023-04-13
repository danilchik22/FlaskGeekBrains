from flask import Blueprint, render_template


index_app = Blueprint("index", __name__)

@index_app.route("/index/", endpoint="index")
def index():
    return render_template("index.html")