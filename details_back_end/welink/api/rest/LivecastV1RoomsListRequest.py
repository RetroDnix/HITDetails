#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取直播间列表
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/cw1seg
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class LivecastV1RoomsListRequest(RestApi):
    """获取直播间列表"""

    def __init__(self, url):
        super().__init__(url)
        self.limit = None
        self.offset = None
        self.subject = None
        self.start_time = None
        self.end_time = None

    def get_valid_path(self):
        return ("/api/livecast/v1/rooms/list",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
