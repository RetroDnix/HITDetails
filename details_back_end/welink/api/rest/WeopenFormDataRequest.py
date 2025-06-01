#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询表单填写数据
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/p3zlah
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class WeopenFormDataRequest(RestApi):
    """查询表单填写数据"""

    def __init__(self, url):
        super().__init__(url)
        self.form_id = None
        self.answer_date = None
        self.page = None
        self.page_size = None

    def get_valid_path(self):
        return ("/api/weopen/form/data",)

    def get_rest_method(self):
        return "POST"
