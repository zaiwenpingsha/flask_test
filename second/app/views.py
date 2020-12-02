from flask import Blueprint

# from manager import app

blue = Blueprint('first', __name__)


# @app.route('/')
@blue.route('/')
def hello_world():
    return 'Hello World!'
