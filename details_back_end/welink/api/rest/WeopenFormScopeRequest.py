#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询表单填写数据
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/p3zlah
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism
from welink.api.rest.ObjectParamBase import ObjectParamBase


class Scopes(ObjectParamBase):
    def __init__(self):
        super().__init__()
        self.users = None
        self.depts = None


class FillScope(ObjectParamBase):
    def __init__(self):
        self.scope_type = None
        self.scopes = None

    @staticmethod
    def scopes():
        return Scopes()

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        if self.scopes:
            _body_params["scopes"] = self.scopes.get_data()
        else:
            _body_params.pop("scopes", None)
        return _body_params


class WeopenFormScopeRequest(RestApi):
    """查询表单填写数据"""

    def __init__(self, url):
        super().__init__(url)
        self.form_id = None
        self.fill_scope = FillScope

    @staticmethod
    def fill_scope():
        return WeopenFormScopeRequest("").fill_scope()

    def get_valid_path(self):
        return ("/api/weopen/form/scope",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        _body_params["formId"] = self.form_id
        if isinstance(self.fill_scope, FillScope):
            _body_params["fillScope"] = self.fill_scope.get_data()
        return _body_params
