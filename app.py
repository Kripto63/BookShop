"""Init site"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Home page site"""
    return "hellow"
