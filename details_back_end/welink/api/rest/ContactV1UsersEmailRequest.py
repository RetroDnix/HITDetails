#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取用户邮箱信息
https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/7bkr7r?type=third
@author: wecode@huawei.com
"""
from welink.api.rest.ContactV1UsersRequest import ContactV1UsersRequest


class ContactV1UsersEmailRequest(ContactV1UsersRequest):
    """获取用户邮箱信息"""

    def __init__(self, url):
        super(ContactV1UsersEmailRequest, self).__init__(url)
        self.__valid_path = ("/api/contact/v1/users/email",)

    def get_valid_path(self):
        return self.__valid_path
