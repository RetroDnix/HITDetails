#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
人脸比对
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/pelr6y
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV2FrsFaceCompareRequest(RestApi):
    """人脸比对"""

    def __init__(self, url):
        super(AiserviceV2FrsFaceCompareRequest, self).__init__(url)
        # 以下是接口的参数
        self.image1 = None
        self.image2 = None

    def get_valid_path(self):
        return ("/api/aiservice/v2/frs/face-compare",)

    def get_rest_method(self):
        return "POST"
