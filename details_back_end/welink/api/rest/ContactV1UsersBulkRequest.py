#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
异步批量同步用户
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/9meri5?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import ParametersList, RestApi
from welink.api.users import UserDetail


class ContactV1UsersBulkRequest(RestApi):
    """异步批量同步用户"""

    def __init__(self, url):
        super(ContactV1UsersBulkRequest, self).__init__(url)
        self.__body_params = super(
            ContactV1UsersBulkRequest, self
        ).get_body_params()
        self.__rest_method = "POST"
        self.__param_key = "personInfo"
        self.__param_list = ParametersList()
        self.__param_list.item_class_obj = UserDetail
        self.__param_list.max_records_count = 100
        self.__param_list.attr_name = self.__param_key
        self.__valid_path = ("/api/contact/v1/users/bulk",)

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path

    def get_param_key(self):
        """
        获取参数的关键字
        :return: string 参数关键字
        """
        return self.__param_key

    def get_body_params(self):
        self.__body_params[self.__param_key] = self.__param_list.get_data()
        return copy.deepcopy(self.__body_params)

    def get_unnull_body_keys(self):
        return (self.get_param_key(),)

    @property
    def person_info(self):
        """
        UserDetail 必填 用户详情对象
        """
        return self.__param_list.item_class_obj

    def get_param_list(self):
        """
        获取用户详情列表
        :return: list 用户详情列表
        """
        return self.__param_list.get_data()

    def get_param_by_index(self, index):
        """
        根据索引获取指定位置的用户详情
        :param index: int 索引
        :return: dict 指定索引位置的用户详情
        """
        return self.__param_list.get_param_by_index(index)

    def add_person_info(self, value):
        """
        在用户详情数组中添加元素
        :param value: UserDetail 需要添加的用户详情对象
        """
        self.__param_list.add_param(value)

    def set_person_info_by_index(self, value, index):
        """
        根据索引修改指定位置的用户详情
        :param value: UserDetail 需要修改的新的用户详情对象
        :param index: int 索引
        """
        self.__param_list.set_param_by_index(value, index)

    def del_person_info_by_index(self, index):
        """
        根据索引删除指定位置的用户详情
        :param index: int 索引
        """
        self.__param_list.del_param_by_index(index)
