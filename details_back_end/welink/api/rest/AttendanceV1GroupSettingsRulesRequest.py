#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
同步人员排班
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/1jnom9
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase
from welink.api.bilingualism import Bilingualism


class ShiftScheduleInfo(ObjectParamBase):
    def __init__(self):
        self.user_id = None
        self.group_id = None
        self.schedule_id = None
        self.punch_weekday = None


class AttendanceV1GroupSettingsRulesRequest(RestApi):
    """同步人员排班"""

    def __init__(self, url):
        super().__init__(url)
        self.shift_schedule_info = ShiftScheduleInfo
        self._shift_schedule_info = []

    def add_shift_schedule_info(self, shift_schedule_info):
        if type(shift_schedule_info) is not ShiftScheduleInfo:
            raise (ParameterException("schedule_info type error"))
        self._shift_schedule_info.append(shift_schedule_info.get_data())

    def get_valid_path(self):
        return ("/api/attendance/v1/group/settings/rules",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        _body_params.pop("shiftScheduleInfo", None)
        if self._shift_schedule_info:
            _body_params["shiftScheduleInfo"] = self._shift_schedule_info
        return _body_params
