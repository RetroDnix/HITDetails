#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
发消息到群组
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/a2v4um?type=internal
@author: wecode@huawei.com
"""
import json

from welink.api import utils
from welink.api.base import RestApi


class ImChatBaseRequest(object):
    def __init__(self):
        super(ImChatBaseRequest, self).__init__()

    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        return _body_params


class AppServiceInfo(ImChatBaseRequest):
    """发消息到群组"""

    def __init__(self):
        super(AppServiceInfo, self).__init__()
        self.app_service_id = None
        self.app_service_name = None


class Card(ImChatBaseRequest):
    """卡片消息"""

    def __init__(self):
        super(Card, self).__init__()
        self.digest = None
        self.img_url = None
        self.title = None
        self.card_type = 49

        self.enable_forward = None
        self.is_pc_display = None
        self.source_url = None
        self.handler_uri_android = None
        self.handler_uri_ios = None

        self._card_context_keys = [
            "enable_forward",
            "is_pc_display",
            "source_url",
            "handler_uri_android",
            "handler_uri_ios",
        ]

    def get_data(self):
        _body_params = {}
        _card_context = {}
        for key, value in self.__dict__.items():
            if (
                not key.startswith("_")
                and key not in self._card_context_keys
                and value is not None
            ):
                _body_params[utils.translate_param_name(key)] = _escapesMsg(
                    value
                )
            elif (
                not key.startswith("_")
                and key in self._card_context_keys
                and value is not None
            ):
                _card_context[utils.translate_param_name(key)] = _escapesMsg(
                    value
                )
        if _card_context:
            _body_params["cardContext"] = _card_context
        return _body_params


class Text(ImChatBaseRequest):
    """文本消息"""

    def __init__(self):
        super(Text, self).__init__()
        self.content = None


class Content(ImChatBaseRequest):
    """消息体"""

    def __init__(self):
        super(Content, self).__init__()
        self.card = Card
        self.text = Text

    @staticmethod
    def text():
        return Content().text

    @staticmethod
    def card():
        return Card

    card = Card
    text = Text


class WelinkIMV1ImServiceChatGroupChatRequest(RestApi):
    """创建群组"""

    def __init__(self, url):
        super(WelinkIMV1ImServiceChatGroupChatRequest, self).__init__(url)
        self.app_service_info = AppServiceInfo
        self.app_msg_id = None
        self.group_id = None
        self.content_type = None
        self.content = Content
        self.client_app_id = None
        self.is_push = None
        self.push_ext_data = None
        self.client_send_time = None
        self.card = Card
        self.text = Text

    @staticmethod
    def content():
        return WelinkIMV1ImServiceChatGroupChatRequest("").content()

    def get_valid_path(self):
        return ("/api/welinkim/v1/im-service/chat/group-chat",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        """
        获取请求实例中的消息体参数字典
        :return: dict 消息体参数字典
        """
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[key] = value
        if isinstance(self.app_service_info, AppServiceInfo):
            _body_params["app_service_info"] = self.app_service_info.get_data()
        else:
            del _body_params["app_service_info"]
        # 有文本消息的话，优先发送文本消息
        if not isinstance(self.content, Content):
            del _body_params["text"]
            del _body_params["card"]
            del _body_params["content"]
            return _body_params
        if isinstance(self.content.card, Card):
            _body_params["content"] = self._get_card_content()
        if isinstance(self.content.text, Text):
            _body_params["content"] = self._get_text_content()
        del _body_params["text"]
        del _body_params["card"]
        return _body_params

    def _get_card_content(self):
        if isinstance(self.content, Content) and isinstance(
            self.content.card, Card
        ):
            card_content_body = self.content.card.get_data()
            cardMsg = (
                "<imbody><content><![CDATA["
                + json.dumps(card_content_body)
                + "]]></content></imbody>"
            )
            return self._spliceMessage("0", _escapesMsg(cardMsg))
        return ""

    def _get_text_content(self):
        if isinstance(self.content, Content) and isinstance(
            self.content.text, Text
        ):
            return self._assembleTextMessage(self.content.text.content)
        return ""

    def _assembleTextMessage(self, content):
        # 文本消息内容格式
        msg = (
            "<imbody><imagelist/><html><![CDATA[<DIV>"
            + content
            + "</DIV>]]></html><content><![CDATA["
            + content
            + "]]></content></imbody>"
        )
        return self._spliceMessage("0", _escapesMsg(msg))

    def _spliceMessage(self, flag, msg):
        """拼接消息体"""
        sb = []
        sb.append("<r>")
        sb.append("<n>")
        sb.append("</n>")
        sb.append("<g>")
        sb.append(flag)
        sb.append("</g>")
        sb.append("<c>")
        sb.append(msg)
        sb.append("</c>")
        sb.append("</r>")
        return "".join(sb)


def _escapesMsg(msg):
    if type(msg) != str:
        return msg
    return (
        msg.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )
