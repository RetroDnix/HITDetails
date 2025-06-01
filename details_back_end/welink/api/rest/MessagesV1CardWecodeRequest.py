#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
应用卡片消息
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/vt2yoc
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/y7foaq
@author: wecode@huawei.com
"""

from welink.api import utils
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase


class Content(ObjectParamBase):
    def __init__(self):
        self.key = None
        self.value = None


class Btn(ObjectParamBase):
    def __init__(self):
        self.btn_title = None
        self.btn_url = None
        self.url_type = None


class MessagesV1CardWecodeRequest(RestApi):
    """应用卡片消息"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.public_acc_id = None
        self.msg_range = None
        self.department_list = None
        self.role_list = None
        self.receive_device_type = None
        self.message_status = None
        self.status_color = None
        self.msg_title = None
        self.url_type = None
        self.url_path = None
        self.btn_type = None
        self.is_force_tips = None
        self.content_list = Content
        self.btn_list = Btn
        self._btn = []
        self._content = []

    def add_btn(self, btn):
        if type(btn) is not Btn:
            raise (ParameterException("btn type error"))
        self._btn.append(btn.get_data())

    def add_content(self, content):
        if type(content) is not Content:
            raise (ParameterException("content type error"))
        self._content.append(content.get_data())

    def get_valid_path(self):
        return ("/api/messages/v1/card/wecode",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        _body_params.pop("contentList", None)
        _body_params.pop("btnList", None)
        if self._content:
            _body_params["contentList"] = self._content
        if self._btn:
            _body_params["btnList"] = self._btn
        if self.public_acc_id:
            _body_params.pop("public_acc_id", None)
            _body_params["publicAccID"] = self.public_acc_id
        return _body_params
