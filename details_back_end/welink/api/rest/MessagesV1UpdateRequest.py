#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修改消息状态
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/bzai2q
@author: wecode@huawei.com
"""

from welink.api import constants, utils
from welink.api.base import RestApi


class MessagesV1UpdateRequest(RestApi):
    """修改消息状态"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.item_id = None
        self.message_status = None
        self.staus_color = None
        self.public_acc_id = None

    def get_valid_path(self):
        return ("/api/messages/v1/update",)

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
