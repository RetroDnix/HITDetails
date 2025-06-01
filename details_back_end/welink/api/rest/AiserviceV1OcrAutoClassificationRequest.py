#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
票证识别
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/3rwip3
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1OcrAutoClassificationRequest(RestApi):
    """票证识别"""

    def __init__(self, url):
        super(AiserviceV1OcrAutoClassificationRequest, self).__init__(url)
        # 以下是接口的参数
        self.image = None
        self.side = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/ocr/auto-classification",)

    def get_rest_method(self):
        return "POST"
