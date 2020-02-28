from flask import render_template, redirect, session, request
from market.models import Category, Meal, User, Order
from random import sample
from market.forms import OrderForm, AuthenticationForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from market import app, db


def get_cart_values():
    cart = session.get('cart', [])
    price = 0
    result = dict()
    meals = []
    count = 0
    if cart:
        count = len(cart)
        for meal_id in cart:
            meal = db.session.query(Meal).get(meal_id)
            price += meal.price
            meals.append(meal)

    result['count'] = count
    result['meals'] = meals
    result['price'] = price
    return result


@app.route("/")
def main():
    categories = db.session.query(Category).all()
    meals = {}
    for c in categories:
        random_meals = sample(c.meals, 3)
        meals[c.title] = random_meals
    cart = get_cart_values()
    return render_template(
        "main.html",
        meals=meals,
        cart=cart)


@app.route("/cart/", methods=["GET", "POST"])
def cart():
    dateTimeObj = datetime.now()
    cart = get_cart_values()
    is_deleted = session.get('is_deleted', False)
    if is_deleted:
        session.pop('is_deleted')
    form = OrderForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            return render_template(
                "cart.html",
                cart=cart,
                is_deleted=is_deleted,
                form=form)
        user = db.session.query(User).filter(
            User.mail == form.mail.data).first()
        if not user:
            user = User(
                name=form.name.data,
                mail=form.mail.data,
                address=form.address.data,
                phone=form.phone.data
            )
            db.session.add(user)
            db.session.commit()
            session["is_user_created"] = True
        user_id = user.id
        session_cart = session.get('cart', [])
        order = Order(
            date=dateTimeObj.strftime("%d-%b-%Y"),
            summary=cart.get('price'),
            status="Выполняется",
            meal_list=session_cart,
            user_id=user_id
        )
        db.session.add(order)
        db.session.commit()
        session.pop('cart')
        return redirect("/ordered/")
    return render_template(
        "cart.html",
        cart=cart,
        is_deleted=is_deleted,
        form=form)


@app.route("/addtocart/<int:meal_id>/")
def add_to_cart(meal_id):
    cart = session.get('cart', [])
    cart.append(meal_id)
    session['cart'] = cart
    return redirect("/cart/")


@app.route("/deletefromcart/<int:meal_id>")
def delete_from_cart(meal_id):
    session['is_deleted'] = True
    cart = session.get('cart', [])
    cart.remove(meal_id)
    session['cart'] = cart
    return redirect("/cart/")


@app.route("/account/")
def account():
    cart = get_cart_values()
    user = session.get('user')
    orders_list = db.session.query(Order).filter(
        Order.user_id == user.get('id')).all()
    orders = []
    for o in orders_list:
        meals = []
        meal_list = o.meal_list
        for meal_id in meal_list:
            m = db.session.query(Meal).get(meal_id)
            meal = {
               'title': m.title,
               'price': m.price
            }
            meals.append(meal)
        order = {
            'date': o.date,
            'summary': o.summary,
            'meals': meals
        }
        orders.append(order)
    return render_template(
        "account.html",
        orders=orders,
        cart=cart)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = AuthenticationForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            return render_template(
                "auth.html",
                form=form
            )
        user = db.session.query(User).filter(
            User.mail == form.mail.data).first()
        if not user:
            user = User(
                mail=form.mail.data,
                password=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
        if not user.password and session.get(
                    'is_user_created'):
            session['is_user_created'] = False
            user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
        if not check_password_hash(user.password, form.password.data):
            form.mail.errors.append("Неверное имя или пароль")
            return render_template(
                "auth.html",
                form=form)
        session["user"] = {
                "id": user.id,
                "mail": user.mail
            }
        return redirect("/account/")

    return render_template(
        "auth.html",
        form=form)


@app.route("/logout/")
def logout():
    if session.get('user'):
        session.pop("user")
    return redirect("/login/")


@app.route("/ordered/")
def ordered():
    return render_template("ordered.html")