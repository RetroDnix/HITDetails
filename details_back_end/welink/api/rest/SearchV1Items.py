#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
搜索服务-搜索基础信息
@author: wecode@huawei.com
"""
import json

from welink.api import utils


class Items(object):
    """搜索基础信息"""

    def __init__(self):
        self.item_id = None
        self.data_type_en = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class SearchV1Items(object):
    """搜索基础信息"""

    def __init__(self):
        self.item_id = None
        self.data_type_en = None
        self.data_type = None
        self.title = None
        self.content = None
        self.author = None
        self.keywords = None
        self.createTime = None
        self.updateTime = None
        self.url = None
        self.icon = None
        self.ext_field1 = None
        self.ext_field2 = None
        self.ext_field3 = None
        self.ext_field4 = None
        self.ext_field5 = None
        self.ext_field6 = None
        self.ext_field7 = None
        self.ext_field8 = None
        self.ext_field9 = None
        self.ext_field10 = None
        self.ext_field11 = None
        self.ext_field12 = None
        self.ext_field13 = None
        self.ext_field14 = None
        self.ext_field15 = None

    @property
    def ext_field1_string(self):
        return self.ext_field1

    @ext_field1_string.setter
    def ext_field1_string(self, value):
        self.ext_field1 = json.loads(value)

    @property
    def ext_field2_string(self):
        return self.ext_field2

    @ext_field2_string.setter
    def ext_field2_string(self, value):
        self.ext_field2 = json.loads(value)

    @property
    def ext_field3_string(self):
        return self.ext_field3

    @ext_field3_string.setter
    def ext_field3_string(self, value):
        self.ext_field3 = json.loads(value)

    @property
    def ext_field4_string(self):
        return self.ext_field4

    @ext_field4_string.setter
    def ext_field4_string(self, value):
        self.ext_field4 = json.loads(value)

    @property
    def ext_field5_string(self):
        return self.ext_field5

    @ext_field5_string.setter
    def ext_field5_string(self, value):
        self.ext_field5 = json.loads(value)

    @property
    def ext_field6_string(self):
        return self.ext_field6

    @ext_field6_string.setter
    def ext_field6_string(self, value):
        self.ext_field6 = json.loads(value)

    @property
    def ext_field7_string(self):
        return self.ext_field7

    @ext_field7_string.setter
    def ext_field7_string(self, value):
        self.ext_field7 = json.loads(value)

    @property
    def ext_field8_string(self):
        return self.ext_field8

    @ext_field8_string.setter
    def ext_field8_string(self, value):
        self.ext_field8 = json.loads(value)

    @property
    def ext_field9_string(self):
        return self.ext_field9

    @ext_field9_string.setter
    def ext_field9_string(self, value):
        self.ext_field9 = json.loads(value)

    @property
    def ext_field10_string(self):
        return self.ext_field10

    @ext_field10_string.setter
    def ext_field10_string(self, value):
        self.ext_field10 = json.loads(value)

    @property
    def ext_field11_string(self):
        return self.ext_field11

    @ext_field11_string.setter
    def ext_field11_string(self, value):
        self.ext_field11 = json.loads(value)

    @property
    def ext_field12_string(self):
        return self.ext_field12

    @ext_field12_string.setter
    def ext_field12_string(self, value):
        self.ext_field12 = json.loads(value)

    @property
    def ext_field13_string(self):
        return self.ext_field13

    @ext_field13_string.setter
    def ext_field13_string(self, value):
        self.ext_field13 = json.loads(value)

    @property
    def ext_field14_string(self):
        return self.ext_field14

    @ext_field14_string.setter
    def ext_field14_string(self, value):
        self.ext_field14 = json.loads(value)

    @property
    def ext_field15_string(self):
        return self.ext_field15

    @ext_field15_string.setter
    def ext_field15_string(self, value):
        self.ext_field15 = json.loads(value)

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params
