#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
命名实体识别
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/g02ozz
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpNerRequest(RestApi):
    """命名实体识别"""

    def __init__(self, url):
        super(AiserviceV1NlpNerRequest, self).__init__(url)
        # 以下是接口的参数
        self.text = None
        self.lang = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/ner",)

    def get_rest_method(self):
        return "POST"
