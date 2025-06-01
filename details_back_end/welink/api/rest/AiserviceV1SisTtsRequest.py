#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
语音合成
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/hv9f1x
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class Config(object):
    """语音合成"""

    def __init__(self):
        super(Config, self).__init__()
        self.audio_format = None
        self.property = None
        self.sample_rate = None
        self.speed = None
        self.pitch = None
        self.volume = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class AiserviceV1SisTtsRequest(RestApi):
    """文档识字"""

    def __init__(self, url):
        super(AiserviceV1SisTtsRequest, self).__init__(url)
        # 以下是接口的参数
        self.text = None
        self.config = Config

    def get_valid_path(self):
        return ("/api/aiservice/v1/sis/tts",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {"text": self.text, "config": self.config.get_data()}
        return _body_params
