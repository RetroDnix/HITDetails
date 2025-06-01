#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小微推送
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/4h745j
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/nfwhv1
@author: wecode@huawei.com
"""
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class AthenaserviceV1ContextawarePushRequest(RestApi):
    """小微推送"""

    def __init__(self, url):
        super().__init__(url)
        self.to_user_list = None
        self.title_cn = None
        self.title_en = None
        self.end_date = None
        self.url_cn = None
        self.url_en = None
        self.icon_url_cn = None
        self.icon_url_en = None

    def get_valid_path(self):
        return ("/api/athenaservice/v1/contextaware/push",)

    def get_rest_method(self):
        return "POST"
