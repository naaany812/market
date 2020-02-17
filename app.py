from flask import Flask, render_template, request
from random import sample
from models import db, Teacher, Study_Request, Booking
from enums import Goals, Days
from forms import Booking_form, Request_form

app = Flask(__name__)
app.secret_key = 'It is my shop! My shop is cool'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db.init_app(app)


@app.route("/")
def main():
    pass


@app.route("/cart/")
def cart():
    pass


@app.route("/account/")
def account():
    pass


@app.route("/login/")
def login():
    pass


@app.route("/logout/")
def logout():
    pass


if __name__ == '__main__':
    app.run()
