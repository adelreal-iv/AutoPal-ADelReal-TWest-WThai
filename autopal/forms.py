from xml.dom import ValidationErr
from flask_wtf import FlaskForm                                                #Forms library
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField      #Included with wtf forms
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError           #Input validation
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
        loan_amount = DecimalField('Vehicle Base Price', places = 2,                                                   #Validates email for signing in as opposed to username
                                validators=[DataRequired()])
        interest = DecimalField('Interest Rate', places = 2, 
                                validators=[DataRequired()])
        months = IntegerField('Loan Term in Months', 
                                validators=[DataRequired()])
        city = StringField('City of Residence',
                                validators=[DataRequired()])                                
        submit = SubmitField('Calculate')
        



