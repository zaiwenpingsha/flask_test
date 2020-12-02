from flask import Flask

app = Flask(__name__)


@app.route('/index/')
def index():
    return '今天阴天,明天不知道'

if __name__ == '__main__':
    app.run(debug=True)
