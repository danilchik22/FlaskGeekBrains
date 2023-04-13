from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from blog.models.models import User
from blog.models.database import db


auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    
    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="Пользователь не введен")
    
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error="Пользователь не найден")
    login_user(user)
    return redirect(url_for("index.index"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))


@auth_app.route("/signup/", methods=["GET", "POST"], endpoint="signup")
def signup():
    if request.method == "GET":
        return render_template("auth/register.html")
    if request.method == "POST":
        email = request.values.get('email')
        username = request.values.get('username')
        password = request.values.get('password')
        age = request.values.get('age')
    
        
        user = User.query.filter_by(username=username, email=email).first()
        print(user)
        if user:
            return render_template("auth/register.html", error = "Такой пользователь уже есть")
        new_user = User(email=email, username=username, password=password, age=age, is_staff=False)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth_app.login'))


__all__ = [
    "login_manager",
    "auth_app",
]