from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class OrderForm(FlaskForm):
    name = StringField(
        'Ваше имя',
        validators=[DataRequired()])
    phone = StringField(
        'Tелефон',
        validators=[DataRequired()])
    address = StringField(
        'Адрес',
        validators=[DataRequired()])
    mail = StringField(
        'Электропочта',
        validators=[DataRequired(), Email("Невалидный адрес Электропочта!")])
    date = StringField('date')
    status = StringField('status')
    user_id = IntegerField('user_id')
    submit = SubmitField('Оформить заказ')


class AuthenticationForm(FlaskForm):
    mail = StringField(
        'Электропочта',
        validators=[DataRequired(), Email("Невалидный адрес Электропочта!")])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
