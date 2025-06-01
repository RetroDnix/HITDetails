#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新班次
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/5zyueq
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase
from welink.api.bilingualism import Bilingualism


class AttendanceV1ScheduleSettingUpdateRequest(RestApi):
    """更新班次"""

    def __init__(self, url):
        super().__init__(url)
        self.schedule_id = None
        self.schedule_name = None
        self.punch_times = None
        self.is_next_day = None
        self.enable_arrive_late_leave_late = None
        self.flex_duration = None
        self.hasLunch_break = None
        self.punch_in_time = None
        self.punch_out_time = None
        self.punch_in_time2 = None
        self.latest_punch_time = None
        self.enable_leave_late_arrive_late = None
        self.leave_late_arrive_late_rule = None
        self.enable_early_toLeave_early = None
        self.punch_out_time2 = None
        self.punch_in_time3 = None
        self.punch_out_time3 = None
        self.lunch_break_start_time = None
        self.lunch_break_end_time = None
        self.is_next_lunch_break = None
        self.latest_next_day = None
        self.early_arrival_time = None
        self.due_hours = None
        self.total_work_time = None

    def get_valid_path(self):
        return ("/api/attendance/v1/schedule/setting/update",)

    def get_rest_method(self):
        return "PUT"
