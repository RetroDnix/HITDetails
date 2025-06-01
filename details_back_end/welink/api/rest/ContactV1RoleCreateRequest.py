#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建角色
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/rzmvo4
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RoleCreateRequest(RestApi):
    """创建角色"""

    def __init__(self, url):
        super().__init__(url)
        self.corp_role_id = None
        self.role_name = None
        self.role_group_id = None
        self.corp_role_group_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/role/create",)

    def get_rest_method(self):
        return "POST"
