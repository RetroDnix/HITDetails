#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
考勤打卡
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/hp7zrc?type=internal
@author: wecode@huawei.com
"""
import copy
import datetime

from welink.api import utils, exceptions, constants
from welink.api.base import RestApi


class AttendanceV2RecordsRequest(RestApi):
    """考勤打卡"""

    def __init__(self, url):
        super(AttendanceV2RecordsRequest, self).__init__(url)
        self.__body_params = super(
            AttendanceV2RecordsRequest, self
        ).get_body_params()
        self.__rest_mothod = "POST"

        self.__offset_key = "offset"
        self.__user_id_list_key = "userIdList"
        self.__date_from_key = "dateFrom"
        self.__date_to_key = "dateTo"
        self.__limit_key = "limit"
        self.__unnull_keys = (
            self.__offset_key,
            self.__date_from_key,
            self.__date_to_key,
            self.__limit_key,
        )
        self.__valid_path = ("/api/attendance/v2/records",)
        self.__date_time_format = "%Y-%m-%d %H:%M:%S"

    @property
    def offset(self):
        """
        int 必填 表示获取考勤数据的起始点，第一次传0，
            如果还有多余数据,下次获取传的1、2...依次递增
        """
        return self.__body_params.get(self.__offset_key, 0)

    @offset.setter
    def offset(self, value):
        value = utils.integer_check(value, self.__offset_key, "body")
        if value < 0:
            raise exceptions.ParameterException(
                "The value of %s must be a positive integer."
                % self.__offset_key
            )
        self.__body_params[self.__offset_key] = value

    @property
    def user_id_list(self):
        """
        list 非必填 此处userIdList指的是员工企业标识，
        员工企业标识需要在管理后台维护才可以查询，员工在企业内的员工工号列表，最多不能超过50个；
        如果没有维护员工企业标识，传递[]，即默认获取全员当天的考勤数据
        """
        return self.__body_params.get(self.__user_id_list_key, list())

    @user_id_list.setter
    def user_id_list(self, value):
        utils.type_check(value, list)
        user_list = [str(u) for u in value]
        utils.records_count_check(
            constants.MAX_USER_NUMBER_TO_QUERY_ATTENDANCE_RECORDS,
            len(user_list),
            "queried",
        )
        self.__body_params[self.__user_id_list_key] = user_list

    @user_id_list.deleter
    def user_id_list(self):
        if self.__user_id_list_key in self.__body_params:
            del self.__body_params[self.__user_id_list_key]

    @property
    def date_from(self):
        """string 必填 查询考勤打卡记录的起始工作日。"""
        return self.__body_params.get(self.__date_from_key, "")

    @date_from.setter
    def date_from(self, value):
        new_time = utils.datetime_format_check(
            str(value), self.__date_time_format, self.__date_from_key
        )
        if self.date_to:
            utils.time_span_check(
                new_time,
                datetime.datetime.strptime(
                    self.date_to, self.__date_time_format
                ),
                constants.MAX_INTERVAL_BETWEEN_START_AND_END_WORKDAYS,
            )
        self.__body_params[self.__date_from_key] = new_time.strftime(
            self.__date_time_format
        )

    @property
    def date_to(self):
        """
        string 必填 查询考勤打卡记录的结束工作日。
               注意，起始与结束工作日最多相隔24小时
        """
        return self.__body_params.get(self.__date_to_key, "")

    @date_to.setter
    def date_to(self, value):
        new_time = utils.datetime_format_check(
            str(value), self.__date_time_format, self.__date_to_key
        )
        if self.date_from:
            utils.time_span_check(
                datetime.datetime.strptime(
                    self.date_from, self.__date_time_format
                ),
                new_time,
                constants.MAX_INTERVAL_BETWEEN_START_AND_END_WORKDAYS,
            )
        self.__body_params[self.__date_to_key] = new_time.strftime(
            self.__date_time_format
        )

    @property
    def limit(self):
        """
        int 必填 表示获取考勤数据的条数，最大不能超过100条
        """
        return self.__body_params.get(self.__limit_key, 0)

    @limit.setter
    def limit(self, value):
        value = utils.integer_check(value, self.__limit_key, "body")
        utils.attribute_bounds_check(
            value,
            constants.MIN_ATTENDANCE_RECORDS_LIMIT,
            constants.MAX_ATTENDANCE_RECORDS_LIMIT,
            self.__class__.__name__,
            self.__limit_key,
        )
        self.__body_params[self.__limit_key] = value

    def get_body_params(self):
        return copy.deepcopy(self.__body_params)

    def get_rest_method(self):
        return self.__rest_mothod

    def get_valid_path(self):
        return self.__valid_path

    def get_unnull_body_keys(self):
        return self.__unnull_keys
