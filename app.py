from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.secret_key = 'It is my shop! My shop is cool'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/cart/")
def cart():
    return render_template("cart.html")


@app.route("/account/")
def account():
    return render_template("account.html")


@app.route("/login/")
def login():
    return render_template("auth.html")


@app.route("/logout/")
def logout():
    return render_template("auth.html")


if __name__ == '__main__':
    app.run()
