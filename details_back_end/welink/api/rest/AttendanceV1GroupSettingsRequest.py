#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
同步人员考勤组
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/laomcf
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase
from welink.api.bilingualism import Bilingualism


class GroupInfo(ObjectParamBase):
    def __init__(self):
        self.org_id = None
        self.org_type = None
        self.group_id = None


class AttendanceV1GroupSettingsRequest(RestApi):
    """获取打卡记录"""

    def __init__(self, url):
        super().__init__(url)
        self.group_info = GroupInfo
        self._group_info = []

    def add_group_info(self, group_info):
        if type(group_info) is not GroupInfo:
            raise (ParameterException("btn type error"))
        self._group_info.append(group_info.get_data())

    def get_valid_path(self):
        return ("/api/attendance/v1/group/settings",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        _body_params.pop("groupInfo", None)
        if self._group_info:
            _body_params["groupInfo"] = self._group_info
        return _body_params
