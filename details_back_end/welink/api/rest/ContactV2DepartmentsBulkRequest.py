#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
异步批量同步部门
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/zgn4mp?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import ParametersList, RestApi
from welink.api.depts import DeptDetail


class ContactV2DepartmentsBulkRequest(RestApi):
    """异步批量同步部门"""

    def __init__(self, url):
        super(ContactV2DepartmentsBulkRequest, self).__init__(url)
        self.__body_params = super(
            ContactV2DepartmentsBulkRequest, self
        ).get_body_params()
        self.__rest_method = "POST"
        self.__param_key = "deptInfo"
        self.__param_list = ParametersList()
        self.__param_list.item_class_obj = DeptDetail
        self.__param_list.max_records_count = 100
        self.__param_list.attr_name = self.__param_key
        self.__valid_path = ("/api/contact/v2/departments/bulk",)

    def get_rest_method(self):
        return self.__rest_method

    def get_valid_path(self):
        return self.__valid_path

    def get_unnull_body_keys(self):
        return (self.get_param_key(),)

    def get_param_key(self):
        """
        获取参数关键字
        """
        return self.__param_key

    def get_body_params(self):
        self.__body_params[self.__param_key] = self.__param_list.get_data()
        return copy.deepcopy(self.__body_params)

    @property
    def dept_info(self):
        """
        DeptDetail 部门详情对象
        """
        return self.__param_list.item_class_obj

    def get_dept_info_by_index(self, index):
        """
        根据索引获取指定位置的部门信息
        :param index: int 索引
        :return: dict 获取到的部门信息
        """
        return self.__param_list.get_param_by_index(index)

    def get_dept_info_list(self):
        """
        获取请求实例中的部门信息数组
        :return: list 部门信息数组
        """
        return self.__param_list.get_data()

    def set_dept_info_by_index(self, value, index):
        """
        根据索引修改指定位置的部门详情
        :param value: DeptDetail 需要修改的新的部门详情对象
        :param index: int 索引
        """
        self.__param_list.set_param_by_index(value, index)

    def add_dept_info(self, value):
        """
        在请求实例中添加新的部门信息
        :param value: DeptDetail 需要添加的新的部门详情对象
        """
        self.__param_list.add_param(value)

    def del_dept_info_by_index(self, index):
        """
        根据索引删除指定位置的部门详情对象
        :param index: int 索引
        """
        self.__param_list.del_param_by_index(index)
