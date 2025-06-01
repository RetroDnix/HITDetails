#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询班次
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/xgjvsr
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase
from welink.api.bilingualism import Bilingualism


class AttendanceV1ScheduleSettingListRequest(RestApi):
    """查询班次"""

    def __init__(self, url):
        super().__init__(url)
        self.offset = None
        self.limit = None

    def get_valid_path(self):
        return ("/api/attendance/v1/schedule/list",)

    def get_rest_method(self):
        return "GET"
