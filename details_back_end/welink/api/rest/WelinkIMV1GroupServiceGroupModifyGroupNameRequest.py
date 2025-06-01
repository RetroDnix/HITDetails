#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修改群组名称
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/o1lp0r?type=internal
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WelinkIMV1GroupServiceGroupModifyGroupNameRequest(RestApi):
    """修改群组名称"""

    def __init__(self, url):
        super(WelinkIMV1GroupServiceGroupModifyGroupNameRequest, self).__init__(
            url
        )
        self.group_id = None
        self.name = None
        self.en_name = None

    def get_valid_path(self):
        return ("/api/welinkim/v1/group-service/group/modify-group-name",)

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
