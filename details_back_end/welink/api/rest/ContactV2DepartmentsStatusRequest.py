#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门异步同步结果
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/8w9qk3?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import ParametersList, RestApi
from welink.api.depts import CorpDeptCode


class ContactV2DepartmentsStatusRequest(RestApi):
    """查询部门异步同步结果"""

    def __init__(self, url):
        super(ContactV2DepartmentsStatusRequest, self).__init__(url)
        self.__body_params = super(
            ContactV2DepartmentsStatusRequest, self
        ).get_body_params()
        self.__rest_method = "POST"
        self.__param_key = "deptInfo"
        self.__param_list = ParametersList()
        self.__param_list.item_class_obj = CorpDeptCode
        self.__param_list.max_records_count = 10
        self.__param_list.attr_name = self.__param_key
        self.__valid_path = ("/api/contact/v2/departments/status",)

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path

    def get_param_key(self):
        """
        获取参数关键字
        :return: string 获取到的参数关键字
        """
        return self.__param_key

    def get_unnull_body_keys(self):
        return (self.get_param_key(),)

    def get_body_params(self):
        self.__body_params[self.__param_key] = self.__param_list.get_data()
        return copy.deepcopy(self.__body_params)

    @property
    def dept_info(self):
        """CorpDeptCode 必填 客户侧部门唯一编码对象"""
        return self.__param_list.item_class_obj

    def get_dept_info_list(self):
        """
        获取请求实例中客户侧部门唯一编码数组
        :return: list 客户侧部门唯一编码数组
        """
        return self.__param_list.get_data()

    def get_dept_info_by_index(self, index):
        """
        根据索引获取指定位置的客户侧部门唯一编码
        :param index: int 索引
        :return: dict 客户侧部门唯一编码字典
        """
        return self.__param_list.get_param_by_index(index)

    def add_dept_info(self, value):
        """
        在请求实例中添加新的客户侧部门唯一编码对象
        :param value: int 索引
        :return: CorpDeptCode 客户侧部门唯一编码对象
        """
        self.__param_list.add_param(value)

    def set_dept_info_by_index(self, value, index):
        """
        根据索引修改指定位置的客户侧部门唯一编码对象
        :param value: CorpDeptCode 需要修改的新的客户侧部门唯一编码对象
        :param index: int 索引
        """
        self.__param_list.set_param_by_index(value, index)

    def del_dept_info_by_index(self, index):
        """
        根据索引删除指定位置的客户侧部门唯一编码对象
        :param index: int 索引
        """
        self.__param_list.del_param_by_index(index)
