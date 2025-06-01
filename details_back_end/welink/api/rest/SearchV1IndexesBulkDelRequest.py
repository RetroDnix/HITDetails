#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
搜索服务-批量删除数据
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/47dw44
@author: wecode@huawei.com
"""

from welink.api.base import RestApi
from welink.api.rest.SearchV1Items import Items as OriginItems


class Items(OriginItems):
    """搜索基础信息"""

    def __init__(self):
        super().__init__()


class SearchV1IndexesBulkDelRequest(RestApi):
    """搜索服务-批量删除数据"""

    def __init__(self, url):
        super().__init__(url)
        self.items = Items
        self._items_list = []

    def get_valid_path(self):
        return ("/api/search/v1/indexes/bulk/del",)

    def get_rest_method(self):
        return "POST"

    def add_items(self, value):
        self._items_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"items": self._items_list}
        return _body_params
