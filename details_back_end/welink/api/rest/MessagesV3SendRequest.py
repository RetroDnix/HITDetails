#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
公众号消息接口
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/n792d4?type=internal
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/sx2v22/n792d4?type=third
@author: wecode@huawei.com
"""
import copy
import time

from welink.api import constants, utils
from welink.api.base import RestApi
from welink.api.bilingualism import Bilingualism


class MessagesV3SendRequest(RestApi):
    """公众号消息接口"""

    def __init__(self, url):
        super(MessagesV3SendRequest, self).__init__(url)
        self.__body_params = super(MessagesV3SendRequest, self).get_params()
        self.__rest_method = "POST"

        self.__msg_range_key = "msgRange"
        self.__to_user_list_key = "toUserList"
        self.__msg_title_key = "msgTitle"
        self.__msg_content_key = "msgContent"
        self.__url_type_key = "urlType"
        self.__url_path_key = "urlPath"
        self.__msg_owner_key = "msgOwner"
        self.__create_time_key = "createTime"
        self.__msg_display_mode_key = "msgDisplayMode"
        self.__desktop_url_path_key = "desktopUrlPath"
        self.__is_force_tips = "isForceTips"
        self.__unnull_keys = (
            self.__to_user_list_key,
            self.__msg_range_key,
            self.__msg_title_key,
            self.__msg_content_key,
            self.__url_type_key,
            self.__url_path_key,
            self.__msg_owner_key,
        )
        self.__valid_path = ("/api/messages/v3/send",)
        self.__unescaped_mark = "-".join(list(str(int(time.time()))))

    @property
    def msg_range(self):
        """
        string 必填 0：按用户推送
        """
        return self.__body_params.get(self.__msg_range_key, "")

    @msg_range.setter
    def msg_range(self, value):
        value = utils.integer_check(value, self.__msg_range_key, "body")
        utils.attribute_valid_check(
            constants.MSG_RANGE_LIST,
            value,
            self.__msg_range_key,
            self.__class__.__name__,
            constants.MSG_RANGE_TRANS,
        )
        self.__body_params[self.__msg_range_key] = value

    @property
    def to_user_list(self):
        """
        list 必填 成员ID列表（消息接收者，多个接收者用','分隔，最多支持1000个）。
        """
        return self.__body_params.get(self.__to_user_list_key, list())

    @to_user_list.setter
    def to_user_list(self, value):
        utils.type_check(value, list)
        user_list = [str(u) for u in value]
        utils.records_count_check(
            constants.MAX_USER_NUMBER_TO_BE_PUSHED_MSG,
            len(user_list),
            "queried",
        )
        self.__body_params[self.__to_user_list_key] = user_list

    @property
    def msg_title(self):
        """
        string 必填 标题，不超过128个字节，超过会自动截断，
               如果不需要双语，可直接传string如“出差电子流” ,
               需要双语则参考请求包体示例，传入{json}string对象。
        """
        return self.__body_params.get(self.__msg_title_key, "")

    @msg_title.setter
    def msg_title(self, value):
        value = str(value)
        value = utils.bilingualism_check(value, Bilingualism)
        if utils.is_json(value):
            value = utils.add_unescaped_mark(value, self._get_unescaped_mark())
        print("value: %s" % value)
        self.__body_params[self.__msg_title_key] = value

    @property
    def msg_content(self):
        """
        string 必填 描述，不超过512个字节，超过会自动截断，如果不需要双语，
               可直接传string如“张三提交了一个去上海的出差申请” ，双语场景同上。
        """
        return self.__body_params.get(self.__msg_content_key, "")

    @msg_content.setter
    def msg_content(self, value):
        value = str(value)
        value = utils.bilingualism_check(value, Bilingualism)
        self.__body_params[self.__msg_content_key] = value

    @property
    def url_type(self):
        """
        string 必填 链接类型定义，如"html",则可跳转到http://url地址。
        """
        return self.__body_params.get(self.__url_type_key, "")

    @url_type.setter
    def url_type(self, value):
        self.__body_params[self.__url_type_key] = str(value)

    @property
    def url_path(self):
        """
        string 必填 点击后跳转的链接，如需要跳转到微码，参考推送消息实现免登。
        """
        return self.__body_params.get(self.__url_path_key, "")

    @url_path.setter
    def url_path(self, value):
        self.__body_params[self.__url_path_key] = str(value)

    @property
    def msg_owner(self):
        """
        string 必填 消息所有者，如“差旅管理”。
        """
        return self.__body_params.get(self.__msg_owner_key, "")

    @msg_owner.setter
    def msg_owner(self, value):
        self.__body_params[self.__msg_owner_key] = str(value)

    @property
    def create_time(self):
        """
        string 非必填 消息创建时间，可不传系统将自动生成推送时间。
        """
        return self.__body_params.get(self.__create_time_key, "")

    @create_time.setter
    def create_time(self, value):
        self.__body_params[self.__create_time_key] = str(value)

    @create_time.deleter
    def create_time(self):
        if self.__create_time_key in self.__body_params:
            del self.__body_params[self.__create_time_key]

    @property
    def msg_display_mode(self):
        """
        string 非必填 默认0表示支持手机链接和PC链接，配置为1时仅移动端显示
        """
        return self.__body_params.get(self.__msg_display_mode_key)

    @msg_display_mode.setter
    def msg_display_mode(self, value):
        value = utils.integer_check(value, self.__msg_display_mode_key, "body")
        utils.attribute_valid_check(
            constants.MSG_DISPLAY_MODE_LIST,
            value,
            self.__msg_display_mode_key,
            self.__class__.__name__,
            constants.MSG_DISPLAY_MODE_TRANS,
        )
        self.__body_params[self.__msg_display_mode_key] = value

    @msg_display_mode.deleter
    def msg_display_mode(self):
        if self.__msg_display_mode_key in self.__body_params:
            del self.__body_params[self.__msg_display_mode_key]

    @property
    def desktop_url_path(self):
        """
        string 非必填 当msgDisplMode配置为0时，需要配置该参数，
               如果不配置那就默认使用urlPath
        """
        return self.__body_params.get(self.__desktop_url_path_key, "")

    @desktop_url_path.setter
    def desktop_url_path(self, value):
        self.__body_params[self.__desktop_url_path_key] = str(value)

    @desktop_url_path.deleter
    def desktop_url_path(self):
        if self.__desktop_url_path_key in self.__body_params:
            del self.__body_params[self.__desktop_url_path_key]

    @property
    def is_force_tips(self):
        """
        string 非必填 当msgDisplMode配置为0时，需要配置该参数，
               如果不配置那就默认使用urlPath
        """
        return self.__body_params.get(self.__is_force_tips, "")

    @is_force_tips.setter
    def is_force_tips(self, value):
        self.__body_params[self.__is_force_tips] = str(value)

    @is_force_tips.deleter
    def is_force_tips(self):
        if self.__is_force_tips in self.__body_params:
            del self.__body_params[self.__is_force_tips]

    def get_rest_method(self):
        return self.__rest_method

    def get_unnull_body_keys(self):
        return self.__unnull_keys

    def get_body_params(self):
        return copy.deepcopy(self.__body_params)

    def _get_body_params_for_curl(self):
        curl_body = self.get_body_params()
        if utils.is_json(self.msg_title):
            curl_body[self.__msg_title_key] = utils.add_unescaped_mark(
                self.msg_title, self._get_unescaped_mark()
            )
        if utils.is_json(self.msg_content):
            curl_body[self.__msg_content_key] = utils.add_unescaped_mark(
                self.msg_content, self._get_unescaped_mark()
            )
        return curl_body

    def get_valid_path(self):
        return self.__valid_path

    def _get_unescaped_mark(self):
        return self.__unescaped_mark
