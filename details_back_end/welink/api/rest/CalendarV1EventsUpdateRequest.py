#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新事件日历
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/xx5731?type=internal
@author: wecode@huawei.com
"""
from welink.api.rest.CalendarBaseRequest import CalendarBaseRequest


class CalendarV1EventsUpdateRequest(CalendarBaseRequest):
    """更新事件日历"""

    def __init__(self, url):
        super(CalendarV1EventsUpdateRequest, self).__init__(url)
        self.cal_uid = None

    def get_valid_path(self):
        return ("/api/calendar/v1/events/update",)

    def get_rest_method(self):
        return "PUT"
