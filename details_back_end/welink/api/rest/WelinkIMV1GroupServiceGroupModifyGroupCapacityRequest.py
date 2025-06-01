#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
修改群组容量
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/4g820b
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest(RestApi):
    """修改群组容量"""

    def __init__(self, url):
        super(
            WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest, self
        ).__init__(url)
        self.group_id = None
        self.capacity = None

    def get_valid_path(self):
        return ("/api/welinkim/v1/group-service/group/modify-group-capacity",)

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
