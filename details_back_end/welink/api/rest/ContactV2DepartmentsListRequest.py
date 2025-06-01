#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询子部门信息
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/0ncaat?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/0ncaat?type=third
@author: wecode@huawei.com
"""
import copy

from welink.api import constants, utils
from welink.api.base import RestApi


class ContactV2DepartmentsListRequest(RestApi):
    """查询子部门信息"""

    def __init__(self, url):
        super(ContactV2DepartmentsListRequest, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = super(
            ContactV2DepartmentsListRequest, self
        ).get_params()
        self.__dept_code_key = "deptCode"
        self.__recursive_flag_key = "recursiveflag"
        self.__offset_key = "offset"
        self.__limit_key = "limit"
        self.__unnull_keys = (
            self.__dept_code_key,
            self.__recursive_flag_key,
            self.__offset_key,
            self.__limit_key,
        )
        self.__valid_path = ("/api/contact/v2/departments/list",)

    @property
    def dept_code(self):
        """
        string 必填 部门编码，示例：0
        """
        return self.__params.get(self.__dept_code_key, "")

    @dept_code.setter
    def dept_code(self, value):
        self.__params[self.__dept_code_key] = str(value)

    @property
    def recursiveflag(self):
        """
        string 必填 0 ：查询下级部门信息 1 ：查询递归获取所有子部门
        """
        return self.__params.get(self.__recursive_flag_key, "")

    @recursiveflag.setter
    def recursiveflag(self, value):
        value = str(value)
        utils.attribute_valid_check(
            constants.RECURSIVE_FLAG_LIST,
            value,
            self.__recursive_flag_key,
            self.__class__.__name__,
            constants.RECURSIVE_FLAG_TRANS,
        )
        self.__params[self.__recursive_flag_key] = str(value)

    @property
    def offset(self):
        """
        int 必填 当前页，默认值是1
        """
        return self.__params.get(self.__offset_key, "")

    @offset.setter
    def offset(self, value):
        utils.check_page(value, self.__offset_key, "header")
        self.__params[self.__offset_key] = str(value)

    @property
    def limit(self):
        """
        int 必填 每页数量，默认值是100，最大限制每页100
        """
        return self.__params.get(self.__limit_key, "")

    @limit.setter
    def limit(self, value):
        value = utils.integer_check(value, self.__limit_key, "header")
        utils.attribute_bounds_check(
            value,
            constants.MIN_LIMIT,
            constants.MAX_LIMIT,
            self.__class__.__name__,
            self.__limit_key,
        )
        self.__params[self.__limit_key] = str(value)

    def get_params(self):
        return copy.deepcopy(self.__params)

    def get_rest_method(self):
        return self.__rest_method

    def get_unnull_keys(self):
        return self.__unnull_keys

    def get_valid_path(self):
        return self.__valid_path
