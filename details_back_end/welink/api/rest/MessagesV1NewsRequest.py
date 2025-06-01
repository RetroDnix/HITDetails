#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
公众号消息接口
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/igr53l
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism
from welink.api.exceptions import ParameterException
from welink.api.rest.ObjectParamBase import ObjectParamBase


class News(ObjectParamBase):
    """图文消息"""

    def __init__(self):
        self.title = None
        self.description = None
        self.url_type = None
        self.news_url = None
        self.image_url = None


class MessagesV1NewsRequest(RestApi):
    """图文消息"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.public_acc_id = None
        self.msg_range = None
        self.department_list = None
        self.role_list = None
        self.receive_device_type = None
        self.news = News
        self._news = []

    def get_valid_path(self):
        return ("/api/messages/v1/news",)

    def get_rest_method(self):
        return "POST"

    def add_news(self, news):
        if type(news) is not News:
            raise (ParameterException("news type error"))
        self._news.append(news.get_data())

    def get_body_params(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        if self.public_acc_id:
            _body_params.pop("public_acc_id", None)
            _body_params["publicAccID"] = self.public_acc_id
        _body_params.pop("news", None)
        if self._news:
            _body_params["news"] = self._news
        return _body_params
