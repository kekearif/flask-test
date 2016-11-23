# __init__.py
from flask import Flask
from main import main
app = Flask(__name__)
app.register_blueprint(main)

@app.errorhandler(404)
def page_not_found(e):
    return app.send_static_file("static/404_error.html")
