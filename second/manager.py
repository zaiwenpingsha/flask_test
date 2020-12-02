from flask import Flask
from flask_script import Manager

from app import create_app
from app.views import blue

app = create_app()
app.register_blueprint(blueprint=blue)
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
