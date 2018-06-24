# from flask import Flask
#
# # app = Flask(__name__)
# # app.config.from_object('config')
from app import create_app


app = create_app()


@app.route('/')
def index():
    return "Hello World"


app.run(debug=app.config["DEBUG"])
