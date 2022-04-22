from xml.dom import ValidationErr
from flask_wtf import FlaskForm                                                #Forms library
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField      #Included with wtf forms
from wtforms.validators import Optional, DataRequired, Length, Email, EqualTo, ValidationError           #Input validation
from autopal.models import user        

class RegistrationForm(FlaskForm):
        username = StringField('Username', 
                                validators=[DataRequired(), Length(min=6, max=20)])     #Validates username length of 6 to 20 characters
        email = StringField('Email', 
                                validators=[DataRequired(), Email()])
        password = PasswordField('Password', 
                                validators=[DataRequired(), Length(min=6, max=20)])                                
        confirm_password = PasswordField('Confirm Password', 
                                validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')


        def validate_username(self, username):
                newuser = user.query.filter_by(username=username.data).first()
                if newuser:
                        raise ValidationError('That username is taken please choose a different one.')          #validates if username is taken already in the database

        def validate_email(self, email):
                newemail = user.query.filter_by(email=email.data).first()
                if newemail:
                        raise ValidationError('That email is taken please choose a differnet one.')          #validates if email is taken already in the database

class LoginForm(FlaskForm):
        email = StringField('Email',                                                    #Validates email for signing in as opposed to username
                                validators=[DataRequired(), Email()])
        password = PasswordField('Password', 
                                validators=[DataRequired()])                                
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')

class CalculateForm(FlaskForm):
        loan_amount = DecimalField('Vehicle Base Price:', places = 2,                                                   
                                validators=[DataRequired()])
        interest = DecimalField('Interest Rate:', places = 2, 
                                validators=[DataRequired()])
        months = IntegerField('Loan Term in Months:', 
                                validators=[DataRequired()])
        city = StringField('City of Residence Tax Rate (State of CA):',
                                validators=[DataRequired()], render_kw={"placeholder": "Ex: Los Angeles"})                                
        submit = SubmitField('Calculate')
        

class BudgetAssistantForm(FlaskForm):
        monthly_income = 0
        annual_income = 0
        monthly_savings = 0
        monthly_debt = 0
        annual_debt = 0
        
        monthly_income1 = DecimalField('Net Monthly Income:', places = 2,                                                          
                                validators=[Optional()])
        monthly_income2 = DecimalField('Monthly Other (alimony child support, etc):', places = 2,                                                   
                                validators=[Optional()])
        annual_income1 = DecimalField('Annual Gifts:', places = 2,                                                   
                                validators=[Optional()])
        annual_income2 = DecimalField('Annual Tax Return:', places = 2,                                                   
                                validators=[Optional()])
        monthly_savings1 = DecimalField('Emergency Fund:', places = 2,                                                   
                                validators=[Optional()])
        monthly_savings2 = DecimalField('Investments/Dividends:', places = 2,                                                   
                                validators=[Optional()])
        monthly_savings3 = DecimalField('Retirement', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt1 = DecimalField('Loan Payments (refer to our loan calculator):', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt2 = DecimalField('Food and Groceries:', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt3 = DecimalField('Housing (mortgage, rent, taxes):', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt4 = DecimalField('Transportation (gas, public transportation, parking):', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt5 = DecimalField('Health (Doctor visits, insurance, medication):', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt6 = DecimalField('Personal (Hobbies, entertainment, charity):', places = 2,                                                   
                                validators=[Optional()])
        monthly_debt7 = DecimalField('Other:', places = 2,                                                   
                                validators=[Optional()])
        annual_debt1 = DecimalField('Tuition', places = 2,                                                   
                                validators=[Optional()])
        annual_debt2 = DecimalField('Homeowner\'s Renter\'s Insurance', places = 2,                                                   
                                validators=[Optional()])
        annual_debt3 = DecimalField('Taxes', places = 2,                                                   
                                validators=[Optional()])
        annual_debt4 = DecimalField('Vacation', places = 2,                                                   
                                validators=[Optional()])
        annual_debt5 = DecimalField('Other', places = 2,                                                   
                                validators=[Optional()])
        submit = SubmitField('Calculate Debt to Income Ratio')

