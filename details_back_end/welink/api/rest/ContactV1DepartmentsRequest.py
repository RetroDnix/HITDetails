#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门详情
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/vk8nvh?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/vk8nvh?type=third
@author: wecode@huawei.com
"""
from welink.api import exceptions
from welink.api.base import RestApi


class ContactV1DepartmentsRequest(RestApi):
    """查询部门详情"""

    def __init__(self, url):
        super(ContactV1DepartmentsRequest, self).__init__(url)
        self.__params = super(ContactV1DepartmentsRequest, self).get_params()
        self.__format_path = super(ContactV1DepartmentsRequest, self).get_path()
        self.__dept_code_key = "deptcode"
        self.__dept_code_path_index = 5
        self.__path_keys = (
            (self.__dept_code_key, self.__dept_code_path_index),
        )
        self.__valid_path = ("/api/contact/v1/departments/{deptcode}",)
        self.__rest_method = "GET"
        self.__init_path_params()

    def __init_path_params(self):
        path = super(ContactV1DepartmentsRequest, self).get_path()
        tmp_path_list = path.split("/")
        for p_key in self.__path_keys:
            if p_key[1] >= len(tmp_path_list):
                raise exceptions.RequestException(
                    "Incorrect URL. The URL must start with  %s. "
                    % list(self.get_valid_path())
                )
            p_value = tmp_path_list[p_key[1]]
            format_key = "{%s}" % p_key[0]
            if p_value != format_key:
                self.__params[p_key[0]] = p_value
            tmp_path_list[p_key[1]] = format_key
        self.__format_path = "/".join(tmp_path_list)

    @property
    def dept_code(self):
        """
        string 必填 部门编码，从用户详细信息中获取部门编码
        """
        return self.__params.get(self.__dept_code_key)

    @dept_code.setter
    def dept_code(self, value):
        self.__params[self.__dept_code_key] = str(value)

    def get_rest_method(self):
        return self.__rest_method

    def get_path(self):
        return self.__format_path.format(**self.__params)

    def get_valid_path(self):
        return self.__valid_path

    def check_path(self):
        if self.__format_path not in self.get_valid_path():
            raise exceptions.RequestException(
                "Incorrect URL. The URL must start with  %s. "
                % list(self.get_valid_path())
            )

    def check_headers(self):
        if not self.dept_code:
            raise exceptions.ParameterException(
                "The parameter [%s] in the request url cannot be empty."
                % self.__dept_code_key
            )
