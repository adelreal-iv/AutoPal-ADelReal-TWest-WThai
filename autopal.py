from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy  #for database

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'f453ce6c9f307342c7e1fe6857315d4f'


#next section is for database
app.config['SQLAlchemy_DATABASE_URI'] = 'sql:///site.db'  
db = SQLAlchemy(app) 

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
#end of section for database

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/test') 
def test():
    return render_template('test.html', posts=posts)    

@app.route("/registration", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'isa_success')
        return redirect(url_for('index'))                     
    return render_template('registration.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()                     
    return render_template('login.html', title='Login', form=form)

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')

#dont worry about this for now
if __name__ == '__main__':
    app.run(debug=True)
