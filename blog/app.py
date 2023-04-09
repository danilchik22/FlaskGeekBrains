from flask import Flask
from blog.views.users import users_app
from blog.views.articles import articles_app



def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

app = create_app()

