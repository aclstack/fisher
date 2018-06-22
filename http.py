# -*- coding: utf-8 -*-
import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url=url)
        # 判断返回状态码
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
