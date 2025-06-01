#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通过免登授权码查询用户userId
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/p0n1j0?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/p0n1j0?type=third
@author: wecode@huawei.com
"""
import copy

from welink.api.base import RestApi


class AuthV2UseridRequest(RestApi):
    """通过免登授权码查询用户userId"""

    def __init__(self, url):
        super(AuthV2UseridRequest, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = super(AuthV2UseridRequest, self).get_params()
        self.__code_key = "code"
        self.__unnull_params = (self.__code_key,)
        self.__valid_path = ("/api/auth/v2/userid",)

    @property
    def code(self):
        """
        string 必填 免登授权码，获取方式参考We码小程序免登授权码或者H5轻应用免登授权码
        """
        return self.get_params().get(self.__code_key, "")

    @code.setter
    def code(self, value):
        self.__params[self.__code_key] = str(value)

    def get_params(self):
        return copy.deepcopy(self.__params)

    def get_unnull_keys(self):
        return self.__unnull_params

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
