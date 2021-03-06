# -*- coding: utf-8 -*-
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web


@web.route('/book/search/')
def search():

    # 验证层，对参数进行校验
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.replace(' ', '')
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)  # flask自带的返回json
    else:
        return jsonify(form.errors)
