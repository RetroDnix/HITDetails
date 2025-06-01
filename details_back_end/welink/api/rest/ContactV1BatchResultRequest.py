#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取异步任务结果
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/ml9ac5
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi


class ContactV1BatchResultRequest(RestApi):
    """获取异步任务结果"""

    def __init__(self, url):
        super().__init__(url)
        self.job_id = None

    def get_valid_path(self):
        return ("/api/contact/v1/batch/result",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
