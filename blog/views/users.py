from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__)

USERS = [
    {
    "id": 1,
    "username": "vasya01",
    "name": "Василий",
    "age": 32,
    },
    {
    "id": 2,
    "username": "vanyaAbrikos",
    "name": "Иван",
    "age": 15,
    },
    {
    "id": 3,
    "username": "petrovich",
    "name": "Григорий",
    "age": 56,
    }
]

@users_app.route("/", endpoint="list")
def list_users():
    return render_template("users/list.html", users=USERS)

@users_app.route("/<int:user_id>/", endpoint="details")
def detail_user(user_id: int):
    try:
        user_id = USERS[user_id]["id"]
    except IndexError:
        raise NotFound(f"User #{user_id} не существует!")
    return render_template("users/detail.html", user_id=user_id)