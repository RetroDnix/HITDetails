#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新增会议日历
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/apzfbf?type=internal
@author: wecode@huawei.com
"""
from welink.api.rest.CalendarBaseRequest import CalendarBaseRequest


class CalendarV1MeetingsAddRequest(CalendarBaseRequest):
    """新增会议日历"""

    def __init__(self, url):
        super(CalendarV1MeetingsAddRequest, self).__init__(url)
        self.creatorUserId = None

    def get_valid_path(self):
        return ("/api/calendar/v1/meetings/add",)

    def get_rest_method(self):
        return "POST"
