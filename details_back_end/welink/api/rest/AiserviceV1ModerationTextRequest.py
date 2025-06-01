#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文本内容审核
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/9ofubj
@author: wecode@huawei.com
"""
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException


class Items(object):
    """接口配置信息"""

    def __init__(self):
        self.text = None
        self.type = None

    def _get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class AiserviceV1ModerationTextRequest(RestApi):
    """文本内容审核"""

    def __init__(self, url):
        super(AiserviceV1ModerationTextRequest, self).__init__(url)
        # 以下是接口的参数
        self.categories = None
        self.__items = []

    def get_valid_path(self):
        return ("/api/aiservice/v1/moderation/text",)

    def get_rest_method(self):
        return "POST"

    def items(self):
        """待检测的文本列表"""
        return Items()

    def add_items(self, items):
        """添加items的元素"""
        if type(items) is not Items:
            raise (ParameterException("item type error"))
        self.__items.append(items._get_data())

    def get_body_params(self):
        _body_params = {"items": self.__items}
        if self.categories:
            _body_params["categories"] = self.categories
        return _body_params
