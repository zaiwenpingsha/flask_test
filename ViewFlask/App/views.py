import uuid

from flask import Blueprint, url_for, request

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


# request
@blue.route('/testRequest/', methods=['post', 'get'])
def testRequest():
    # method是获取请求方式
    print(request.method)

    # 获取的是一个全路径
    print(request.url)
    # 获取的是不带请求参数的url
    print(request.base_url)
    # 获取的是一个全路径
    print(request.host_url)

    # 获取请求的客户端ip  应用场景就是反扒
    print(request.remote_addr)

    # http://www.baidu.com/s?name=zs&age=18&sex=nv
    # 获取get请求方式的参数
    # ImmutableMultiDict([('age', '18'), ('name', "'zs'")])
    print(request.args)
    print(request.args.get('name'))

    # 获取post请求方式的参数
    # ImmutableMultiDict([('name', 'zs'), ('age', '18')])
    print(request.form)
    print(request.form.get('name'))

    # request.file用户文件上传

    # 获取的是请求头
    print(request.headers)

    # 获取的是请求资源路径
    print(request.path)

    return 'testRequest'