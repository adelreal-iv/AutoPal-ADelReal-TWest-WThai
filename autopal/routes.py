from flask import render_template, url_for, flash, redirect
from autopal import app, db, bcrypt
from autopal.forms import RegistrationForm, LoginForm
from autopal.models import user
from flask_login import login_user

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/test') 
def test():
    return render_template('test.html')    

@app.route("/registration", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        newuser = user(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(newuser)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'isa_success')
        return redirect(url_for('index'))                     
    return render_template('registration.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        session = user.query.filter_by(email=form.username.data).first()
        if session and bcrypt.check_passwod_has(user.password, form.password.data):
            login_user(session, remember=form.remember.data)
            return redirect(url_for('home))'))
        else:
            flash("login Unsuccessful. Please check email and password")
    return render_template('login.html', title='Login', form=form)

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')