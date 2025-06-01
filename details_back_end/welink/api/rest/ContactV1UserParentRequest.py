#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询用户父级部门
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/r464tk?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/r464tk?type=third
@author: wecode@huawei.com
"""
from welink.api.base import GetApiByUserInfo


class ContactV1UserParentRequest(GetApiByUserInfo):
    """查询用户父级部门"""

    def __init__(self, url):
        super(ContactV1UserParentRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v1/user/parent",)

    def get_valid_path(self):
        return self.__valid_path

    def check_headers(self):
        self.unnull_check()
