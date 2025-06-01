#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
人脸检测
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/kee8c0
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV2FrsFaceDetectRequest(RestApi):
    """人脸检测"""

    def __init__(self, url):
        super(AiserviceV2FrsFaceDetectRequest, self).__init__(url)
        # 以下是接口的参数
        self.image = None
        self.attributes = None

    def get_valid_path(self):
        return ("/api/aiservice/v2/frs/face-detect",)

    def get_rest_method(self):
        return "POST"
