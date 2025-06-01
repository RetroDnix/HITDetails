#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取已支持的翻译语种
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/adnowe
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1TranslateSupportedRequest(RestApi):
    """获取已支持的翻译语种"""

    def __init__(self, url):
        super(AiserviceV1TranslateSupportedRequest, self).__init__(url)
        # 以下是接口的参数
        self.target_language = None
        self.source_texts = None
        self.source_language = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/translate/supported",)

    def get_rest_method(self):
        return "GET"
