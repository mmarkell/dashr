from dasher import *
import models

import sqlite3
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash

@app.route('/')
def render_splash_page():
    return render_template('index.html')

@app.route('/home')
def render_home_page():
    users = db.session.query(models.User).all()
    return render_template('home.html', users=users)

@app.route('/herds')
def render_herds_page():
    herds = db.session.query(models.Interest).all()
    return render_template('herds.html', herds=herds)

@app.route('/profile/<int:user_id>')
def render_profile_page(user_id):
    user = db.session.query(models.User).filter_by(id=3).first()
    return render_template('profile.html', user=user)
