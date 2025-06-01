#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
消息撤回
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/r8h62a
@author: wecode@huawei.com
"""

from welink.api import constants, utils
from welink.api.base import RestApi


class MessagesV1RecallRequest(RestApi):
    """消息撤回"""

    def __init__(self, url):
        super().__init__(url)
        self.item_id = None

    def get_valid_path(self):
        return ("/api/messages/v1/recall",)

    def get_rest_method(self):
        return "POST"
