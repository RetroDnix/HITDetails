#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户详情（新）
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/zuizxb?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV3UsersRequest(RestApi):
    """查询用户详情（新）"""

    def __init__(self, url):
        super(ContactV3UsersRequest, self).__init__(url)
        self.user_id = None
        self.mobile_number = None
        self.corp_user_id = None

    def get_valid_path(self):
        return ("/api/contact/v3/users",)

    def get_rest_method(self):
        return "POST"
