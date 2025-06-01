#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取角色详情
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/07fmvz
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RoleDetailRequest(RestApi):
    """获取角色详情"""

    def __init__(self, url):
        super().__init__(url)
        self.role_id = None
        self.corp_role_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/role/detail",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
