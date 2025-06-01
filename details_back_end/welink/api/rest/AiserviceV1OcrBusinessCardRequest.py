#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
名片识别
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/8hogls
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1OcrBusinessCardRequest(RestApi):
    """名片识别"""

    def __init__(self, url):
        super(AiserviceV1OcrBusinessCardRequest, self).__init__(url)
        # 以下是接口的参数
        self.image = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/ocr/business-card",)

    def get_rest_method(self):
        return "POST"
