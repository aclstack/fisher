# -*- coding: utf-8 -*-
from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)  # python 默认会将json转换为dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return (page - 1) * current_app.config['PER_PAGE']

# 9787501524044 测试ISBN
