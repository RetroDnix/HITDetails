#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
语音评测
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/ix70sg
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class Config(object):
    """接口配置信息"""

    def __init__(self):
        super(Config, self).__init__()
        self.audio_format = None
        self.language = None
        self.mode = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class AiserviceV1SisAudioAssessmentRequest(RestApi):
    """语音评测"""

    def __init__(self, url):
        super(AiserviceV1SisAudioAssessmentRequest, self).__init__(url)
        # 以下是接口的参数
        self.audio_data = None
        self.ref_text = None
        self.config = Config

    def get_valid_path(self):
        return ("/api/aiservice/v1/sis/audio-assessment",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = {}
        if self.audio_data:
            _body_params["audioData"] = self.audio_data
        if self.ref_text:
            _body_params["refText"] = self.ref_text
        if isinstance(self.config, Config):
            _body_params["config"] = self.config.get_data()
        return _body_params
