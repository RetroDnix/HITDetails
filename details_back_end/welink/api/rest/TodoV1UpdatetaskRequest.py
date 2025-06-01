#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
结束指定电子流的指定用户的待办
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/5zqq4f?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/5zqq4f?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi
from welink.api.todoTasks import TodoTask


class TodoV1UpdatetaskRequest(RestApi):
    """结束指定电子流的指定用户的待办"""

    def __init__(self, url):
        super(TodoV1UpdatetaskRequest, self).__init__(url)
        self.__rest_method = "PUT"
        self.__params = TodoTask()
        self.__unnull_keys = (
            self.__params.task_id_key,
            self.__params.user_id_key,
        )
        self.__valid_path = ("/api/todo/v1/updatetask",)

    @property
    def task_id(self):
        """
        string 必填 租户应用任务id
        """
        return self.__params.task_id

    @task_id.setter
    def task_id(self, value):
        self.__params.task_id = value

    @property
    def user_id(self):
        """
        string 必填 任务的当前处理人账号
        """
        return self.__params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__params.user_id = value

    def get_params(self):
        return self.__params.get_data()

    def get_unnull_keys(self):
        return self.__unnull_keys

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
