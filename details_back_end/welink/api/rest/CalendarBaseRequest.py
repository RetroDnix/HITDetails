#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi


class Reminder(object):
    """提醒设置"""

    def __init__(self):
        self.minutes = None
        self.remind_type = None

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class Recurrence(object):
    """日历重复规则"""

    def __init__(self):
        self.frequency = None
        self.count = None
        self.until = None
        self.days = None
        self.interval = None
        self.monthdays = None
        self.months = None

    @property
    def days_string(self):
        return self.days

    @days_string.setter
    def days_string(self, value):
        self.days = json.loads(value)

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params


class CalendarBaseRequest(RestApi):
    def __init__(self, url):
        super(CalendarBaseRequest, self).__init__(url)
        self.content = None
        self.summary = None
        self.receiverUserList = None
        self.reminder = Reminder
        self.startTime = None
        self.endTime = None
        self.location = None
        self.recurrence = Recurrence

    def get_body_params(self):
        """
        获取请求实例中的消息体参数字典
        :return: dict 消息体参数字典
        """
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        if isinstance(self.recurrence, Recurrence):
            _body_params["recurrence"] = self.recurrence.get_data()
        else:
            del _body_params["recurrence"]
        if isinstance(self.reminder, Reminder):
            _body_params["reminder"] = self.reminder.get_data()
        else:
            del _body_params["reminder"]
        return _body_params
