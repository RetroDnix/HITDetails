#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图片审核
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/210hl6
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1ModerationImageRequest(RestApi):
    """图片审核"""

    def __init__(self, url):
        super(AiserviceV1ModerationImageRequest, self).__init__(url)
        # 以下是接口的参数
        self.image = None
        self.threshold = None
        self.categories = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/moderation/image",)

    def get_rest_method(self):
        return "POST"
