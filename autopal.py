from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home")
def home():                     #Note to self, be careful not to duplicate function names
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

#dont worry about this for now
if __name__ == '__main__':
    app.run(debug=True)


#this is a test