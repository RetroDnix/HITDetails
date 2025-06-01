#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门用户
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/lsaq2z
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi
from welink.api.rest.ContactV1UserInfo import UserInfo


class ContactV1UserSimplelistRequest(RestApi):
    """查询部门用户"""

    def __init__(self, url):
        super(ContactV1UserSimplelistRequest, self).__init__(url)
        self.dept_code = None
        self.corp_dept_code = None
        self.pageNo = None
        self.pageSize = None

    def get_valid_path(self):
        return ("/api/contact/v1/user/simplelist",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
