from flask import Flask
from flask import make_response

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


app.run(debug=app.config["DEBUG"])

