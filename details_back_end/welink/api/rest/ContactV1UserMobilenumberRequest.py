#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修改用户手机号
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/26v7vi?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1UserMobilenumberRequest(RestApi):
    """修改用户手机号"""

    def __init__(self, url):
        super(ContactV1UserMobilenumberRequest, self).__init__(url)
        # 以下是接口的参数
        self.corp_user_id = None
        self.user_id = None
        self.mobile_number = None

    def get_valid_path(self):
        return ("/api/contact/v1/user/mobilenumber",)

    def get_rest_method(self):
        return "PUT"
