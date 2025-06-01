#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询公告文章列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/pgu8ti
@author: wecode@huawei.com
"""
from welink.api.articles import Article
from welink.api.base import RestApi


class KnowledgeV1ArticleListRequest(RestApi):
    """查询公告文章列表"""

    def __init__(self, url):
        super().__init__(url)
        self.component_id = None
        self.category_id = None
        self.user_id = None
        self.corp_user_id = None
        self.offset = None
        self.limit = None

    def get_valid_path(self):
        return ("/api/knowledge/v1/article/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
