#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询指定角色用户列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/zh8zor
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RoleSimplelistRequest(RestApi):
    """查询指定角色用户列表"""

    def __init__(self, url):
        super().__init__(url)
        self.role_id = None
        self.corp_role_id = None
        self.page_no = None
        self.page_size = None

    def get_valid_path(self):
        return ("/api/contact/v1/role/simplelist",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
