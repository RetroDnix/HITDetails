#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询公告组件
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/dlswid
@author: wecode@huawei.com
"""
from welink.api.articles import Article
from welink.api.base import RestApi


class KnowledgeV1ComponentListRequest(RestApi):
    """查询公告分类"""

    def __init__(self, url):
        super().__init__(url)

    def get_valid_path(self):
        return ("/api/knowledge/v1/component/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
