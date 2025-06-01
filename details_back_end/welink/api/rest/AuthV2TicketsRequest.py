#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取access_token
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/q76fsn?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/om8sc7?type=third
@author: wecode@huawei.com
"""
import copy

from welink.api.base import RestApi


class AuthV2TicketsRequest(RestApi):
    """获取access_token"""

    def __init__(self, url):
        super(AuthV2TicketsRequest, self).__init__(url)
        self.__client_id_key = "client_id"
        self.__client_secret_key = "client_secret"
        self.__tenant_id_key = "tenant_id"
        self.__unnull_body_keys = (
            self.__client_id_key,
            self.__client_secret_key,
        )
        self.__body_params = super(AuthV2TicketsRequest, self).get_body_params()
        self.__rest_method = "POST"
        self.__is_token_need = False
        self.__valid_path = ("/api/auth/v2/tickets",)

    @property
    def client_id(self):
        """
        string 必填 client_id 即 app_id，可在We码小程序开放平台中查看。
        """
        return self.get_body_params().get(self.__client_id_key)

    @client_id.setter
    def client_id(self, value):
        self.__body_params[self.__client_id_key] = str(value)

    @property
    def client_secret(self):
        """
        string 必填 client_secret 即 app_secret，可在We码小程序开放平台中查看。
        """
        return self.get_body_params().get(self.__client_secret_key)

    @client_secret.setter
    def client_secret(self, value):
        self.__body_params[self.__client_secret_key] = str(value)

    @property
    def tenant_id(self):
        """
string 非必填 目标租户的租户id, 可从应用授权或者通过免登授权码查询用户userId获取,不填表示获取自身租户的通行证
        """
        return self.get_body_params().get(self.__tenant_id_key)

    @tenant_id.setter
    def tenant_id(self, value):
        self.__body_params[self.__tenant_id_key] = str(value)

    @tenant_id.deleter
    def tenant_id(self):
        if self.__tenant_id_key in self.__body_params:
            del self.__body_params[self.__tenant_id_key]

    def check_token_need(self):
        return self.__is_token_need

    def get_body_params(self):
        return copy.deepcopy(self.__body_params)

    def get_unnull_body_keys(self):
        return self.__unnull_body_keys

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
