#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户详情
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/dt3t14
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class ContactV2UserDetailRequest(RestApi):
    """查询用户详情"""

    def __init__(self, url):
        super().__init__(url)
        self.corp_user_id = None
        self.user_id = None
        self.mobile_number = None

    def get_valid_path(self):
        return ("/api/contact/v2/user/detail",)

    def get_rest_method(self):
        return "POST"
