#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除角色
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/flcud7
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RoleDeleteRequest(RestApi):
    """删除角色"""

    def __init__(self, url):
        super().__init__(url)
        self.role_id = None
        self.corp_role_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/role/delete",)

    def get_rest_method(self):
        return "POST"
