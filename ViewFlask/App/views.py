import uuid

from flask import Blueprint, url_for

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello aaaaa!'


# 路由参数

# 路由参数基本使用，默认是字符串类型
@blue.route('/testbase/<id>/')
def testbase(id):
    return '路由参数基本使用'


# 路由参数----字符串类型
@blue.route('/teststr/<string:a>/')
def teststr(a):
    print(a)
    print(type(a))
    return '测试路由参数是字符串类型'


# 路由参数----整数的类型
@blue.route('/testint/<int:b>/')
def testint(b):
    print(b)
    print(type(b))
    return '路由参数测试整数类型'


# 路由参数----path
@blue.route('/testpath/<path:c>/')
def testpath(c):
    print(c)
    print(type(c))
    return '路由参数测试path'


# 路由参数----float
@blue.route('/testfloat/<float:d>/')
def testfloat(d):
    print(d)
    print(type(d))
    return '路由参数测试float'


# 产生uuid
@blue.route('/makeuuid/')
def makeuuid():
    u = uuid.uuid4()
    print(u)
    return '产生uuid'


# 路由参数----uuid
@blue.route('/testuuid/<uuid:e>/')
def testuuid(e):
    print(e)
    print(type(e))
    return '路由参数测试uuid'


# 路由参数----any
@blue.route('/testany/<any(a,b):c>/')
def testany(c):
    print(c)
    print(type(c))
    return '路由参数测试any'


# 视图函数的请求方式
# 默认是get
@blue.route('/testmethod/', methods=['post'])
def testmethod():
    return '视图函数的请求方式'


# 反向解析
@blue.route('/index/')
def index():
    return 'index'


@blue.route('/index1/')
def index1():
    a = url_for('blue.index')
    print(a)
    return 'index1'