#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文本分词
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/13anlx
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpSegmentRequest(RestApi):
    """文本分词"""

    def __init__(self, url):
        super(AiserviceV1NlpSegmentRequest, self).__init__(url)
        # 以下是接口的参数
        self.text = None
        self.pos_switch = None
        self.lang = None
        self.criterion = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/segment",)

    def get_rest_method(self):
        return "POST"
