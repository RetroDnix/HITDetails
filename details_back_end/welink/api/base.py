#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
接口请求基础模块
Create on 2020-02-29
@author wecode@huawei.com
"""
import copy
import json
import urllib
from urllib import parse, request

import welink
from welink.api import constants, exceptions, utils
from welink.api.depts import DeptCode
from welink.api.users import UserInfo


class RestApi(object):
    """
    restApi接口的基础请求对象
    """

    def __init__(self, url=""):
        if not url:
            raise exceptions.RequestException("The domain cannot be empty.")

        url_parse = parse.urlparse(url)
        if url_parse.scheme not in constants.PROTOCOLS:
            raise exceptions.RequestException(
                "Invalid protocol. protocol must be one of %s"
                % str(constants.PROTOCOLS)
            )

        self.__protocol = url_parse.scheme  # 协议
        self.__domain = url_parse.netloc  # 域名
        self.__path = url_parse.path  # url路径
        self.__params = dict(parse.parse_qsl(parse.urlsplit(url).query))  # 参数
        self.__unnull_keys = tuple()  # 非空参数集
        self.__body_params = dict()  # 消息体
        self.__unnull_body_keys = tuple()  # 非空消息体集
        self.__request_header = constants.REQUEST_HEADERS  # 请求头
        self.__rest_method = ""  # REST方法
        self.__access_token = ""  # Token
        self.__is_token_need = True  # 是否需要Token验证
        self.__valid_path = ("",)
        self.__debug = False
        self.__unescaped_mark = ""
        self._body_object_params = []  # body消息体中为子Object的参数的key

    def get_protocol(self):
        """
        获取请求实例的请求协议
        :return: string 请求协议
        """
        return self.__protocol

    def get_domain(self):
        """
        获取请求实例中的域名
        :return: string 域名
        """
        return self.__domain

    def get_path(self):
        """
        获取请求实例中的url路径
        :return: string url路径
        """
        return self.__path

    def get_params(self):
        """
        获取请求实例中的查询参数
        :return: map 查询参数
        """
        return copy.deepcopy(self.__params)

    def get_unnull_keys(self):
        """
        获取请求实例中的必填字段数组
        :return: list 必填字段数组
        """
        return self.__unnull_keys

    def get_body_params(self):
        """
        获取请求实例中的消息体参数字典
        :return: dict 消息体参数字典
        """
        if self.__body_params is None or self.__body_params == {}:
            _body_params = {}
            for key, value in self.__dict__.items():
                if not key.startswith("_") and value is not None:
                    _body_params[utils.translate_param_name(key)] = value
            for key in self._body_object_params:
                try:
                    _body_params[key] = _body_params[key].get_data()
                except TypeError:
                    del _body_params[key]
            return _body_params
        return copy.deepcopy(self.__body_params)

    def _get_body_params_for_curl(self):
        return copy.deepcopy(self.get_body_params())

    def get_unnull_body_keys(self):
        """
        获取请求实例消息体参数中的必填字段
        :return: list 消息体参数的必填字段数组
        """
        return self.__unnull_body_keys

    def get_request_header(self):
        """
        获取请求实例中的消息头字典
        :return: dict 消息头字典
        """
        return self.__request_header

    def set_request_header(self, header):
        """
        设置请求实例的消息头
        :param header: dict 需要设置的消息头字典
        """
        if not isinstance(header, dict):
            raise exceptions.RequestException(
                "Invalid request header. "
                "The request header must be of the dictionary type."
            )
        self.__request_header = header

    def get_rest_method(self):
        """
        获取请求实例的REST请求方法类型
        :return: string REST请求方法类型
        """
        return self.__rest_method

    def set_rest_method(self, method):
        """
        设置请求实例的REST请求方法类型
        :param method: 需要设置的REST请求方法类型
        """
        if method not in constants.REST_METHODS:
            raise exceptions.RequestException(
                "Invalid request method. The request method must be one of %s."
                % str(constants.REST_METHODS)
            )
        self.__rest_method = method

    def check_headers(self):
        """
        检查请求的查询参数是否设置完成
        """
        utils.check_params(self.get_params(), self.get_unnull_keys(), "header")

    def check_bodies(self):
        """
        检查请求消息体中的必填字段是否设置完成
        """
        utils.check_params(
            self.get_body_params(), self.get_unnull_body_keys(), "body"
        )

    def set_access_token(self, access_token):
        """
        设置请求实例的access_token
        :param access_token: 需要设置的access_token
        """
        self.__access_token = access_token
        new_headers = self.get_request_header()
        new_headers.update({constants.TOKEN_KEY_IN_HEADER: access_token})
        self.set_request_header(new_headers)

    def get_access_token(self):
        """
        获取请求实例中设置的access_token
        :return: string 请求实例中的access_token
        """
        return self.__access_token

    def check_token_need(self):
        """
        检查请求实例是否需要token验证
        :return: bool 检查结果
        """
        return self.__is_token_need

    def get_valid_path(self):
        """
        获取请求实例有效的url路径数组
        :return: list 有效的url路径数组
        """
        return self.__valid_path

    @classmethod
    def set_debug(cls, switch=True):
        """
        全局设置是否开启调试模式
        :param switch: bool 调试模式开关
        """
        welink.DEBUG = bool(switch)

    def _get_unescaped_mark(self):
        return self.__unescaped_mark

    def check_path(self):
        """
        检查请求实例的url路径是否有效
        """
        if self.get_path() not in self.get_valid_path():
            raise exceptions.RequestException(
                "Incorrect URL path. Use the correct path %s and try again. "
                % list(self.get_valid_path())
            )

    def get_curl_command(self):
        """
        获取请求实例发起接口调用时的模拟curl命令
        :return: string 请求实例发起接口调用时的模拟curl命令
        """
        cmd_command = "curl "

        if self.get_rest_method():
            cmd_command += "-X %s " % self.get_rest_method()

        bash_command = cmd_command
        cmd_command += '"' + self.split_join_url() + '" '
        bash_command += "'" + self.split_join_url() + "' "

        if self.get_request_header():
            for k, v in self.get_request_header().items():
                cmd_command += '-H "%s: %s" ' % (
                    utils.cmd_escape(k, self._get_unescaped_mark()),
                    utils.cmd_escape(v, self._get_unescaped_mark()),
                )
                bash_command += "-H '%s: %s' " % (
                    utils.bash_escape(k, self._get_unescaped_mark()),
                    utils.bash_escape(v, self._get_unescaped_mark()),
                )

        if self._get_body_params_for_curl():
            cmd_command += '-d "%s" ' % utils.cmd_escape(
                json.dumps(self._get_body_params_for_curl()),
                self._get_unescaped_mark(),
            )
            bash_command += "-d '%s' " % utils.bash_escape(
                json.dumps(self._get_body_params_for_curl()),
                self._get_unescaped_mark(),
            )

        curl_command = "Cmd: " + cmd_command[:-1]
        curl_command += "\n\nBash: " + bash_command[:-1]

        return curl_command

    def split_join_url(self):
        """
        拼接完整的url路径（携带请求实例中的查询参数）
        :return: string 完整的URL路径
        """
        url = self.get_protocol() + "://" + self.get_domain() + self.get_path()
        if self.get_params():
            url += "?" + parse.urlencode(self.get_params())

        return url

    def get_response(self, access_token="", timeout=30):
        """
        请求实例发起接口调用
        :param access_token: string 需要设置的access_token
        :param timeout: int 请求超时时间
        :return: string 接口响应的json字符串
        """
        self.check_path()

        if access_token:
            self.set_access_token(access_token)
        if self.check_token_need() and not self.get_access_token():
            raise exceptions.RequestException(
                "The access_token cannot be empty. "
                "You can invoke the set_access_token method "
                "or add the access_token parameter to set it. "
            )

        self.check_headers()
        path = self.get_protocol() + "://" + self.get_domain() + self.get_path()
        if self.get_params():
            path += "?" + parse.urlencode(self.get_params())

        body = json.dumps(self.get_body_params())

        if welink.DEBUG:
            print(self.get_curl_command() + "\n")

        print(self.get_rest_method(), path)
        req = request.Request(
            path,
            data=body.encode("utf-8"),
            headers=self.get_request_header(),
            method=self.get_rest_method(),
        )
        try:
            response = request.urlopen(req, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            response = e.read().decode()
        except Exception as e:
            print("urlopen error: ", e)
            response = "{}"

        try:
            result = json.loads(response)
        except Exception as e:
            print("json decode failed: ", e)
            result = response
        return result


class GetApiByUserInfo(RestApi):
    """
    请求参数为用户信息的GET接口基础对象
    """

    def __init__(self, url):
        super(GetApiByUserInfo, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = UserInfo()
        self.__params.type_in_data(super(GetApiByUserInfo, self).get_params())
        self.__valid_keys = (
            self.__params.user_id_key,
            self.__params.corp_user_id_key,
            self.__params.mobile_number_key,
        )

    @property
    def user_id(self):
        """
        string 特殊可选 用户帐号
        """
        return self.__params.user_id

    @user_id.setter
    def user_id(self, value):
        self.__params.user_id = value

    @user_id.deleter
    def user_id(self):
        del self.__params.user_id

    @property
    def mobile_number(self):
        """
        string 特殊可选 绑定的手机号码
        """
        return self.__params.mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self.__params.mobile_number = value

    @mobile_number.deleter
    def mobile_number(self):
        del self.__params.mobile_number

    @property
    def corp_user_id(self):
        """
        string 特殊可选 该用户在租户自身系统的登录标识，用于认证和邮箱登录（客户内唯一）
        """
        return self.__params.corp_user_id

    @corp_user_id.setter
    def corp_user_id(self, value):
        self.__params.corp_user_id = value

    @corp_user_id.deleter
    def corp_user_id(self):
        del self.__params.corp_user_id

    def get_rest_method(self):
        return self.__rest_method

    def get_params(self):
        return self.__params.get_data()

    def get_valid_keys(self):
        """
        获取请求实例中的可选参数关键字数组
        :return: list 可选参数关键字数组
        """
        return self.__valid_keys

    def reset_params(self):
        """
        清空请求实例中的查询参数
        """
        self.__params.clear()

    def unnull_check(self):
        """
        检查请求实例中的必填参数是否设置完成
        """
        self.__params.unnull_check()


class GetUserListByDepartment(RestApi):
    """
    根据部门信息查询人员列表的基础请求对象
    """

    def __init__(self, url):
        super(GetUserListByDepartment, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = super(GetUserListByDepartment, self).get_params()
        self.__dept_code_key = "deptCode"
        self.__page_number_key = "pageNo"
        self.__page_size_key = "pageSize"
        self.__unnull_keys = (self.__dept_code_key,)

    @property
    def dept_code(self):
        """
        string 必填 部门编码。从用户详细信息中获取部门编码
        """
        return self.__params.get(self.__dept_code_key)

    @dept_code.setter
    def dept_code(self, value):
        self.__params[self.__dept_code_key] = str(value)

    @property
    def page_number(self):
        """
        string 非必填 当前页数。默认为1
        """
        return self.__params.get(self.__page_number_key, "")

    @page_number.setter
    def page_number(self, value):
        utils.check_page(value, self.__page_number_key, "header")
        self.__params[self.__page_number_key] = str(value)

    @page_number.deleter
    def page_number(self):
        utils.del_param_from_dict(self.__params, self.__page_number_key)

    @property
    def page_size(self):
        """
        string 非必填 每页显示数量。默认为10（不能大于50）
        """
        return self.__params.get(self.__page_size_key, "")

    @page_size.setter
    def page_size(self, value):
        value = utils.integer_check(value, self.__page_size_key, "header")
        utils.attribute_bounds_check(
            value,
            constants.MIN_PAGE_SIZE,
            constants.MAX_PAGE_SIZE,
            self.__class__.__name__,
            self.__page_size_key,
        )
        self.__params[self.__page_size_key] = str(value)

    @page_size.deleter
    def page_size(self):
        utils.del_param_from_dict(self.__params, self.__page_size_key)

    def get_params(self):
        return copy.deepcopy(self.__params)

    def get_rest_method(self):
        return self.__rest_method

    def get_unnull_keys(self):
        return self.__unnull_keys


class GetApiUseDeptCode(RestApi):
    """
    通过部门编码发起GET请求的基础对象
    """

    def __init__(self, url):
        super(GetApiUseDeptCode, self).__init__(url)
        self.__rest_method = "GET"
        self.__params = DeptCode()
        self.__params.type_in_data(super(GetApiUseDeptCode, self).get_params())

    @property
    def dept_code(self):
        """
        string 必填 部门编码，从用户详细信息中获取部门编码
        """
        return self.__params.dept_code

    @dept_code.setter
    def dept_code(self, value):
        self.__params.dept_code = value

    def get_params(self):
        return self.__params.get_data()

    def get_rest_method(self):
        return self.__rest_method

    def unnull_check(self):
        """
        检查请求实例中的必填参数是否设置完成
        """
        self.__params.unnull_check("header")


class ParametersList(object):
    """
    数组类型参数对象
    """

    def __init__(self):
        self.item_class_obj = None
        self.__data = list()
        self.max_records_count = 0
        self.attr_name = ""

    def get_data(self):
        """
        获取参数内容
        :return: list 参数内容
        """
        return copy.deepcopy(self.__data)

    def get_param_by_index(self, index):
        """
        根据索引获取数组型参数指定位置的元素
        :param index: int 索引
        :return: 数组型参数指定索引位置的元素
        """
        try:
            return self.get_data()[index]
        except Exception as e:
            raise exceptions.ParameterException(e)

    def add_param(self, value):
        """
        向数组型参数中添加元素
        :param value: 需要添加的参数元素
        """
        utils.add_param_appoint_type(self.__data, value, self.item_class_obj)

    def set_param_by_index(self, value, index):
        """
        修改数组型参数指定位置的元素
        :param value: 需要修改的新的元素
        :param index: int 索引
        """
        utils.set_param_appoint_type_by_index(
            self.__data, value, index, self.item_class_obj
        )

    def del_param_by_index(self, index):
        """
        删除数组型参数指定索引位置的元素
        :param index: int 索引
        """
        utils.del_param_by_index(self.__data, index)
