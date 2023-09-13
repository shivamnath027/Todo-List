from flask import Flask #import Flask module from flask package
from flask import render_template #import render_template from flask package
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def hello_world():
    # return '<p>Hello world<p>'
    return render_template('index.html')


@app.route('/product')
def greet():
    return "<h1>This is Product Page<h1>"


if __name__ == "__main__":
    app.run(debug=True)  #if run via python app.py then can change port-->>   ,port=8000
#also running through app.py method instead of flask run the changes made in the code will be automatically reflected