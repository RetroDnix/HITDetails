#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
语音识别
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/oli98v
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class Config(object):
    """接口配置信息"""

    def __init__(self):
        super(Config, self).__init__()
        self.audio_format = None
        self.property = None
        self.add_punc = None
        self.vocabulary_id = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class AiserviceV1SisShortAudioRequest(RestApi):
    """语音识别"""

    def __init__(self, url):
        super(AiserviceV1SisShortAudioRequest, self).__init__(url)
        # 以下是接口的参数
        self.data = None
        self.config = Config

    def get_valid_path(self):
        return ("/api/aiservice/v1/sis/short-audio",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {"data": self.data, "config": self.config.get_data()}
        return _body_params
