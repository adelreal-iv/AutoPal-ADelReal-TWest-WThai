from flask import render_template, url_for, flash, redirect
from autopal import app, db, bcrypt
from autopal.forms import RegistrationForm, LoginForm, CalculateForm
from autopal.models import user
from flask_login import login_user
from autopal.utils import InterestCalculator, TaxAPI

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

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalculateForm()
    base_price = 0
    monthly_payment = 0 
    interest_charge = 0
    final_amount = 0
    last_payment = 0
    total_payments = 0
    total_price = 0
    city = " "
    tax_rate = 0

    
    if form.validate_on_submit():
        city, tax_rate = TaxAPI(form.city.data)
        monthly_payment, interest_charge, final_amount, last_payment, total_price = InterestCalculator(
            form.loan_amount.data, form.months.data, form.interest.data, last_payment, tax_rate)
        
        total_payments = form.months.data
        base_price = form.loan_amount.data
    
    return render_template('calculator.html', title='Calculator',
        form=form, monthly_payment=monthly_payment,
        interest_charge=interest_charge, final_amount=final_amount,
        last_payment=last_payment, total_payments=total_payments,
        tax_rate=tax_rate, city=city, base_price=base_price,
        total_price=total_price
        )