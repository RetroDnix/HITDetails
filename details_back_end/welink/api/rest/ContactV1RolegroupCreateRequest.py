#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建角色组
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/l7m80w
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RolegroupCreateRequest(RestApi):
    """创建角色组"""

    def __init__(self, url):
        super().__init__(url)
        self.corp_role_group_id = None
        self.role_group_name = None

    def get_valid_path(self):
        return ("/api/contact/v1/rolegroup/create",)

    def get_rest_method(self):
        return "POST"
