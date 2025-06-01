#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文本摘要生成
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/lhrlh9
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1NlpSummarizationRequest(RestApi):
    """文本摘要生成"""

    def __init__(self, url):
        super(AiserviceV1NlpSummarizationRequest, self).__init__(url)
        # 以下是接口的参数
        self.lengthLimit = None
        self.title = None
        self.lang = None
        self.content = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/nlp/summarization",)

    def get_rest_method(self):
        return "POST"
