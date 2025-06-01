#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
意图理解
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/fxqpsr
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpSemanticParserRequest(RestApi):
    """意图理解"""

    def __init__(self, url):
        super(AiserviceV1NlpSemanticParserRequest, self).__init__(url)
        # 以下是接口的参数
        self.text = None
        self.lang = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/semantic-parser",)

    def get_rest_method(self):
        return "POST"
