#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
获取回看视频的观众
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/skkxe5
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class LivecastV1VideosAudienceRequest(RestApi):
    """获取回看视频的观众"""

    def __init__(self, url):
        super().__init__(url)
        self.video_id = None
        self.limit = None
        self.offset = None

    def get_valid_path(self):
        return ("/api/livecast/v1/videos/audience",)

    def get_rest_method(self):
        return "GET"

    def get_body_params(self):
        return None

    def get_params(self):
        return super().get_body_params()
