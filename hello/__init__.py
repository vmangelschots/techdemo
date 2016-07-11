from flask import Flask
app = Flask("hello")

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
    
