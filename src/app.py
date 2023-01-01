from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/login')

def login():
    return render_template("loginpage.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == '__main__' :
    app.run(port=5001,debug=True)
