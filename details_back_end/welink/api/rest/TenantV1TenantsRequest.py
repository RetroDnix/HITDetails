#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取企业详细信息
https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/ij1yns?type=third
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class TenantV1TenantsRequest(RestApi):
    """获取企业详细信息"""

    def __init__(self, url):
        super(TenantV1TenantsRequest, self).__init__(url)
        self.__rest_method = "GET"
        self.__valid_path = ("/api/tenant/v1/tenants",)

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
