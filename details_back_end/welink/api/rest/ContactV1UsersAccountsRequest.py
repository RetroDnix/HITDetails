#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户userId
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/5kuxyj?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/5kuxyj?type=third
@author: wecode@huawei.com
"""
import copy

from welink.api import constants, utils
from welink.api.base import RestApi


class ContactV1UsersAccountsRequest(RestApi):
    """查询用户userId"""

    def __init__(self, url):
        super(ContactV1UsersAccountsRequest, self).__init__(url)
        self.__rest_method = "POST"
        self.__body_params = super(
            ContactV1UsersAccountsRequest, self
        ).get_body_params()
        self.__corp_user_id_key = "corpUserId"
        self.__unnull_body_params = (self.__corp_user_id_key,)
        self.__valid_path = ("/api/contact/v1/users/accounts",)

    @property
    def corp_user_id(self):
        """
        list 必填 corpUserId列表（多个id用“,”分隔，最多支持50个一次）
        """
        return self.get_body_params().get(self.__corp_user_id_key, list())

    @corp_user_id.setter
    def corp_user_id(self, value):
        utils.type_check(value, list)
        new_corp_user_ids = [str(v) for v in value]
        records_count = len(new_corp_user_ids)
        utils.records_count_check(
            constants.MAX_USER_ID_RECORDS_COUNT,
            records_count,
            self.__corp_user_id_key,
        )
        self.__body_params[self.__corp_user_id_key] = new_corp_user_ids

    def get_rest_method(self):
        return self.__rest_method

    def get_body_params(self):
        return copy.deepcopy(self.__body_params)

    def get_unnull_body_keys(self):
        return self.__unnull_body_params

    def get_valid_path(self):
        return self.__valid_path
