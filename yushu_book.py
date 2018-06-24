# -*- coding: utf-8 -*-
from httper import HTTP


class YuShuBook:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)  # python 默认会将json转换为dict
        return result

    @classmethod
    def search_by_keyword(cls,keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result

# 9787501524044 测试ISBN
