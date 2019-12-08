# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Посмотри логинчик! {}, Запоминашечки!={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='ЛЕТСГОШЕЧКИ!', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Linocka'}
    return render_template('nikituluv.html', title='Home', user=user)
