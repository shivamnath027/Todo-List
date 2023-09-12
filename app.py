from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Hello world<p>'

@app.route('/product')
def greet():
    return "<h1>This is Product Page<h1>"


if __name__ == "__main__":
    app.run(debug=True)  #if run via python app.py then can change port-->>   ,port=8000
#also running through app.py method instead of flask run the changes made in the code will be automatically reflected