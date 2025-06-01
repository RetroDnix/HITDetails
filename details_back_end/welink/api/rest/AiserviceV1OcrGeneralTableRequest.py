#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文档识字
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/gcgpy4
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class AiserviceV1OcrGeneralTableRequest(RestApi):
    """文档识字"""

    def __init__(self, url):
        super(AiserviceV1OcrGeneralTableRequest, self).__init__(url)
        # 以下是接口的参数
        self.image = None

    def get_valid_path(self):
        return ("/api/aiservice/v1/ocr/general-table",)

    def get_rest_method(self):
        return "POST"
