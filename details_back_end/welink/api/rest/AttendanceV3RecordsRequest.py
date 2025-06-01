#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取打卡记录
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/r5dwyc
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class AttendanceV3RecordsRequest(RestApi):
    """获取打卡记录"""

    def __init__(self, url):
        super().__init__(url)
        self.offset = None
        self.user_id_list = None
        self.start_time = None
        self.end_time = None
        self.limit = None

    def get_valid_path(self):
        return ("/api/attendance/v3/records",)

    def get_rest_method(self):
        return "POST"
