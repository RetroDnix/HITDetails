#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新会议日历
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/gxempg?type=internal
@author: wecode@huawei.com
"""
from welink.api.rest.CalendarBaseRequest import CalendarBaseRequest


class CalendarV1MeetingsUpdateRequest(CalendarBaseRequest):
    """更新会议日历"""

    def __init__(self, url):
        super(CalendarV1MeetingsUpdateRequest, self).__init__(url)
        self.cal_uid = None
        self.creatorUserId = None

    def get_valid_path(self):
        return ("/api/calendar/v1/meetings/update",)

    def get_rest_method(self):
        return "PUT"
