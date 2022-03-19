from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  #for database

app = Flask(__name__, static_url_path='/static')

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

@app.route("/login")
def login():                     #Note to self, be careful not to duplicate function names
    return render_template('login.html')

@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route("/calculator")
def calculator():
    return render_template('calculator.html')

#dont worry about this for now
if __name__ == '__main__':
    app.run(debug=True)


#this is a test
#testing commit
