#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
查询应用可见权限人员信息列表
https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/isdppu?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV3UserPermissionUsersRequest(RestApi):
    """查询应用可见权限人员信息列表"""

    def __init__(self, url):
        super(ContactV3UserPermissionUsersRequest, self).__init__(url)
        self.page_no = None
        self.page_size = None

    def get_valid_path(self):
        return ("/api/contact/v3/user/permission/users",)

    def get_rest_method(self):
        return "GET"
