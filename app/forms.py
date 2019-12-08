# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имечко', validators=[DataRequired()])
    password = PasswordField('Парольчик', validators=[DataRequired()])
    remember_me = BooleanField('Запоминашки?')
    submit = SubmitField('Войтишечки')