from blog.app import create_app
from blog.models.database import db
from werkzeug.security import generate_password_hash
from blog.app import app


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port="8080",
    )

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Миграции сделаны!")


@app.cli.command("create_users")
def create_users():
    from blog.models import User
    admin = User(
        username = input('Введите username: '), 
        email = input('Введите email: '), 
        is_staff = True, 
        password = generate_password_hash(input('Введите пароль: '))
    )
    test_user = User(
        username = "user",
        email = "user@mail.ru",
        is_staff = False,
        password = generate_password_hash(input("Введите пароль для user"))
    )
    db.session.add(admin)
    db.session.add(test_user)
    db.session.commit()

    print("Созданы 2 пользователя: admin и user")
