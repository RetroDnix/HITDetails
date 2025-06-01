#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门人员信息列表(ISV)
https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/bc17pu?type=third
@author: wecode@huawei.com
"""
from welink.api.rest.ContactV1UserUsersRequest import ContactV1UserUsersRequest


class ContactV2UserUsersRequest(ContactV1UserUsersRequest):
    """查询部门人员信息列表(ISV)"""

    def __init__(self, url):
        super(ContactV2UserUsersRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v2/user/users",)

    def get_valid_path(self):
        return self.__valid_path
