#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询父部门信息
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/yoyclo?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/yoyclo?type=third
@author: wecode@huawei.com
"""
from welink.api.base import GetApiUseDeptCode


class ContactV1DepartmentParentRequest(GetApiUseDeptCode):
    """查询父部门信息"""

    def __init__(self, url):
        super(ContactV1DepartmentParentRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v1/department/parent",)

    def get_valid_path(self):
        return self.__valid_path

    def check_headers(self):
        self.unnull_check()
