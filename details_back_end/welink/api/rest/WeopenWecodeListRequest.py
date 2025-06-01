#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询应用列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/iss5uj
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WeopenWecodeListRequest(RestApi):
    """查询公告文章列表"""

    def __init__(self, url):
        super().__init__(url)
        self.type = None
        self.edition = None
        self.page = None
        self.pageSize = None

    def get_valid_path(self):
        return ("/api/weopen/wecode/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
