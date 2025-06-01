#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量删除用户
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/e5kpsd
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV1UserInfo import PersonInfos as OriginPeronInfos


class PersonInfos(OriginPeronInfos):
    def __init__(self):
        super().__init__()
        self.is_delete_user = None


class ContactV1UserBatchDeleteRequest(RestApi):
    """批量删除用户"""

    def __init__(self, url):
        super().__init__(url)
        self.person_infos = PersonInfos
        self._person_infos_list = []

    def get_valid_path(self):
        return ("/api/contact/v1/user/batch/delete",)

    def get_rest_method(self):
        return "POST"

    def add_person_infos(self, value):
        self._person_infos_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"personInfos": self._person_infos_list}
        return _body_params
