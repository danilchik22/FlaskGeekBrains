from flask import Flask
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import auth_app, login_manager
from blog.views.index import index_app
from flask_migrate import Migrate


def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(index_app, url_prefix="/")


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost/blog"
    app.config["SECRET_KEY"] = "qwd;;gu393390qiefjkwldkasdjkdkjkdwp[a03]"
    db.init_app(app)
    login_manager.init_app(app)
    register_blueprints(app)
    return app

app = create_app()
migrate = Migrate(app, db, compare_type=True)