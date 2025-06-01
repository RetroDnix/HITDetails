#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
公众号消息接口
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/dv3tx0
@author: wecode@huawei.com
"""

from welink.api import constants, utils
from welink.api.base import RestApi


class MessagesV1ImageRequest(RestApi):
    """图片消息"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.public_acc_id = None
        self.msg_range = None
        self.department_list = None
        self.role_list = None
        self.receive_device_type = None
        self.image_url = None
        self.jump_url = None

    def get_valid_path(self):
        return ("/api/messages/v1/image",)

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
