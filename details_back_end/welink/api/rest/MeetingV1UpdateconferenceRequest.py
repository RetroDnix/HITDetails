#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修改预定会议
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/7motl4?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.rest.MeetingV1CreateconferenceRequest import (
    MeetingV1CreateconferenceRequest,
)


class MeetingV1UpdateconferenceRequest(MeetingV1CreateconferenceRequest):
    """修改预定会议"""

    def __init__(self, url):
        super(MeetingV1UpdateconferenceRequest, self).__init__(url)
        self.__rest_method = "PUT"
        self.__valid_path = ("/api/meeting/v1/updateconference",)
        self.__params = super(
            MeetingV1UpdateconferenceRequest, self
        ).get_params()
        self.__conference_id_key = "conferenceid"
        self.__unnull_keys = tuple(
            list(super(MeetingV1UpdateconferenceRequest, self).get_params())
            + [self.__conference_id_key]
        )

    @property
    def conferenceid(self):
        """会议标识"""
        return self.__params.get(self.__conference_id_key)

    @conferenceid.setter
    def conferenceid(self, value):
        self.__params[self.__conference_id_key] = str(value)

    @property
    def groupuri(self):
        """
软终端创建即时会议时在当前字段带临时群组ID，由服务器在邀请其他与会者时在或者conference-info头域中携带。长度限制为31个字符。
        """
        return self.body.groupuri

    @groupuri.setter
    def groupuri(self, value):
        self.body.groupuri = value

    @groupuri.deleter
    def groupuri(self):
        del self.body.groupuri

    def get_body_params(self):
        return self.body.get_data()

    def get_rest_method(self):
        return self.__rest_method

    def check_bodies(self):
        self.body.unnull_check()

    def get_valid_path(self):
        return self.__valid_path

    def get_params(self):
        self.__params.update(
            super(MeetingV1UpdateconferenceRequest, self).get_params()
        )
        return copy.deepcopy(self.__params)

    def get_unnull_keys(self):
        return self.__unnull_keys
