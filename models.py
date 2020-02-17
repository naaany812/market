from sqlalchemy_utils import PhoneNumberType, EmailType, PasswordType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mail = db.Column(EmailType(), unique=True, nullable=False)
    password = db.Column(PasswordType(), nullable=False)
    address = db.Column(db.String, nullable=False)
    orders = db.relationship("", back_populates="user")
    


class Meal(db.Model):
    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    picture = db.Column(db.String, nullable=False, unique=True)
    category = db.relationship("Category", back_populates="meals")
    category_id = db.Column(db.Integer, db.ForeignKey="categories.id")


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    meals = db.relationship("Dish", back_populates="category")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    summary = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    user = db.relationship("User", back_populates="orders")
    user_id = db.Column(db.Integer, ForeignKey="users.id")
