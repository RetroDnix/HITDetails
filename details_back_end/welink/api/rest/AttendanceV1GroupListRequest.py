#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询考勤组
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/b53oxe
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class AttendanceV1GroupListRequest(RestApi):
    """查询考勤组"""

    def __init__(self, url):
        super().__init__(url)
        self.offset = None
        self.limit = None

    def get_valid_path(self):
        return ("/api/attendance/v1/group/list",)

    def get_rest_method(self):
        return "GET"
