from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from market.config import Config
from market.models import db, Category, Meal, User, Order
from market.views import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Meal, db.session))
admin.add_view(ModelView(Category, db.session))
