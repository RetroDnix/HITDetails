#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询部门的人员信息列表(简单信息)
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/kqn7u3?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import GetUserListByDepartment


class ContactV2UserUseridRequest(GetUserListByDepartment):
    """查询部门的人员信息列表(简单信息)"""

    def __init__(self, url):
        super(ContactV2UserUseridRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v2/user/userid",)

    def get_valid_path(self):
        return self.__valid_path
