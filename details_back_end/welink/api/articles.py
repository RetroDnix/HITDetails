#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
知识管理中的文章基本属性相关模块
Create on 2020-03-09
@author wecode@huawei.com
"""
import copy

from welink.api import constants, exceptions, utils
from welink.api.base import ParametersList


class Article(object):
    """
    新增文章参数对象
    """

    def __init__(self):
        self.source_name_key = "sourceName"
        self.source_article_id_key = "sourceArticleId"
        self.title_key = "title"
        self.corp_user_id_key = "corpUserId"
        self.user_id_key = "userId"
        self.content_type_key = "contentType"
        self.content_key = "content"
        self.link_key = "link"
        self.documents_key = "documents"
        self.module_type_key = "moduleType"
        self.lang_key = "lang"
        self.is_recommended_key = "isRecommended"
        self.is_topped_key = "isTopped"
        self.pub_time_key = "pubTime"
        self.cover_img_key = "coverImg"
        self.rec_data_style_key = "recDataStyle"
        self.excerpt_key = "excerpt"
        self.cate_name_key = "cateName"
        self.documents = ParametersList()
        self.documents.item_class_obj = Document
        self.documents.attr_name = self.documents_key
        self.valid_check_map = {
            self.content_type_key: (
                constants.ARTICLE_CONTENT_TYPE_LIST,
                constants.ARTICLE_CONTENT_TYPE_TRANS,
            ),
            self.module_type_key: (
                constants.ARTICLE_MODULE_TYPE_LIST,
                constants.ARTICLE_MODULE_TYPE_TRANS,
            ),
            self.lang_key: (
                constants.ARTICLE_LANG_LIST,
                constants.ARTICLE_LANG_TRANS,
            ),
            self.is_recommended_key: (
                constants.IS_RECOMMENDED_LIST,
                constants.IS_RECOMMENDED_TRANS,
            ),
            self.is_topped_key: (
                constants.IS_TOPPED_LIST,
                constants.IS_TOPPED_TRANS,
            ),
            self.rec_data_style_key: (
                constants.REC_DATA_STYLE_LIST,
                constants.REC_DATA_STYLE_TRANS,
            ),
        }
        self.data = dict()

    @property
    def source_name(self):
        """
        string 必填 自定义来源识别字串【允许数字、字母、下划线，最大50个字符】
        """
        return self.data.get(self.source_name_key)

    @source_name.setter
    def source_name(self, value):
        value = str(value)
        utils.string_re_check(
            value, constants.SOURCE_NAME_RE, self.source_name_key
        )
        utils.bytes_length_check(
            constants.MAX_SOURCE_NAME_LENGTH, value, self.source_name_key
        )
        self.data[self.source_name_key] = value

    @property
    def source_article_id(self):
        """
        string 必填 当前来源识别某篇文章的唯一id 【允许数字、字母、下划线，最大50个字符】
        """
        return self.data.get(self.source_article_id_key)

    @source_article_id.setter
    def source_article_id(self, value):
        value = str(value)
        utils.string_re_check(
            value, constants.SOURCE_ID_RE, self.source_article_id_key
        )
        utils.bytes_length_check(
            constants.MAX_SOURCE_ID_LENGTH, value, self.source_article_id_key,
        )
        self.data[self.source_article_id_key] = value

    @property
    def title(self):
        """
        string 必填 标题
        """
        return self.data.get(self.title_key)

    @title.setter
    def title(self, value):
        self.data[self.title_key] = str(value)

    @property
    def corp_user_id(self):
        """
        string 特殊可选 作者在客户系统的登录标示，客户内唯一。
        corpUserId、userId不可同时为空，都存在时优先使用corp_user_id
        """
        return self.data.get(self.corp_user_id_key)

    @corp_user_id.setter
    def corp_user_id(self, value):
        self.data[self.corp_user_id_key] = str(value)

    @corp_user_id.deleter
    def corp_user_id(self):
        if self.corp_user_id_key in self.data:
            del self.data[self.corp_user_id_key]

    @property
    def user_id(self):
        """
        string 特殊可选 作者在WeLink中的用户账号 【可在用户管理看到类似 xx@tenant 】。
        corpUserId、userId不可同时为空，都存在时优先使用corpUserId
        """
        return self.data.get(self.user_id_key)

    @user_id.setter
    def user_id(self, value):
        self.data[self.user_id_key] = str(value)

    @user_id.deleter
    def user_id(self):
        del self.data[self.user_id_key]

    @property
    def content_type(self):
        """
        int 非必填 类型【0:链接型，1:内容型，默认为：1】
        """
        return self.data.get(self.content_type_key)

    @content_type.setter
    def content_type(self, value):
        value = utils.integer_check(
            value, self.content_type_key, self.__class__.__name__
        )
        self.valid_check(self.content_type_key, value)
        self.data[self.content_type_key] = value

    @content_type.deleter
    def content_type(self):
        if self.content_type_key in self.data:
            del self.data[self.content_type_key]

    @property
    def content(self):
        """
        string 非必填 内容【contentType为1必传，其它非必须传】
        """
        return self.data.get(self.content_key)

    @content.setter
    def content(self, value):
        self.data[self.content_key] = str(value)

    @content.deleter
    def content(self):
        if self.content_key in self.data:
            del self.data[self.content_key]

    @property
    def link(self):
        """
        string 非必填 链接型文章的链接【contentType为0必传 】
        """
        return self.data.get(self.link_key)

    @link.setter
    def link(self, value):
        self.data[self.link_key] = str(value)

    @link.deleter
    def link(self):
        if self.link_key in self.data:
            del self.data[self.link_key]

    @property
    def module_type(self):
        """
        string 非必填 文章模块【bulletins:信息发布文章，默认为bulletins】
        """
        return self.data.get(self.module_type_key)

    @module_type.setter
    def module_type(self, value):
        value = str(value)
        self.valid_check(self.module_type_key, value)
        self.data[self.module_type_key] = value

    @module_type.deleter
    def module_type(self):
        if self.module_type_key in self.data:
            del self.data[self.module_type_key]

    @property
    def lang(self):
        """
        int 非必填 语言【0:中文 1:英文，默认：0】
        """
        return self.data.get(self.lang_key)

    @lang.setter
    def lang(self, value):
        value = utils.integer_check(
            value, self.lang_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.lang_key, value)
        self.data[self.lang_key] = value

    @lang.deleter
    def lang(self):
        if self.lang_key in self.data:
            del self.data[self.lang_key]

    @property
    def is_recommended(self):
        """
        int 非必填 是否推荐【0:否 1:是，默认：0】
        """
        return self.data.get(self.is_recommended_key)

    @is_recommended.setter
    def is_recommended(self, value):
        value = utils.integer_check(
            value, self.is_recommended_key, class_name=self.__class__.__name__,
        )
        self.valid_check(self.is_recommended_key, value)
        self.data[self.is_recommended_key] = value

    @is_recommended.deleter
    def is_recommended(self):
        if self.is_recommended_key in self.data:
            del self.data[self.is_recommended_key]

    @property
    def is_topped(self):
        """
        int 非必填 是否置顶【0:否 1:是，默认：0】
        """
        return self.data.get(self.is_topped_key)

    @is_topped.setter
    def is_topped(self, value):
        value = utils.integer_check(
            value, self.is_topped_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.is_topped_key, value)
        self.data[self.is_topped_key] = value

    @is_topped.deleter
    def is_topped(self):
        if self.is_topped_key in self.data:
            del self.data[self.is_topped_key]

    @property
    def pub_time(self):
        """
        int 非必填 发布时间，秒为单位的时间戳【不传则取当前时间】
        """
        return self.data.get(self.pub_time_key)

    @pub_time.setter
    def pub_time(self, value):
        value = utils.integer_check(value, self.pub_time_key)
        self.data[self.pub_time_key] = value

    @pub_time.deleter
    def pub_time(self):
        if self.pub_time_key in self.data:
            del self.data[self.pub_time_key]

    @property
    def cover_img(self):
        """
        string 非必填 封面图URL
        """
        return self.data.get(self.cover_img_key)

    @cover_img.setter
    def cover_img(self, value):
        self.data[self.cover_img_key] = str(value)

    @cover_img.deleter
    def cover_img(self):
        if self.cover_img_key in self.data:
            del self.data[self.cover_img_key]

    @property
    def rec_data_style(self):
        """
        int 非必填 条目模板，【1：'左文右图',2：'大图卡',3：'视频（大）',4：'视频（小）',
        5：'直播',6：'音频',7：'博客',8:问答,9:文档式。默认为：1】
        """
        return self.data.get(self.rec_data_style_key)

    @rec_data_style.setter
    def rec_data_style(self, value):
        value = utils.integer_check(
            value, self.rec_data_style_key, class_name=self.__class__.__name__,
        )
        self.valid_check(self.rec_data_style_key, value)
        self.data[self.rec_data_style_key] = value

    @rec_data_style.deleter
    def rec_data_style(self):
        if self.rec_data_style_key in self.data:
            del self.data[self.rec_data_style_key]

    @property
    def excerpt(self):
        """
        string 非必填 摘要信息
        """
        return self.data.get(self.excerpt_key)

    @excerpt.setter
    def excerpt(self, value):
        self.data[self.excerpt_key] = str(value)

    @excerpt.deleter
    def excerpt(self):
        if self.excerpt_key in self.data:
            del self.data[self.excerpt_key]

    @property
    def cate_name(self):
        """
        string 非必填 文章所属分类，不传则取默认分类或第一个分类，
        传则取传过来的分类，没有则新建分类
        """
        return self.data.get(self.cate_name_key)

    @cate_name.setter
    def cate_name(self, value):
        self.data[self.cate_name_key] = str(value)

    @cate_name.deleter
    def cate_name(self):
        if self.cate_name_key in self.data:
            del self.data[self.cate_name_key]

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        if key in self.valid_check_map:
            utils.attribute_valid_check(
                self.valid_check_map[key][0],
                value,
                key,
                self.__class__.__name__,
                self.valid_check_map[key][1],
            )

    def unnull_check(self):
        """
        必填字段校验，检查文章实例的必填字段是否设置完成
        """
        for key in self.unnull_keys:
            if key not in self.data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )
        unnull_keys = [k for k in self.one_of_unnull_keys if k in self.data]
        if not unnull_keys and self.one_of_unnull_keys:
            raise exceptions.ParameterException(
                "The userId and corpUserId parameters " "cannot be all empty. "
            )
        if (
            self.content_type_key in self.data
            and self.content_type_unnull_keys[self.content_type]
            not in self.data
        ):
            raise exceptions.ParameterException(
                "The %s parameter cannot be empty when %s is set to %s."
                % (
                    self.content_type_unnull_keys[self.content_type],
                    self.content_type_key,
                    self.content_type,
                )
            )

    def get_data(self):
        """
        以map形式获取文章实例的内容
        :return: dict 文章实例的内容
        """
        data = copy.deepcopy(self.data)
        if self.documents.get_data():
            data[self.documents_key] = self.documents.get_data()
        return data


class Document(object):
    """
    文章附件对象
    """

    def __init__(self):
        self.__name_key = "name"
        self.__size_key = "size"
        self.__url_key = "url"
        self.__data = dict()
        self.__unnull_keys = (self.__name_key, self.__url_key)

    @property
    def name(self):
        """
        string 必填 文档完整名，包含后缀
        """
        return self.__data.get(self.__name_key)

    @name.setter
    def name(self, value):
        self.__data[self.__name_key] = value

    @property
    def size(self):
        """
        string 非必填 文件大小,单位B
        """
        return self.__data.get(self.__size_key)

    @size.setter
    def size(self, value):
        self.__data[self.__size_key] = value

    @property
    def url(self):
        """
        string 必填 下载地址
        """
        return self.__data.get(self.__url_key)

    @url.setter
    def url(self, value):
        self.__data[self.__url_key] = value

    def get_data(self):
        """
        以dict形式获取附件实例的内容
        :return: dict 附件实例的内容
        """
        return copy.deepcopy(self.__data)

    def unnull_check(self):
        """
        必填字段校验，检查附件实例中的必填字段是否设置完成
        """
        for k in self.__unnull_keys:
            if k not in self.__data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (k, self.__class__.__name__)
                )


class UpdateArticle(Article):
    """
    更新文章属性时所需参数对象
    """

    def __init__(self):
        super(UpdateArticle, self).__init__()
        self.unnull_keys = (
            self.source_name_key,
            self.source_article_id_key,
        )
        self.one_of_unnull_keys = tuple()

    @property
    def title(self):
        """
        string 非必填 标题
        """
        return self.data.get(self.title_key)

    @title.setter
    def title(self, value):
        self.data[self.title_key] = str(value)

    @title.deleter
    def title(self):
        if self.title_key in self.data:
            del self.data[self.title_key]
