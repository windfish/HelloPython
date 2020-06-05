from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    # 从request 对象读取表单内容
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin_ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()

# Flask 默认支持的模板是jinja2
# jinja2 中用{{ name }}表示一个需要替换的变量；用{% ... %}表示指令

# 其他常见的模板：
# Mako 用<% ... %> 和 ${xxx} 的一个模板
# Cheetah 用<% ... %> 和 ${xxx} 的一个模板
# Django 一站式框架，内置了一个用{% ... %}和{{ xxx }}的模板
