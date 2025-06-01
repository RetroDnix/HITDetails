#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新应用详情
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/wg33ml
@author: wecode@huawei.com
"""
from welink.api.articles import Article
from welink.api.base import RestApi


class WeopenWecodeUpdateRequest(RestApi):
    """更新应用详情"""

    def __init__(self, url):
        super().__init__(url)
        self.client_id = None
        self.edition = None
        self.name_zh = None
        self.name_en = None
        self.desc_zh = None
        self.desc_en = None
        self.keyword = None
        self.suppport_info = None
        self.is_support_mobile = None
        self.mobile_url = None
        self.is_support_pc = None
        self.pc_url = None
        self.is_open_system_browser = None
        self.manage_url = None
        self.callback_url = None
        self.white_ip = None
        self.service_from = None
        self.service_owners = None

    def get_valid_path(self):
        return ("/api/weopen/wecode/update",)

    def get_rest_method(self):
        return "PUT"

    def get_body_params(self):
        _body_params = super().get_body_params()
        if _body_params.get("whiteIp"):
            _body_params["whiteIP"] = _body_params["whiteIp"]
            _body_params.pop("whiteIp", None)
        if _body_params.get("isSupportPc"):
            _body_params["isSupportPC"] = _body_params["isSupportPc"]
            _body_params.pop("isSupportPc", None)
        return _body_params
