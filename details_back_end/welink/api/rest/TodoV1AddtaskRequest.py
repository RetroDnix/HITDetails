#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新增待办任务
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/2oeerl?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/2oeerl?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi
from welink.api.todoTasks import TodoTask


class TodoV1AddtaskRequest(RestApi):
    """新增待办任务"""

    def __init__(self, url):
        super(TodoV1AddtaskRequest, self).__init__(url)
        self.__rest_method = "POST"
        self.__body_params = TodoTask()
        self.__unnull_keys = (
            self.__body_params.task_id_key,
            self.__body_params.user_id_key,
            self.__body_params.details_url_key,
            self.__body_params.app_name_key,
            self.__body_params.applicant_user_id_key,
            self.__body_params.applicant_user_name_cn_key,
            self.__body_params.applicant_user_name_en_key,
        )
        self.__valid_path = ("/api/todo/v1/addtask",)

    @property
    def task_id(self):
        """
        string 必填 租户应用任务id
        """
        return self.__body_params.task_id

    @task_id.setter
    def task_id(self, value):
        self.__body_params.task_id = value

    @property
    def task_title(self):
        """
        string 非必填 审批任务标题
        """
        return self.__body_params.task_title

    @task_title.setter
    def task_title(self, value):
        self.__body_params.task_title = value

    @task_title.deleter
    def task_title(self):
        del self.__body_params.task_title

    @property
    def user_id(self):
        """
        string 必填 任务的当前处理人账号
        """
        return self.__body_params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__body_params.user_id = value

    @property
    def details_url(self):
        """
        string 必填 消息处理路径
        """
        return self.__body_params.details_url

    @details_url.setter
    def details_url(self, value):
        self.__body_params.details_url = value

    @property
    def app_name(self):
        """
        string 必填 应用名称
        """
        return self.__body_params.app_name

    @app_name.setter
    def app_name(self, value):
        self.__body_params.app_name = value

    @property
    def task_desc(self):
        """
        string 非必填 审批任务内容
        """
        return self.__body_params.task_desc

    @task_desc.setter
    def task_desc(self, value):
        self.__body_params.task_desc = value

    @task_desc.deleter
    def task_desc(self):
        del self.__body_params.task_desc

    @property
    def applicant_user_id(self):
        """
        string 必填 申请人id
        """
        return self.__body_params.applicant_user_id

    @applicant_user_id.setter
    def applicant_user_id(self, value):
        self.__body_params.applicant_user_id = value

    @applicant_user_id.deleter
    def applicant_user_id(self):
        del self.__body_params.applicant_user_id

    @property
    def applicant_user_name_cn(self):
        """
        string 非必填 申请人中文名称
        """
        return self.__body_params.applicant_user_name_cn

    @applicant_user_name_cn.setter
    def applicant_user_name_cn(self, value):
        self.__body_params.applicant_user_name_cn = value

    @applicant_user_name_cn.deleter
    def applicant_user_name_cn(self):
        del self.__body_params.applicant_user_name_cn

    @property
    def applicant_user_name_en(self):
        """
        string 非必填 申请人英文名称
        """
        return self.__body_params.applicant_user_name_en

    @applicant_user_name_en.setter
    def applicant_user_name_en(self, value):
        self.__body_params.applicant_user_name_en = value

    @applicant_user_name_en.deleter
    def applicant_user_name_en(self):
        del self.__body_params.applicant_user_name_en

    def get_body_params(self):
        return self.__body_params.get_data()

    def get_unnull_body_keys(self):
        return self.__unnull_keys

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path
