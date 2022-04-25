from flask import render_template, url_for, flash, redirect, request
from autopal import app, db, bcrypt
from autopal.forms import BudgetAssistantForm, RegistrationForm, LoginForm, CalculateForm
from autopal.models import user
from flask_login import login_user
from autopal.utils import InterestCalculator, TaxAPI, BudgetAssistant, weatherAPI, newsAPI
from flask_mail import Mail, Message
import smtplib
import os

@app.route('/') 
def index():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    weatherinfo = weatherAPI(ip_address)
    newsinfo = newsAPI()
    return render_template('index.html', weatherinfo=weatherinfo, newsinfo=newsinfo)

@app.route('/test')
def test():
    return render_template('test.html')    

@app.route("/registration", methods=['GET', 'POST'])
def register():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    weatherinfo = weatherAPI(ip_address)
    newsinfo = newsAPI()
    EMAIL_ADDRESS = 'autopalasu@gmail.com'#os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = 'Capstone'#os.environ.get('EMAIL_PASS')    
    form = RegistrationForm()

    if form.validate_on_submit():
        server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Registration Successful'
        body = 'Hello! This email was sent to inform you that you have successfully registered with AutoPal!'
        msg = f'Subject: {subject}\n\n{body}'

        server.sendmail(EMAIL_ADDRESS, form.email.data, msg)

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        newuser = user(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(newuser)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'isa_success')
        return redirect(url_for('index'))                     
    return render_template('registration.html', title='Register', form=form, weatherinfo=weatherinfo, newsinfo=newsinfo)

@app.route("/login", methods=['GET', 'POST'])
def login():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    weatherinfo = weatherAPI(ip_address)
    newsinfo = newsAPI()
    form = LoginForm()  
    if form.validate_on_submit():
        session = user.query.filter_by(email=form.email.data).first()
        if session and bcrypt.check_password_hash(session.password, form.password.data):
            login_user(session, remember=form.remember.data)
            flash(f"You have logged in as {form.email.data}!", 'isa_success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'isa_error')
    return render_template('login.html', title='Login', form=form, weatherinfo=weatherinfo, newsinfo=newsinfo)

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    weatherinfo = weatherAPI(ip_address)
    newsinfo = newsAPI()
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
        total_price=total_price, weatherinfo=weatherinfo, newsinfo=newsinfo
        )

@app.route("/budgetassistant", methods=['GET', 'POST'])
def budget_assistant():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    weatherinfo = weatherAPI(ip_address)
    newsinfo = newsAPI()
    form = BudgetAssistantForm()
    dti = 0
    dti_tier = 0
    dti_text = " "
    tier1 = False
    tier2 = False
    tier3 = False

    if form.validate_on_submit():
        monthly_income = (form.monthly_income1.data + form.monthly_income2.data) 
        annual_income = (form.annual_income1.data + form.annual_income2.data)
        monthly_savings = (form.monthly_savings1.data + form.monthly_savings2.data + form.monthly_savings3.data)
        monthly_debt = (form.monthly_debt1.data + form.monthly_debt2.data + form.monthly_debt3.data + form.monthly_debt4.data + form.monthly_debt5.data + form.monthly_debt6.data + form.monthly_debt7.data)
        annual_debt = (form.annual_debt1.data + form.annual_debt2.data + form.annual_debt3.data + form.annual_debt4.data + form.annual_debt5.data)

        final_monthly_income = (monthly_income + (annual_income/12))
        final_monthly_debt = (monthly_savings + monthly_debt + (annual_debt/12))
        dti, dti_tier, dti_text = BudgetAssistant(final_monthly_income, final_monthly_debt)

        if dti_tier == 1:
            tier1 = True
        elif dti_tier == 2:
            tier2 = True
        elif dti_tier == 3:
            tier3 = True
        

    return render_template('budget_assistant.html', title='Budget Assistant', form=form, dti=dti, dti_tier=dti_tier, dti_text=dti_text, tier1=tier1, tier2=tier2, tier3=tier3, weatherinfo=weatherinfo, newsinfo=newsinfo)
