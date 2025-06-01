#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新文章(新)
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/orz9nu
@author: wecode@huawei.com
"""

from welink.api.base import RestApi
from welink.api.rest.KnowledgeV2ArticlesAddRequest import (
    ArticlesInfo,
    Permission,
    Documents,
)


class KnowledgeV2ArticlesUpdateRequest(RestApi):
    """更新文章(新)"""

    def __init__(self, url):
        super().__init__(url)
        self.source_name = None
        self.source_article_id = None
        self.title = None
        self.corp_user_id = None
        self.user_id = None
        self.content_type = None
        self.content = None
        self.link = None
        self.documents = Documents
        self._documents_list = []
        self.uploaded_document_ids = None
        self.lang = None
        self.is_recommended = None
        self.is_topped = None
        self.rec_data_style = None
        self.excerpt = None
        self.permission = Permission
        self.pub_time = None
        self.cover_img = None
        self._body_object_params = ["documents", "permission"]
        self.is_auto_create_cate = None
        self.cate_name = None

    def add_documents(self, value):
        self._documents_list.append(value)

    def get_valid_path(self):
        return ("/api/knowledge/v2/articles/update",)

    def get_rest_method(self):
        return "PUT"
