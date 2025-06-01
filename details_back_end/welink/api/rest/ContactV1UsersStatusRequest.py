#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询人员信息同步结果
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/0pj1sw?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import ParametersList, RestApi
from welink.api.users import UserInfo


class ContactV1UsersStatusRequest(RestApi):
    """查询人员信息同步结果"""

    def __init__(self, url):
        super(ContactV1UsersStatusRequest, self).__init__(url)
        self.__rest_method = "POST"
        self.__body_params = super(
            ContactV1UsersStatusRequest, self
        ).get_body_params()
        self.__param_key = "personInfo"
        self.__param_list = ParametersList()
        self.__param_list.item_class_obj = UserInfo
        self.__param_list.max_records_count = 10
        self.__param_list.attr_name = self.__param_key
        self.__valid_path = ("/api/contact/v1/users/status",)

    def get_rest_method(self):
        return self.__rest_method

    def get_param_key(self):
        """
        获取参数关键字
        :return: string 参数关键字
        """
        return self.__param_key

    def get_valid_path(self):
        return self.__valid_path

    def get_unnull_body_keys(self):
        return (self.get_param_key(),)  # 返回元组，逗号勿删

    def get_body_params(self):
        self.__body_params[self.__param_key] = self.__param_list.get_data()
        return copy.deepcopy(self.__body_params)

    @property
    def person_info(self):
        """
        UserInfo 用户简单信息对象
        """
        return self.__param_list.item_class_obj

    def get_person_info_list(self):
        """
        获取用户简单信息数组
        :return: list 用户简单信息数组
        """
        return self.__param_list.get_data()

    def get_person_info_by_index(self, index):
        """
        根据索引获取指定位置的用户简单信息
        :param index: int 索引
        :return: dict 用户简单信息
        """
        return self.__param_list.get_param_by_index(index)

    def add_person_info(self, value):
        """
        在数组参数中添加用户简单信息对象
        :param value: UserInfo 需要添加的用户简单信息对象
        """
        self.__param_list.add_param(value)

    def set_person_info_by_index(self, value, index):
        """
        根据索引修改指定位置的用户简单信息对象
        :param value: UserInfo 需要修改的新的用户简单信息对象
        :param index: int 索引
        """
        self.__param_list.set_param_by_index(value, index)

    def del_person_info_by_index(self, index):
        """
        根据索引删除指定位置的用户简单信息对象
        :param index: int 索引
        """
        self.__param_list.del_param_by_index(index)
