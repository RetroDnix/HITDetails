#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新增事件日历
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/1zi863?type=internal
@author: wecode@huawei.com
"""
from welink.api.rest.CalendarBaseRequest import CalendarBaseRequest


class CalendarV1EventsAddRequest(CalendarBaseRequest):
    """新增事件日历"""

    def __init__(self, url):
        super(CalendarV1EventsAddRequest, self).__init__(url)

    def get_valid_path(self):
        return ("/api/calendar/v1/events/add",)

    def get_rest_method(self):
        return "POST"
