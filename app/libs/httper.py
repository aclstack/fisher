# -*- coding: utf-8 -*-
import requests


class HTTP:
    @staticmethod       # 静态方法
    def get(url, return_json=True):
        r = requests.get(url=url)
        # 判断返回状态码
        if r.status_code != 200:
            return {} if return_json else ''    # 三元运算简化代码
        return r.json() if return_json else r.text
