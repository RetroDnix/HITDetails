#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门的人员信息列表(详细信息)
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/fr96pu?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import GetUserListByDepartment


class ContactV1UserUsersRequest(GetUserListByDepartment):
    """查询部门的人员信息列表(详细信息)"""

    def __init__(self, url):
        super(ContactV1UserUsersRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v1/user/users",)

    def get_valid_path(self):
        return self.__valid_path
