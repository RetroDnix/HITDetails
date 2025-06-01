#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建群组
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/acfmeo?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WelinkIMV1GroupServiceGroupCreateGroupRequest(RestApi):
    """创建群组"""

    def __init__(self, url):
        super(WelinkIMV1GroupServiceGroupCreateGroupRequest, self).__init__(url)
        self.owner_account = None
        self.user_account = None
        self.name = None
        self.init_capacity = None
        self.group_type = None
        self.desc = None
        self.manifesto = None
        self.group_service_policy = None
        self.cross_corp_group = None
        self.group_ext_data = None

    def get_valid_path(self):
        return ("/api/welinkim/v1/group-service/group/create-group",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        """
        获取请求实例中的消息体参数字典
        :return: dict 消息体参数字典
        """
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params
