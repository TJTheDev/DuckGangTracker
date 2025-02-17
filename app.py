from flask import Flask
from flask import render_template, redirect, request, url_for, flash
import database
from sqlalchemy import MetaData, create_engine, Column, String, Integer
from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List, Optional
from pprint import pprint
from flask_wtf.csrf import CSRFProtect
import forms
import os 
from flask_bootstrap import Bootstrap

from datetime import datetime

from flask_login import LoginManager, login_user, login_required, current_user
login_manager = LoginManager()

app = Flask(__name__)
login_manager.init_app(app)
Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return database.Users.query.get(int(user_id))


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////usr/src/app/data/database.db"
app.config["SECRET_KEY"] = os.urandom(32)
database.db.init_app(app)
with app.app_context():
    database.db.create_all()

@app.route("/")
def hello_world():
    users = database.db.session.execute( database.db.select(database.Users) ).scalars()
    return render_template('index.html', users=users)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form =  forms.LoginForm()
    if request.method == 'POST'and form.validate_on_submit():
        #user = database.Users(name = request.form['name'], password = request.form['password'], number = 0)
        user = database.Users(name = request.form['name'], password = request.form['password'])
        database.db.session.add(user)
        database.db.session.commit()
        return(redirect(url_for('login')))
    return(render_template('register.html', form=form))



@app.route("/user/<int:id>", methods=['GET', 'POST'])
@login_required
def user_detail(id):
    if(current_user.id != id):
        return(redirect('https://www.youtube.com/watch?v=xvFZjo5PgG0'))

    pprint(current_user)
    user = database.db.get_or_404(database.Users, id)
    if request.method == 'POST': 
        user.pushups.append( database.Pushups(date=datetime.now(), number=int(request.form['increment'])))
        #user.number += int(request.form['increment'])
        database.db.session.add(user)
        database.db.session.commit()
        return(redirect(url_for('hello_world')))

    form = forms.IncreaseForm()
    return( render_template('increase.html', form=form, user=user))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = database.db.session.query(database.Users).filter(database.Users.name == request.form['name']).first()
        if user and request.form['password'] == user.password:
            print(f"{user} logged in")
            login_user(user)
            pprint(f"{user.name} {user.is_authenticated}")
            #return(redirect(url_for('user_detail', id=user.id)))
            return(redirect(url_for('hello_world')))


    return(render_template('login.html', form=form))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
