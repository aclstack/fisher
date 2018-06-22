from flask import Flask
from flask import make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    headers = {
        'content-type': 'application/json'   # 返回类型指定为json
        # 'location': 'https://www.baidu.com' #跳转
    }

    response = make_response('<html></html>',301)
    response.headers = headers
    return response


@app.route('/easy')
def index():
    headers = {
        'content-type': 'application/json'   # 指定客户端解析类型
    }
    return 'easy response', 200, headers


@app.route('/book/search/<q>/<page>')
def search(q, page):
    # q 搜索关键字
    isbn_or_key = is_isbn_or_key(q)

    return 'Hi'

app.run(debug=app.config["DEBUG"])

