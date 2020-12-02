from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app=app)


@app.route('/index3/')
def index3():
    return 'index3'

# 视图函数返回页面
@app.route('/index4/')
def index4():
    return render_template('index4.html')

if __name__ == '__main__':
    manager.run()
