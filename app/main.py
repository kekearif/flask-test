# main.py
from flask import Blueprint

main = Blueprint('main',__name__)
@main.route("/")
def hello():
    return "Hello World!"

@main.route("/keke/")
def keke():
    return "Hello Keke!"

@main.route("/elly/")
def keke():
    return "Hello Elly!"
