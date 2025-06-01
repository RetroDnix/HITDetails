#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建用户
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/f4piho
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi
from welink.api.rest.ContactV1UserInfo import UserInfo


class ContactV1UserCreateRequest(RestApi, UserInfo):
    """创建用户"""

    def __init__(self, url):
        super().__init__(url)

    def get_valid_path(self):
        return ("/api/contact/v1/user/create",)

    def get_rest_method(self):
        return "POST"
