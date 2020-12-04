from flask import Blueprint, render_template, request, redirect, url_for

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World  hahah !'


# -----------------------------------
# -----------------------------------
# cookie
# 执行一个请求跳转到一个登录页面
# 在页面中输入一个名字  然后点击提交
# 提交之后跳转到一个欢迎页面   欢迎页面显示 欢迎xxx已登录
# 欢迎页面中有一个退出 点击退出之后  显示 欢迎游客登录
# 如果没有登录 直接跳转到欢迎页面 那么显示欢迎游客登录
@blue.route('/toLogin/')
def toLogin():
    return render_template('login.html')


@blue.route('/login/', methods=['POST'])
def login():
    # 获取post请求的参数的值的方法  request.form.get(input标签的name的属性值)
    name = request.form.get('name')

    # 获取post请求的参数的值的方法  request.form.get(input标签的name的属性值)
    response = redirect(url_for('blue.welcome'))

    # 设置cookie  ‘name’是相当于key  name 相当于value
    # key可以随便设置  但是一般我们设置的key的名字和value一致
    response.set_cookie('name', name)
    return response


@blue.route('/welcome/')
def welcome():
    # request.cookies.get方法的第二个参数  如果获取不到第一个参数的内容的时候
    # 那么就会赋值一个默认值
    name = request.cookies.get('name', '游客')

    # 如果你想把某一个数据放到页面中 那么就可以将这个数据防到render_tempalte方法中进行传递
    # 传递的格式是 render_tempalte('页面',name=name,age=age)
    # 如果已经传递到页面 那么页面可以使用{{name}}
    return render_template('welcome.html', name=name)


@blue.route('/logout/')
def logout():
    # 将cookie中的数据删除 然后重定向到weilcome
    response = redirect(url_for('blue.welcome'))
    response.delete_cookie('name')
    return response
