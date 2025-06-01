#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新增待办任务(新)
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/eatdqi
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/m73r5b
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class TodoV3AddtaskRequest(RestApi):
    """新增待办任务(新)"""

    def __init__(self, url):
        super().__init__(url)
        self.task_id = None
        self.task_title = None
        self.user_id = None
        self.user_name_cn = None
        self.user_name_en = None
        self.details_url = None
        self.details_url_pc = None
        self.app_name = None
        self.applicant_user_id = None
        self.applicant_user_name_cn = None
        self.applicant_user_name_en = None
        self.is_msg = None
        self.is_show_applicant_user_name = None
        self.applicant_id = None
        self.business_code = None

    def get_valid_path(self):
        return ("/api/todo/v3/addtask",)

    def get_rest_method(self):
        return "POST"
