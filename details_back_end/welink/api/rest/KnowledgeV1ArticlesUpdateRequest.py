#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新知识
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/3xl7pg?type=internal
@author: wecode@huawei.com
"""
from welink.api.articles import UpdateArticle
from welink.api.base import RestApi


class KnowledgeV1ArticlesUpdateRequest(RestApi):
    """更新知识"""

    def __init__(self, url):
        super(KnowledgeV1ArticlesUpdateRequest, self).__init__(url)
        self.__body_params = UpdateArticle()
        self.__rest_method = "PUT"
        self.__valid_path = ("/api/knowledge/v1/articles/update",)

    @property
    def source_name(self):
        """
        string 必填 自定义来源识别字串【允许数字、字母、下划线，最大50个字符】
        """
        return self.__body_params.source_name

    @source_name.setter
    def source_name(self, value):
        self.__body_params.source_name = value

    @property
    def source_article_id(self):
        """
        string 必填 当前来源识别文章的id【允许数字、字母、下划线，最大50个字符】
        """
        return self.__body_params.source_article_id

    @source_article_id.setter
    def source_article_id(self, value):
        self.__body_params.source_article_id = value

    @property
    def title(self):
        """
        string 非必填 标题【不传或为空表示不修改】
        """
        return self.__body_params.title

    @title.deleter
    def title(self):
        del self.__body_params.title

    @title.setter
    def title(self, value):
        self.__body_params.title = value

    @property
    def user_id(self):
        """
        string 非必填 作者在WeLink中的用户账号【可在用户管理看到类似 xx@tenant 】。
               corpUserId、userId都存在时优先使用corpUserId。【不传或为空表示不修改】
        """
        return self.__body_params.user_id

    @user_id.deleter
    def user_id(self):
        del self.__body_params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__body_params.user_id = value

    @property
    def corp_user_id(self):
        """
        string 非必填 作者在客户系统的登录标示，客户内唯一。
               corpUserId、userId都存在时优先使用corpUserId。【不传或为空表示不修改】
        """
        return self.__body_params.corp_user_id

    @corp_user_id.deleter
    def corp_user_id(self):
        del self.__body_params.corp_user_id

    @corp_user_id.setter
    def corp_user_id(self, value):
        self.__body_params.corp_user_id = value

    @property
    def content_type(self):
        """
        string 非必填 类型【0:链接型，1:内容型，不传或为空表示不修改】
        """
        return self.__body_params.content_type

    @content_type.deleter
    def content_type(self):
        del self.__body_params.content_type

    @content_type.setter
    def content_type(self, value):
        self.__body_params.content_type = value

    @property
    def content(self):
        """
        string 非必填 内容【不传或为空表示不修改】
        """
        return self.__body_params.content

    @content.deleter
    def content(self):
        del self.__body_params.content

    @content.setter
    def content(self, value):
        self.__body_params.content = value

    @property
    def link(self):
        """
        string 非必填 链接型文章的链接【不传或为空表示不修改】
        """
        return self.__body_params.link

    @link.deleter
    def link(self):
        del self.__body_params.link

    @link.setter
    def link(self, value):
        self.__body_params.link = value

    @property
    def module_type(self):
        """
        string 非必填 文章模块【bulletins:信息发布文章，默认为bulletins】
        """
        return self.__body_params.module_type

    @module_type.deleter
    def module_type(self):
        del self.__body_params.module_type

    @module_type.setter
    def module_type(self, value):
        self.__body_params.module_type = value

    @property
    def lang(self):
        """
        int 非必填 语言【0:中文 1:英文，不传或为空表示不修改】
        """
        return self.__body_params.lang

    @lang.deleter
    def lang(self):
        del self.__body_params.lang

    @lang.setter
    def lang(self, value):
        self.__body_params.lang = value

    @property
    def is_recommended(self):
        """
        int 非必填 是否推荐【0:否 1:是，不传或为空表示不修改】
        """
        return self.__body_params.is_recommended

    @is_recommended.deleter
    def is_recommended(self):
        del self.__body_params.is_recommended

    @is_recommended.setter
    def is_recommended(self, value):
        self.__body_params.is_recommended = value

    @property
    def is_topped(self):
        """
        int 非必填 是否置顶【0:否 1:是，不传或为空表示不修改】
        """
        return self.__body_params.is_topped

    @is_topped.deleter
    def is_topped(self):
        del self.__body_params.is_topped

    @is_topped.setter
    def is_topped(self, value):
        self.__body_params.is_topped = value

    @property
    def pub_time(self):
        """
        int 非必填 发布时间，秒为单位的时间戳【不传或为空表示不修改】
        """
        return self.__body_params.pub_time

    @pub_time.deleter
    def pub_time(self):
        del self.__body_params.pub_time

    @pub_time.setter
    def pub_time(self, value):
        self.__body_params.pub_time = value

    @property
    def cover_img(self):
        """
        string 非必填 封面图URL【不传表示不修改，为空表示置空】
        """
        return self.__body_params.cover_img

    @cover_img.deleter
    def cover_img(self):
        del self.__body_params.cover_img

    @cover_img.setter
    def cover_img(self, value):
        self.__body_params.cover_img = value

    @property
    def rec_data_style(self):
        """
        int 非必填 条目模板【1：'左文右图',2：'大图卡',3：'视频（大）',4：'视频（小）',
            5：'直播',6：'音频',7：'博客',8:问答,9:文档式，不传或为空表示不修改】
        """
        return self.__body_params.rec_data_style

    @rec_data_style.deleter
    def rec_data_style(self):
        del self.__body_params.rec_data_style

    @rec_data_style.setter
    def rec_data_style(self, value):
        self.__body_params.rec_data_style = value

    @property
    def excerpt(self):
        """
        string 非必填 摘要信息【不传表示不修改，为空表示置空】
        """
        return self.__body_params.excerpt

    @excerpt.deleter
    def excerpt(self):
        del self.__body_params.excerpt

    @excerpt.setter
    def excerpt(self, value):
        self.__body_params.excerpt = value

    @property
    def cate_name(self):
        """
        string 非必填 文章所属分类，
        【不传或为空表示不修改，传则取传过来的分类，没有则新建分类】
        """
        return self.__body_params.cate_name

    @cate_name.deleter
    def cate_name(self):
        del self.__body_params.cate_name

    @cate_name.setter
    def cate_name(self, value):
        self.__body_params.cate_name = value

    @property
    def documents(self):
        """
        文章附件对象
        """
        return self.__body_params.documents.item_class_obj

    def add_documents(self, value):
        """
        在请求实例中添加新的文章附加信息对象
        :param value: Document 需要添加的新的文章附件信息对象
        """
        self.__body_params.documents.add_param(value)

    def get_documents_by_index(self, index):
        """
        根据索引获取指定位置的文章附件信息
        :param index: int 索引
        :return: dict 获取到的文章附件信息
        """
        return self.__body_params.documents.get_param_by_index(index)

    def del_documents(self, index):
        """
        根据索引删除指定位置的文章附件信息对象
        :param index: int 索引
        """
        self.__body_params.documents.del_param_by_index(index)

    def set_documents(self, value, index):
        """
        根据索引修改指定位置为文章附件信息对象
        :param value: Document 需要修改的新的文章杜建信息对象
        :param index: int 索引
        """
        self.__body_params.documents.set_param_by_index(value, index)

    def get_rest_method(self):
        return self.__rest_method

    def get_body_params(self):
        return self.__body_params.get_data()

    def get_valid_path(self):
        return self.__valid_path

    def check_bodies(self):
        self.__body_params.unnull_check()
