#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询会议信息
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/hvhl3n?type=internal
@author: wecode@huawei.com
"""

from welink.api.conference import ConferenceDetailQuery
from welink.api.base import RestApi


class MeetingV1QueryconferencedetailRequest(RestApi):
    def __init__(self, url):
        super(MeetingV1QueryconferencedetailRequest, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = ConferenceDetailQuery()
        self.__valid_path = ("/api/meeting/v1/queryconferencedetail",)

    @property
    def conferenceid(self):
        """会议标识"""
        return self.__params.conference_id

    @conferenceid.setter
    def conferenceid(self, value):
        self.__params.conference_id = value

    @property
    def page_index(self):
        """指定返回的与会者列表的页面索引。该值必须大于0，默认为1。"""
        return self.__params.page_index

    @page_index.setter
    def page_index(self, value):
        self.__params.page_index = value

    @page_index.deleter
    def page_index(self):
        del self.__params.page_index

    @property
    def page_size(self):
        """指定返回的与会者记录数，默认值由会议AS定义，内置会议和MediaX默认是20"""
        return self.__params.page_size

    @page_size.setter
    def page_size(self, value):
        self.__params.page_size = value

    @page_size.deleter
    def page_size(self):
        del self.__params.page_size

    @property
    def condition(self):
        """查询用来当做关键词的字符串，范围限定为1~128个字符。"""
        return self.__params.condition

    @condition.setter
    def condition(self, value):
        self.__params.condition = value
        return

    @condition.deleter
    def condition(self):
        del self.__params.condition

    @property
    def user_id(self):
        """用户帐号"""
        return self.__params.user_id

    @user_id.deleter
    def user_id(self):
        del self.__params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__params.user_id = value

    @property
    def type(self):
        """
        0：不区分终端和与会人。
        1：分页查询区分终端和与会人，结果合并返回。
        2：单独查询终端和与会人，结果单独返回。
        默认值为“0”。
        """
        return self.__params.type

    @type.deleter
    def type(self):
        del self.__params.type

    @type.setter
    def type(self, value):
        self.__params.type = value

    @property
    def query_type(self):
        """
        当“type”为“2”时，该字段有效。
        0：查询与会人。
        1：查询终端。
        默认值为“0”。
        """
        return self.__params.query_type

    @query_type.deleter
    def query_type(self):
        del self.__params.query_type

    @query_type.setter
    def query_type(self, value):
        self.__params.query_type = value

    def get_rest_method(self):
        return self.__rest_method

    def get_params(self):
        return self.__params.get_data()

    def get_valid_path(self):
        return self.__valid_path

    def check_headers(self):
        self.__params.unnull_check()
