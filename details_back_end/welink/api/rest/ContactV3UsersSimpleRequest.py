#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户基本信息
https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/bc1akx?type=third
@author: wecode@huawei.com
"""
from welink.api.rest.ContactV1UsersRequest import ContactV1UsersRequest


class ContactV3UsersSimpleRequest(ContactV1UsersRequest):
    """查询用户基本信息"""

    def __init__(self, url):
        super(ContactV3UsersSimpleRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v3/users/simple",)
        self.__rest_method = "POST"

    def get_valid_path(self):
        return self.__valid_path

    def get_rest_method(self):
        return "POST"
