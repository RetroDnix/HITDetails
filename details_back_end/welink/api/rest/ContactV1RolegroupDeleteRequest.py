#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除角色组
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/wol4tp
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RolegroupDeleteRequest(RestApi):
    """删除角色组"""

    def __init__(self, url):
        super().__init__(url)
        self.role_group_id = None
        self.corp_role_group_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/rolegroup/delete",)

    def get_rest_method(self):
        return "POST"
