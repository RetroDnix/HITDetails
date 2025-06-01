#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
撤销（或完成）指定电子流
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/u25tct?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/u25tct?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi
from welink.api.todoTasks import TodoTask


class TodoV1DeltaskRequest(RestApi):
    """撤销（或完成）指定电子流"""

    def __init__(self, url):
        super(TodoV1DeltaskRequest, self).__init__(url)
        self.__rest_method = "DELETE"
        self.__params = TodoTask()
        self.__unnull_keys = (self.__params.task_id_key,)
        self.__valid_path = ("/api/todo/v1/deltask",)

    @property
    def task_id(self):
        """
        string 必填 租户应用任务id
        """
        return self.__params.task_id

    @task_id.setter
    def task_id(self, value):
        self.__params.task_id = value

    def get_params(self):
        return self.__params.get_data()

    def get_unnull_keys(self):
        return self.__unnull_keys

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
