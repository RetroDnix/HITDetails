#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除知识
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/tcm93s?type=internal
@author: wecode@huawei.com
"""
from welink.api.articles import UpdateArticle
from welink.api.base import RestApi


class KnowledgeV1ArticlesDeleteRequest(RestApi):
    """删除知识"""

    def __init__(self, url):
        super().__init__(url)
        self.__params = UpdateArticle()
        self.__rest_method = "DELETE"
        self.__valid_path = ("/api/knowledge/v1/articles/delete",)

    @property
    def source_name(self):
        """
        string 必填 自定义来源识别字串【允许数字、字母、下划线，最大50个字符】
        """
        return self.__params.source_name

    @source_name.setter
    def source_name(self, value):
        self.__params.source_name = value

    @property
    def source_article_id(self):
        """
        string 必填 当前来源识别文章的id【允许数字、字母、下划线，最大50个字符】
        """
        return self.__params.source_article_id

    @source_article_id.setter
    def source_article_id(self, value):
        self.__params.source_article_id = value

    @property
    def module_type(self):
        """
        string 非必填 文章模块【bulletins:信息发布文章，默认为bulletins】
        """
        return self.__params.module_type

    @module_type.setter
    def module_type(self, value):
        self.__params.module_type = value

    @module_type.deleter
    def module_type(self):
        del self.__params.module_type

    def get_params(self):
        return self.__params.get_data()

    def get_rest_method(self):
        return self.__rest_method

    def check_headers(self):
        self.__params.unnull_check()

    def get_valid_path(self):
        return self.__valid_path
