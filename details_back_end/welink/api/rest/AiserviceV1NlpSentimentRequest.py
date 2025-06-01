#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
情感分析
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/6lqg0a
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpSentimentRequest(RestApi):
    """情感分析"""

    def __init__(self, url):
        super(AiserviceV1NlpSentimentRequest, self).__init__(url)
        # 以下是接口的参数
        self.text = None
        self.lang = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/sentiment",)

    def get_rest_method(self):
        return "POST"
