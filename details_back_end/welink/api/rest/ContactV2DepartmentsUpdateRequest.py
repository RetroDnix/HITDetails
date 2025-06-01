#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
异步批量更新部门
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/wqgqo2?type=internal
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi


class DeptInfo(object):
    """部门信息"""

    def __init__(self):
        self.corp_dept_code = None
        self.corp_parent_code = None
        self.dept_name_cn = None
        self.dept_name_en = None
        self.manager_id = None
        self.order_no = None
        self.visible_range = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class ContactV2DepartmentsUpdateRequest(RestApi):
    """异步批量更新部门"""

    def __init__(self, url):
        super(ContactV2DepartmentsUpdateRequest, self).__init__(url)
        self.dept_info = DeptInfo
        self._dept_info_list = []

    def get_valid_path(self):
        return ("/api/contact/v2/departments/update",)

    def get_rest_method(self):
        return "PUT"

    def add_dept_info(self, value):
        self._dept_info_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"deptInfo": self._dept_info_list}
        return _body_params
