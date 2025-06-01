#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询父部门列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/3ze12j
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi


class ContactV2DepartmentParentRequest(RestApi):
    """查询父部门列表"""

    def __init__(self, url):
        super(ContactV2DepartmentParentRequest, self).__init__(url)
        self.corp_user_id = None
        self.user_id = None
        self.mobile_number = None
        self.corp_dept_code = None
        self.dept_code = None
        self.type = None

    def get_valid_path(self):
        return ("/api/contact/v2/department/parent",)

    def get_rest_method(self):
        return "POST"
