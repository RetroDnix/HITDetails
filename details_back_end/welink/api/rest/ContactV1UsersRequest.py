#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户详情
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/b6yxfm?type=internal
@author: wecode@huawei.com
"""
from welink.api import exceptions
from welink.api.base import GetApiByUserInfo


class ContactV1UsersRequest(GetApiByUserInfo):
    """查询用户详情"""

    def __init__(self, url):
        super(ContactV1UsersRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v1/users",)

    def get_valid_path(self):
        return self.__valid_path

    def check_headers(self):
        valid_params = set(
            [
                pname
                for pname in self.get_params()
                if pname in self.get_valid_keys()
            ]
        )
        if not valid_params:
            raise exceptions.ParameterException(
                "The parameter is missing. "
                "You need to set only one of the "
                "userId, mobileNumber, and corpUserId parameters."
            )
        if len(valid_params) > 1:
            raise exceptions.ParameterException(
                "Too many parameters. You need to set only one of the "
                "userId, mobileNumber, and corpUserId parameters."
                "But now there are %s parameters: %s."
                % (len(valid_params), tuple(valid_params))
            )
