#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
普通卡片消息
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/a9f9qn
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/u2dqx7
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class MessagesV2CardCommonRequest(RestApi):
    """普通卡片消息"""

    def __init__(self, url):
        super().__init__(url)
        self.msg_owner = None
        self.public_acc_id = None
        self.msg_range = None
        self.department_list = None
        self.role_list = None
        self.to_user_list = None
        self.msg_title = None
        self.msg_content = None
        self.receive_device_type = None
        self.url_type = None
        self.url_path = None
        self.desktop_url_path = None
        self.message_status = None
        self.status_color = None
        self.is_force_tips = None

    def get_valid_path(self):
        return ("/api/messages/v2/card/common",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        if self.public_acc_id:
            _body_params.pop("public_acc_id", None)
            _body_params["publicAccID"] = self.public_acc_id
        return _body_params
