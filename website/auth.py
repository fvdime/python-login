from flask import Blueprint, render_template, request, flash, redirect, url_for
# Blueprint means it has bunch of files in it
from flask_login import current_user, login_user, login_required, logout_user
from .models import User
#way to secure a pasword
from werkzeug.security import generate_password_hash, check_password_hash
from . import db




auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #when u r looking for a specific entry in your db
        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/hdff')
def hdffPage():
    return render_template("hdff.html", user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #we are getting all the information from sign up
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. ', category='error')
        elif len( email ) < 4:
            flash('Email must be longer than 3 characters!', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        elif len(password1) < 7:
            flash('Password must be longer than 6 characters!', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            #add user to database
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)



#URL is get request, pressing the submit is post request