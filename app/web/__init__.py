from flask import Blueprint
web = Blueprint('web', __name__)    # 指定蓝图名字，以及所在的包

from app.web import book
from app.web import user