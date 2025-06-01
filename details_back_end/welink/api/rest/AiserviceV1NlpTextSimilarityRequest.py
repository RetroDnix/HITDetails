#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文本相似度
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/fk98o1
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpTextSimilarityRequest(RestApi):
    """文本相似度"""

    def __init__(self, url):
        super(AiserviceV1NlpTextSimilarityRequest, self).__init__(url)
        # 以下是接口的参数
        self.text1 = None
        self.text2 = None
        self.lang = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/text-similarity",)

    def get_rest_method(self):
        return "POST"
