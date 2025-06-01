#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询公告分类
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/r7prtj
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class KnowledgeV1CategoryListRequest(RestApi):
    """查询公告分类"""

    def __init__(self, url):
        super().__init__(url)
        self.component_id = None

    def get_valid_path(self):
        return ("/api/knowledge/v1/category/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
