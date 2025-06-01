#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除班次
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/e3m4l9
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AttendanceV1ScheduleSettingDeleteRequest(RestApi):
    """删除班次"""

    def __init__(self, url):
        super().__init__(url)
        self.schedule_id = None

    def get_valid_path(self):
        return ("/api/attendance/v1/schedule/setting/delete",)

    def get_rest_method(self):
        return "DELETE"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
