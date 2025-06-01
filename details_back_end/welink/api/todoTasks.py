#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
待办任务参数模块
Create on 2020-03-09
@author wecode@huawei.com
"""
import copy


class TodoTask(object):
    """
    代办参数对象
    """

    def __init__(self):
        self.task_id_key = "taskId"
        self.task_title_key = "taskTitle"
        self.user_id_key = "userId"
        self.details_url_key = "detailsUrl"
        self.app_name_key = "appName"
        self.task_desc_key = "taskDesc"
        self.applicant_user_id_key = "applicantUserId"
        self.applicant_user_name_cn_key = "applicantUserNameCn"
        self.applicant_user_name_en_key = "applicantUserNameEn"
        self.__data = dict()
        self.__valid_keys = (
            self.task_id_key,
            self.task_title_key,
            self.user_id_key,
            self.details_url_key,
            self.app_name_key,
            self.task_desc_key,
            self.applicant_user_id_key,
            self.applicant_user_name_cn_key,
            self.applicant_user_name_en_key,
        )

    @property
    def task_id(self):
        """
        string 必填 租户应用任务id
        """
        return self.__data.get(self.task_id_key)

    @task_id.setter
    def task_id(self, value):
        self.__data[self.task_id_key] = str(value)

    @property
    def task_title(self):
        """
        string 非必填 审批任务标题
        """
        return self.__data.get(self.task_title_key)

    @task_title.setter
    def task_title(self, value):
        self.__data[self.task_title_key] = str(value)

    @task_title.deleter
    def task_title(self):
        if self.task_title_key in self.__data:
            del self.__data[self.task_title_key]

    @property
    def user_id(self):
        """
        string 必填 任务的当前处理人账号
        """
        return self.__data.get(self.user_id_key)

    @user_id.setter
    def user_id(self, value):
        self.__data[self.user_id_key] = str(value)

    @property
    def details_url(self):
        """
        string 必填 消息处理路径
        """
        return self.__data.get(self.details_url_key)

    @details_url.setter
    def details_url(self, value):
        self.__data[self.details_url_key] = str(value)

    @property
    def app_name(self):
        """
        string 必填 任务名称
        """
        return self.__data.get(self.app_name_key)

    @app_name.setter
    def app_name(self, value):
        self.__data[self.app_name_key] = str(value)

    @property
    def task_desc(self):
        """
        string 非必填 审批任务内容
        """
        return self.__data.get(self.task_desc_key)

    @task_desc.setter
    def task_desc(self, value):
        self.__data[self.task_desc_key] = str(value)

    @task_desc.deleter
    def task_desc(self):
        if self.task_desc_key in self.__data:
            del self.__data[self.task_desc_key]

    @property
    def applicant_user_id(self):
        """
        string 必填 申请人id
        """
        return self.__data.get(self.applicant_user_id_key)

    @applicant_user_id.setter
    def applicant_user_id(self, value):
        self.__data[self.applicant_user_id_key] = str(value)

    @applicant_user_id.deleter
    def applicant_user_id(self):
        if self.applicant_user_id_key in self.__data:
            del self.__data[self.applicant_user_id_key]

    @property
    def applicant_user_name_cn(self):
        """
        string 非必填 申请人中文名称
        """
        return self.__data.get(self.applicant_user_name_cn_key)

    @applicant_user_name_cn.setter
    def applicant_user_name_cn(self, value):
        self.__data[self.applicant_user_name_cn_key] = str(value)

    @applicant_user_name_cn.deleter
    def applicant_user_name_cn(self):
        if self.applicant_user_name_cn_key in self.__data:
            del self.__data[self.applicant_user_name_cn_key]

    @property
    def applicant_user_name_en(self):
        """
        string 非必填 申请人英文名称
        """
        return self.__data.get(self.applicant_user_name_en_key)

    @applicant_user_name_en.setter
    def applicant_user_name_en(self, value):
        self.__data[self.applicant_user_name_en_key] = str(value)

    @applicant_user_name_en.deleter
    def applicant_user_name_en(self):
        if self.applicant_user_name_en_key in self.__data:
            del self.__data[self.applicant_user_name_en_key]

    def get_data(self):
        """
        以dict形式获取待办任务参数实例的内容
        :return: dict 代办参数实例的内容
        """
        return copy.deepcopy(self.__data)
