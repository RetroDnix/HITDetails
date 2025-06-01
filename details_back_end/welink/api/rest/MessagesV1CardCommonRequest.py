#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
公众号消息接口
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/a9f9qn
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/u2dqx7
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class MessagesV1CardCommonRequest(RestApi):
    """公众号消息接口"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.msg_title = None
        self.msg_content = None
        self.url_type = None
        self.url_path = None
        self.msg_display_mode = None
        self.desktop_url_path = None
        self.is_force_tips = None

    def get_valid_path(self):
        return ("/api/messages/v1/card/common",)

    def get_rest_method(self):
        return "POST"
