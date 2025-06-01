#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询子部门信息
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/0ncaat
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class ContactV3DepartmentsListRequest(RestApi):
    """查询子部门信息"""

    def __init__(self, url):
        super(ContactV3DepartmentsListRequest, self).__init__(url)
        self.dept_code = None
        self.recursiveflag = None
        self.offset = None
        self.limit = None

    def get_valid_path(self):
        return ("/api/contact/v3/departments/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
