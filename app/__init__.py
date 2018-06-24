from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


# 蓝图注册函数
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

