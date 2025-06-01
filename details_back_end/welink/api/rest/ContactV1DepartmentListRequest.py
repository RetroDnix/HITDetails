#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/i50ow9
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi


class ContactV1DepartmentListRequest(RestApi):
    """查询部门列表"""

    def __init__(self, url):
        super(ContactV1DepartmentListRequest, self).__init__(url)
        self.dept_code = None
        self.corp_dept_code = None
        self.recursiveflag = None
        self.pageNo = None
        self.pageSize = None

    def get_valid_path(self):
        return ("/api/contact/v1/department/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
