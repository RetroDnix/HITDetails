#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户表单列表
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/4wvh1t
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class WeopenFormListRequest(RestApi):
    """查询用户表单列表"""

    def __init__(self, url):
        super().__init__(url)
        self.page = None
        self.page_size = None
        self.user_id = None
        self.keyword = None
        self.form_status = None

    def get_valid_path(self):
        return ("/api/weopen/form/list",)

    def get_rest_method(self):
        return "POST"
