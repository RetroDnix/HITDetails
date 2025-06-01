#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量更新客户侧用户corpUserId
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/7kqqf0
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi, utils
from welink.api.rest.ContactV1UserInfo import PersonInfos


class ContactV1UserBatchUpdatecorpuidRequest(RestApi):
    """批量更新客户侧用户corpUserId"""

    def __init__(self, url):
        super().__init__(url)
        self.person_infos = PersonInfos
        self._person_infos_list = []

    def get_valid_path(self):
        return ("/api/contact/v1/user/batch/updatecorpuid",)

    def get_rest_method(self):
        return "POST"

    def add_person_infos(self, value):
        self._person_infos_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"personInfos": self._person_infos_list}
        return _body_params
