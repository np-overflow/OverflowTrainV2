from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello"