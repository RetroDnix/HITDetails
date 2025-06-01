#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
新增文章(新)
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/5lkanx
@author: wecode@huawei.com
"""

from welink.api.base import RestApi


class ArticlesInfo(object):
    """文章基础信息"""

    def __init__(self):
        super().__init__()

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class Permission(ArticlesInfo):
    """私密权限范围【详见下表】。说明：租户管理员、知识管理员、文章所属公告组件【对应 componentName 字段】管理员 默认具有权限。"""

    def __init__(self):
        super().__init__()
        self.dept_codes = None
        self.user_ids = None
        self.corp_user_ids = None


class Documents(ArticlesInfo):
    """附件信息。每个文件内容，name:文档完整名，包含后缀；size:文件大小,单位B；url:下载地址"""

    def __init__(self):
        super().__init__()
        self.name = None
        self.size = None
        self.url = None


class KnowledgeV2ArticlesAddRequest(RestApi):
    """新增文章(新)"""

    def __init__(self, url):
        super().__init__(url)
        self.title = None
        self.content_type = None
        self.source_name = None
        self.source_article_id = None
        self.content = None
        self.link = None
        self.corp_user_id = None
        self.user_id = None
        self.documents = Documents
        self._documents_list = []
        self.uploaded_document_ids = None
        self.module_type = None
        self.component_name = None
        self.lang = None
        self.is_recommended = None
        self.is_topped = None
        self.permission = Permission
        self.pub_time = None
        self.cover_img = None
        self.rec_data_style = None
        self.excerpt = None
        self.is_auto_create_cate = None
        self.cate_name = None

        self._body_object_params = ["documents", "permission"]

    def add_documents(self, value):
        self._documents_list.append(value)

    def get_valid_path(self):
        return ("/api/knowledge/v2/articles/add",)

    def get_rest_method(self):
        return "POST"
