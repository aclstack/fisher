from flask import Flask
from flask import make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    headers = {
        'content-type': 'application/json'
       # 'location': 'https://www.baidu.com'  #跳转
    }

    response = make_response('<html></html>')
    response.headers = headers
    return response
    # return "Hello World"


app.run(debug=app.config["DEBUG"])

