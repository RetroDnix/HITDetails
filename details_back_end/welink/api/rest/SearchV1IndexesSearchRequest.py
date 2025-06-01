#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
搜索服务-搜索企业数据
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/n6yo5s
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class SearchV1IndexesSearchRequest(RestApi):
    """搜索服务-搜索企业数据"""

    def __init__(self, url):
        super().__init__(url)
        self.text = None
        self.size = None
        self.from_ = None

    def get_valid_path(self):
        return ("/api/search/v1/indexes/search",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = super().get_body_params()
        if "from_" in _body_params:
            _body_params["from"] = _body_params["from_"]
            del _body_params["from_"]
        return _body_params
