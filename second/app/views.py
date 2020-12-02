from flask import Blueprint

blue = Blueprint('first', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'
