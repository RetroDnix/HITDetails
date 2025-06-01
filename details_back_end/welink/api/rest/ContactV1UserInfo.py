#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通讯录用户基础信息
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi


class PersonInfos(object):
    """用户信息"""

    def __init__(self):
        self.user_id = None
        self.corp_user_id = None
        self.mobile_number = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class UserInfo(object):
    """用户信息"""

    def __init__(self, url):
        self.corp_user_id = None
        self.user_name_cn = None
        self.user_name_en = None
        self.sex = None
        self.mobile_number = None
        self.phone_number = None
        self.main_corp_dept_code = None
        self.main_dept_code = None
        self.corp_dept_codes = None
        self.dept_codes = None
        self.user_email = None
        self.employee_id = None
        self.landline_number = None
        self.business_address = None
        self.base_location = None
        self.position = None
        self.corp_secretary = None
        self.secretary = None
        self.remark = None
        self.senior_mode = None
        self.is_hide_phone_number = None
        self.is_notify = None
        self.person_type = None
        self.time_zone = None
        self.ext_attr = None
        self.role_ids = None
        self.email_login_account = None

    @property
    def ext_attr_string(self):
        return self.ext_attr

    @ext_attr_string.setter
    def ext_attr_string(self, value):
        self.ext_attr = json.loads(value)

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params
