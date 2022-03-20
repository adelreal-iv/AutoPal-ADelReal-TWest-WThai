from flask_wtf import FlaskForm                                                #Forms library
from wtforms import StringField, PasswordField, SubmitField, BooleanField      #Included with wtf forms
from wtforms.validators import DataRequired, Length, Email, EqualTo            #Input validation

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

class LoginForm(FlaskForm):
        email = StringField('Email',                                                    #Validates email for signing in as opposed to username
                                validators=[DataRequired(), Email()])
        password = PasswordField('Password', 
                                validators=[DataRequired()])                                
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')



