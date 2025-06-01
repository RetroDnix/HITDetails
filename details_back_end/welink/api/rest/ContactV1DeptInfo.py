#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通讯录部门基础信息
@author: wecode@huawei.com
"""
import json

from welink.api import utils


class SimpleDeptInfo(object):
    """部门信息"""

    def __init__(self):
        self.dept_code = None
        self.corp_dept_code = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class DeptInfo(object):
    """用户信息"""

    def __init__(self, url):
        self.parent_code = None
        self.corp_dept_code = None
        self.corp_parent_code = None
        self.dept_name_cn = None
        self.dept_name_en = None
        self.manager_id = None
        self.corp_manager_id = None
        self.visible_range = None
        self.create_dept_group = None
        self.group_contain_sub_dept = None
        self.dept_group_owner_id = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params
