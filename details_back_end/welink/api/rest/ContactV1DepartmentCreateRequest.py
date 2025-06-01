#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建部门
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/fwi6e7
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV1DeptInfo import DeptInfo


class ContactV1DepartmentCreateRequest(RestApi, DeptInfo):
    """创建部门"""

    def __init__(self, url):
        super(ContactV1DepartmentCreateRequest, self).__init__(url)

    def get_valid_path(self):
        return ("/api/contact/v1/department/create",)

    def get_rest_method(self):
        return "POST"
