#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询应用详情
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/0hj43s
@author: wecode@huawei.com
"""
from welink.api.articles import Article
from welink.api.base import RestApi


class WeopenWecodeDetailRequest(RestApi):
    """查询应用详情"""

    def __init__(self, url):
        super().__init__(url)
        self.client_id = None
        self.edition = None

    def get_valid_path(self):
        return ("/api/weopen/wecode/detail",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
