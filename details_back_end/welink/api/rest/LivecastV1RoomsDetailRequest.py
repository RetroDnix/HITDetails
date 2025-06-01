#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取直播间详情
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/ysjv3c
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class LivecastV1RoomsDetailRequest(RestApi):
    """获取直播间详情"""

    def __init__(self, url):
        super().__init__(url)
        self.room_id = None

    def get_valid_path(self):
        return ("/api/livecast/v1/rooms/detail",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
