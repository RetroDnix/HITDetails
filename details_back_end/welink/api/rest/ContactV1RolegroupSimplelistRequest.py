#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取角色组列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/pe90ms
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RolegroupSimplelistRequest(RestApi):
    """获取角色组列表"""

    def __init__(self, url):
        super().__init__(url)

    def get_valid_path(self):
        return ("/api/contact/v1/rolegroup/simplelist",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
