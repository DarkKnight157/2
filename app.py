import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# 留言列表
messages = []

# 首页
@app.route('/')
def index():
    return '<h1>Hello</h1>', 200
    # return render_template('index.html.jinja2', messages=messages)


# 提交留言
@app.route('/post/add', methods=['POST'])
def post_add():
    content = request.form.get('content')
    if content:
        # 如果留言内容非空，则添加到留言列表中
        message = {
            'time': datetime.datetime.now(),
            'content': content
        }
        messages.append(message)
    return index()

if __name__ == '__main__':
    app.run()