#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询历史会议列表
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/lw69lr?type=internal
@author: wecode@huawei.com
"""

from welink.api.conference import HistoryConferenceListQuery
from welink.api.base import RestApi


class MeetingV1QueryhistoryconferencesRequest(RestApi):
    """查询历史会议列表"""

    def __init__(self, url):
        super(MeetingV1QueryhistoryconferencesRequest, self).__init__(url)
        self.__params = HistoryConferenceListQuery()
        self.__rest_method = "GET"
        self.__valid_path = ("/api/meeting/v1/queryhistoryconferences",)

    @property
    def user_id(self):
        """
        待查询的会议预定者的帐号。
        仅管理员有权限查询权限范围内的所有账号；普通账号改字段无效，只能查询自己的。
        """
        return self.__params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__params.user_id = value

    @property
    def page_size(self):
        """
        待查询的会议预定者的uuid。
        指定返回的记录数。默认值由会议AS定义，默认是20，最大500条
        """
        return self.__params.page_size

    @page_size.setter
    def page_size(self, value):
        self.__params.page_size = value

    @property
    def page_index(self):
        """指定返回的页面索引。该值必须大于0，默认为1。"""
        return self.__params.page_index

    @page_index.setter
    def page_index(self, value):
        self.__params.page_index = value

    @property
    def query_all(self):
        """
指定是否查询企业下所有用户的会议记录。如果登录帐号不是企业管理员，则该字段无效。\
如果该字段为true，则userId字段无效。默认值为False。
        """
        return self.__params.query_all

    @query_all.setter
    def query_all(self, value):
        self.__params.query_all = value

    @property
    def condition(self):
        """查询用来当作关键词的字符串。长度限制为1~128个字符。"""
        return self.__params.condition

    @condition.deleter
    def condition(self):
        del self.__params.condition

    @condition.setter
    def condition(self, value):
        self.__params.condition = value

    @property
    def status(self):
        """
        0: 查询待召开的和已召开的
        1：查询待召开的
        2：查询已召开的
        """
        return self.__params.status

    @status.setter
    def status(self, value):
        self.__params.status = value

    @property
    def start_date(self):
        """查询的起始日期毫秒数"""
        return self.__params.start_date

    @start_date.setter
    def start_date(self, value):
        self.__params.start_date = value

    @start_date.deleter
    def start_date(self):
        del self.__params.start_date

    @property
    def end_date(self):
        """查询的截止日期毫秒数"""
        return self.__params.end_date

    @end_date.setter
    def end_date(self, value):
        self.__params.end_date = value

    @end_date.deleter
    def end_date(self):
        del self.__params.end_date

    @property
    def sort_type(self):
        """
        ASC_StartTIME：按会议开始时间升序排序（默认）
        DSC_StartTIME：按会议开始时间降序排序
        ASC_RecordTYPE：按会议是否有录播文件排序，之后默认按照会议开始时间升序排序
        DSC_RecordTYPE：按会议是否有录播文件排序，之后默认按照会议开始时间降序排序
        """
        return self.__params.sort_type

    @sort_type.deleter
    def sort_type(self):
        del self.__params.sort_type

    @sort_type.setter
    def sort_type(self, value):
        self.__params.sort_type = value

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path

    def get_params(self):
        return self.__params.get_data()

    def check_headers(self):
        self.__params.unnull_check()
