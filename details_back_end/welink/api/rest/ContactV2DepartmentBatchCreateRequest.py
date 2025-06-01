#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量创建部门
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/8hxds0
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV2DeptInfo import DeptInfo


class ContactV2DepartmentBatchCreateRequest(RestApi):
    """批量创建部门"""

    def __init__(self, url):
        super().__init__(url)
        self._dept_infos_list = []

    @staticmethod
    def dept_infos():
        return DeptInfo("")

    def get_valid_path(self):
        return ("/api/contact/v2/department/batch/create",)

    def get_rest_method(self):
        return "POST"

    def add_dept_infos(self, value):
        self._dept_infos_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"deptInfos": self._dept_infos_list}
        return _body_params
