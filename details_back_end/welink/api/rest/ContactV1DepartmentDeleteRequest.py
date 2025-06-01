#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除部门
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/lmhpw0
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi


class ContactV1DepartmentDeleteRequest(RestApi):
    """删除部门"""

    def __init__(self, url):
        super(ContactV1DepartmentDeleteRequest, self).__init__(url)
        self.dept_code = None
        self.corp_dept_code = None

    def get_valid_path(self):
        return ("/api/contact/v1/department/delete",)

    def get_rest_method(self):
        return "POST"
