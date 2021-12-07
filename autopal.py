from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

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
