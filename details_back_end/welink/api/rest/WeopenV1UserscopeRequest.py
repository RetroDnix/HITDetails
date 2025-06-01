#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询某We码的可见范围

@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WeopenV1UserscopeRequest(RestApi):
    """查询某We码的可见范围"""

    def __init__(self, url):
        super().__init__(url)
        self.page = None
        self.page_size = None

    def get_valid_path(self):
        return ("/api/weopen/v1/userscope",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
