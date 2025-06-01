#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断用户是否为应用管理员
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/x0ikv2?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/1pl5r2?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WeopenV1IsadminRequest(RestApi):
    """判断用户是否为应用管理员"""

    def __init__(self, url):
        super(WeopenV1IsadminRequest, self).__init__(url)
        self.user_id = None

    def get_valid_path(self):
        return ("/api/weopen/v1/isadmin",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
