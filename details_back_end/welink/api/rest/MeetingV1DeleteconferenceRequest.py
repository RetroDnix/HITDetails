#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
取消预定会议
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/khz06k?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import RestApi


class MeetingV1DeleteconferenceRequest(RestApi):
    """取消预定会议"""

    def __init__(self, url):
        super(MeetingV1DeleteconferenceRequest, self).__init__(url)
        self.__params = super(
            MeetingV1DeleteconferenceRequest, self
        ).get_params()
        self.__rest_method = "DELETE"
        self.__valid_path = ("/api/meeting/v1/deleteconference",)
        self.__user_id_key = "userId"
        self.__conference_id_key = "conferenceid"
        self.__unnull_keys = (self.__user_id_key, self.__conference_id_key)

    @property
    def user_id(self):
        """用户帐号"""
        return self.__params.get(self.__user_id_key)

    @user_id.setter
    def user_id(self, value):
        self.__params[self.__user_id_key] = str(value)

    @property
    def conferenceid(self):
        """会议标识"""
        return self.__params.get(self.__conference_id_key)

    @conferenceid.setter
    def conferenceid(self, value):
        self.__params[self.__conference_id_key] = str(value)

    def get_params(self):
        return copy.deepcopy(self.__params)

    def get_rest_method(self):
        return self.__rest_method

    def get_unnull_keys(self):
        return self.__unnull_keys

    def get_valid_path(self):
        return self.__valid_path
