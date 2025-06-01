#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取分域管理员管理的部门范围
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/a4oido
@author: wecode@huawei.com
"""
from welink.api.articles import Article
from welink.api.base import RestApi


class AdmincenterV1UserDomainScopeRequest(RestApi):
    """获取分域管理员管理的部门范围"""

    def __init__(self, url):
        super().__init__(url)
        self.user_id = None

    def get_valid_path(self):
        return ("/api/admincenter/v1/user/domain/scope",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
