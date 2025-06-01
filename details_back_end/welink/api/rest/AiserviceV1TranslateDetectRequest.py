#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
语种检测
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/60g8ka
@author: wecode@huawei.com
"""
from welink.api.base import RestApi
from welink.api.exceptions import ParameterException


class Content(object):
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


class AiserviceV1TranslateDetectRequest(RestApi):
    """语种检测"""

    def __init__(self, url):
        super(AiserviceV1TranslateDetectRequest, self).__init__(url)
        # 以下是接口的参数
        self.__contents = []

    def get_valid_path(self):
        return ("/api/aiservice/v1/translate/detect",)

    def get_rest_method(self):
        return "POST"

    def contents(self):
        """待检测的文本列表"""
        return Content()

    def add_contents(self, content):
        """添加contents的元素"""
        if type(content) is not Content:
            raise (ParameterException("content type error"))
        self.__contents.append(content._get_data())

    def get_body_params(self):
        _body_params = {"contents": self.__contents}
        return _body_params
