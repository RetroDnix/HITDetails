#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新部门
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/ystdt7
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV1DeptInfo import DeptInfo


class ContactV1DepartmentUpdateRequest(RestApi, DeptInfo):
    """更新部门"""

    def __init__(self, url):
        super(ContactV1DepartmentUpdateRequest, self).__init__(url)
        self.dept_code = None

    def get_valid_path(self):
        return ("/api/contact/v1/department/update",)

    def get_rest_method(self):
        return "POST"
