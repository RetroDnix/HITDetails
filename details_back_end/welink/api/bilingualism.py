#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
双语参数模块
Create on 2020-03-09
@author wecode@huawei.com
"""
import copy


class Bilingualism(object):
    """
    双语参数对象
    """

    def __init__(self):
        self.__cn_key = "CN"
        self.__en_key = "EN"
        self.__data = {self.__cn_key: "", self.__en_key: ""}

    @property
    def cn(self):
        """
        string 可选 中文参数
        """
        return self.__data.get(self.__cn_key, "")

    @cn.setter
    def cn(self, value):
        self.__data[self.__cn_key] = str(value)

    @property
    def en(self):
        """
        string 可选 英文参数
        """
        return self.__data.get(self.__en_key, "")

    @en.setter
    def en(self, value):
        self.__data[self.__en_key] = str(value)

    def get_cn_key(self):
        """
        获取中文参数字段名
        :return: string 中文参数字段名
        """
        return self.__cn_key

    def get_en_key(self):
        """
        获取英文参数字段名
        :return: string 英文参数字段名
        """
        return self.__en_key

    def get_data(self):
        """
        以dict形式获取参数内容
        :return: dict 参数内容
        """
        return copy.deepcopy(self.__data)
