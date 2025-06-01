#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新待办任务
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/wh37dz?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/9x0gcg?type=third
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class TodoV2UpdatetaskRequest(RestApi):
    """更新待办任务"""

    def __init__(self, url):
        super(TodoV2UpdatetaskRequest, self).__init__(url)
        self.task_id = None
        self.user_id = None
        self.user_name_cn = None
        self.user_name_en = None

    def get_valid_path(self):
        return ("/api/todo/v2/updatetask",)

    def get_rest_method(self):
        return "PUT"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
