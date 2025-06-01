#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
异步批量同步用户（新）
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/u4u9ge?type=internal
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi
from welink.api.rest.ContactV2UsersUpdateRequest import PersonInfo


class PersonInfoBulk(PersonInfo):
    """用户信息"""

    def __init__(self):
        super(PersonInfoBulk, self).__init__()
        self.mobile_number = None


class ContactV2UsersBulkRequest(RestApi):
    """异步批量同步用户（新）"""

    def __init__(self, url):
        super(ContactV2UsersBulkRequest, self).__init__(url)
        self.person_info = PersonInfoBulk
        self._person_info_list = []

    def get_valid_path(self):
        return ("/api/contact/v2/users/bulk",)

    def get_rest_method(self):
        return "POST"

    def add_person_info(self, value):
        self._person_info_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"personInfo": self._person_info_list}
        return _body_params
