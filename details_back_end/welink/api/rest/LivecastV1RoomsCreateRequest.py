#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建直播
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/okirq3
@author: wecode@huawei.com
"""

from welink.api.base import RestApi
from welink.api.rest.ObjectParamBase import ObjectParamBase


class Agendas(ObjectParamBase):
    def __init__(self):
        self.time = None
        self.content = None


class Speakers(ObjectParamBase):
    def __init__(self):
        self.name = None
        self.introduction = None


class LivecastV1RoomsCreateRequest(RestApi):
    """获取直播间详情"""

    def __init__(self, url):
        super().__init__(url)
        self.subject = None
        self.userId = None
        self.introduction = None
        self.page_img_url = None
        self.start_time = None
        self.end_time = None
        self.viewing_scope = None
        self.need_vod = None
        self.comment_status = None
        self.ano_comments = None
        self.language = None
        self.agendas = Agendas
        self.speakers = Speakers
        self.enable_watermark = None

    def get_valid_path(self):
        return ("/api/livecast/v1/rooms/create",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        _body_params = super().get_body_params()
        if isinstance(self.agendas, Agendas):
            _body_params["agendas"] = self.agendas.get_data()
        else:
            _body_params.pop("agendas", None)
        if isinstance(self.speakers, Speakers):
            _body_params["speakers"] = self.speakers.get_data()
        else:
            _body_params.pop("speakers", None)
        return _body_params
