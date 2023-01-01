from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project.db"

db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_al()

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
@app.route('/orderpage')
def order():
    items=[{'id':1,'name':'jac n jones blue jeans'},
        {'id':2 ,'name':'armani'},
        {'id':3 ,'name':'gucci'}
    ]
    return render_template("orderpage.html",items=items)

if __name__ == '__main__' :
    app.run(port=5001,debug=True)
