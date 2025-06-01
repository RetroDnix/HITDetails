#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询健康打卡数据
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/l1on1u
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ApproveV1UserHealthRequest(RestApi):
    """查询健康打卡数据"""

    def __init__(self, url):
        super().__init__(url)
        self.user_id = None
        self.start_time = None
        self.end_time = None
        self.page_size = None
        self.page = None

    def get_valid_path(self):
        return ("/api/approve/v1/user/health",)

    def get_rest_method(self):
        return "POST"
