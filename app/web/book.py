# -*- coding: utf-8 -*-
from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook


web = Blueprint('web', __name__)    # 指定蓝图名字，以及所在的包


@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)  # flask自带的返回json
