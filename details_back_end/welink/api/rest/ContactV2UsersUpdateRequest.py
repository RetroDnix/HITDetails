#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
异步批量更新用户
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/qdwqrf?type=internal
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi


class PersonInfo(object):
    """用户信息"""

    def __init__(self):
        self.corp_user_id = None
        self.user_name_cn = None
        self.user_name_en = None
        self.sex = None
        self.main_corp_dept = None
        self.corp_dept_code = None
        self.order_in_depts = None
        self.user_email = None
        self.employee_id = None
        self.landline_number = None
        self.address = None
        self.position = None
        self.is_open_account = None
        self.corp_secretary = None
        self.remark = None
        self.isHide_mobile_number = None
        self.is_notify = None
        self.ext_attr = None

    @property
    def order_in_depts_string(self):
        return self.order_in_depts

    @order_in_depts_string.setter
    def order_in_depts_string(self, value):
        self.order_in_depts = json.loads(value)

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params

    @property
    def ext_attr_string(self):
        return self.ext_attr

    @ext_attr_string.setter
    def ext_attr_string(self, value):
        self.ext_attr = json.loads(value)


class ContactV2UsersUpdateRequest(RestApi):
    """异步批量更新用户"""

    def __init__(self, url):
        super(ContactV2UsersUpdateRequest, self).__init__(url)
        self.person_info = PersonInfo
        self._person_info_list = []

    def get_valid_path(self):
        return ("/api/contact/v2/users/update",)

    def get_rest_method(self):
        return "PUT"

    def add_person_info(self, value):
        self._person_info_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"personInfo": self._person_info_list}
        return _body_params
