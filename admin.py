"""from market import app, db
from market.models import Category, Meal, User, Order
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

admin = Admin(app=app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Meal, db.session))
admin.add_view(ModelView(Category, db.session))"""
