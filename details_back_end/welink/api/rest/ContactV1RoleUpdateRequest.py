#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新角色
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/3r3an6
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RoleUpdateRequest(RestApi):
    """更新角色"""

    def __init__(self, url):
        super().__init__(url)
        self.role_id = None
        self.corp_role_id = None
        self.role_name = None
        self.role_group_id = None
        self.corp_role_group_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/role/update",)

    def get_rest_method(self):
        return "POST"
