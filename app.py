from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello its a simple webapp written in python and depend on flask"