#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除用户
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/1mdou0
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi
from welink.api.rest.ContactV1UserInfo import UserInfo


class ContactV1UserDeleteRequest(RestApi):
    """删除用户"""

    def __init__(self, url):
        super(ContactV1UserDeleteRequest, self).__init__(url)
        self.corp_user_id = None
        self.user_id = None
        self.mobile_number = None
        self.is_delete_user = None

    def get_valid_path(self):
        return ("/api/contact/v1/user/delete",)

    def get_rest_method(self):
        return "POST"
