from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'f453ce6c9f307342c7e1fe6857315d4f'

#next section is for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app) 
#end of section for database
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from autopal import routes