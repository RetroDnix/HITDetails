#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
句向量
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/papv5r
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpSentenceEmbeddingRequest(RestApi):
    """句向量"""

    def __init__(self, url):
        super(AiserviceV1NlpSentenceEmbeddingRequest, self).__init__(url)
        # 以下是接口的参数
        self.sentences = None
        self.domain = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/sentence-embedding",)

    def get_rest_method(self):
        return "POST"
