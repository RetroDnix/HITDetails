#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文本翻译
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/gproyi
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1TranslateTranslateRequest(RestApi):
    """文本翻译"""

    def __init__(self, url):
        super(AiserviceV1TranslateTranslateRequest, self).__init__(url)
        # 以下是接口的参数
        self.target_language = None
        self.source_texts = None
        self.source_language = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/translate/translate",)

    def get_rest_method(self):
        return "POST"
