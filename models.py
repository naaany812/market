from sqlalchemy_utils import EmailType
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mail = db.Column(EmailType(), unique=True, nullable=False)
    password = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    orders = db.relationship("Order", back_populates="user")


class Meal(db.Model):
    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    picture = db.Column(db.String, nullable=False, unique=True)
    category = db.relationship("Category", back_populates="meals")
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    meals = db.relationship("Meal", back_populates="category")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    summary = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    meal_list = db.Column(db.JSON, nullable=False)
    user = db.relationship("User", back_populates="orders")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
