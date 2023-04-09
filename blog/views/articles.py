from flask import Blueprint, render_template


articles_app = Blueprint('articles_app', __name__)

ARTICLES = [
    {
    "title": "Очень интересная статья. Самая интересная статья.",
    "text": "Действительно, интереснее статьи пока не придумали. Она очень длинная и интересная.",
    "author": 1
    },
    {
    "title": "Эта тоже немного интересная.",
    "text": "Ну конечно не такая как предыдущая, но тоже норм.",
    "author": 2
    }
]

@articles_app.route("/", endpoint="list")
def list_articles():
    return render_template("articles/list.html", articles=ARTICLES)