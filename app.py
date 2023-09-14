from flask import Flask #import Flask module from flask package
from flask import render_template #import render_template from flask package
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

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

@app.route('/', methods=['GET','POST'])
def hello_world():
    # return '<p>Hello world<p>'
    if request.method=="POST":
        # print("post")
        form_title = request.form['title']
        form_desc = request.form['desc']
        if form_title and form_desc:
            todo = Todo(title=form_title, desc=form_desc)
            todo.verified=True
            
            db.session.add(todo)
            db.session.commit()
            
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('index.html', allTodo=allTodo)


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is Product Page'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)  #if run via python app.py then can change port-->>   ,port=8000
#also running through app.py method instead of flask run the changes made in the code will be automatically reflected