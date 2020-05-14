from app import app
from app import db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import request
from flask import render_template,flash,redirect, url_for
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required

def index():
    posts = [
        {
           'author':{'username': 'John'},
           'body': '''Beautiful day in Portugal! The sun is so sunny and warm and the sky is so blue
            it is a lovely day to be out in the sun, playing on the beach!'''
        },
        {
           'author':{'username': 'Susan'},
           'body': '''The Avengers movie was so cool! I can't wait until the the next one!'''
        },
        {
           'author':{'username': 'Emmanuela'},
           'body': '''The trees sure all tall today! I love my blue jean overalls'''
        }

    ]
    return render_template('index.html', title='Home Page', posts=posts)


@app.route('/login', methods =['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
       user = User.query.filter_by(username=form.username.data).first()
       if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect(url_for('login'))
       login_user(user, remember=form.remember_me.data)
       next_page = request.args.get('next')
       if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
       return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/registration',methods =['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        newUser = User(username=form.newusername.data,email = form.newemail.data)
        newUser.set_password(form.newpassword.data)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)