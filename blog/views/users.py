from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models.models import User

users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def list_users():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="details")
def detail_user(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} не существует!")
    return render_template("users/detail.html", user_id=user_id)


@users_app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404