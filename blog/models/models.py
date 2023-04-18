from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from blog.models.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    age = Column(Integer)
    articles = db.relationship('Article', backref='user')
    is_staff = Column(Boolean, default=False)


    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    text = Column(Text, nullable=False)
    author = Column(Integer, ForeignKey('user.id'))
    is_delete = Column(Boolean, default=False)


    def __repr__(self):
        return f'<Cтатья "{self.title}"'