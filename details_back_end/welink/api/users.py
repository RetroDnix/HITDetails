#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用户参数模块
Create on 2020-03-09
@author wecode@huawei.com
"""
import copy

from welink.api import constants, exceptions, utils


class UserDetail(object):
    """
    用户详情对象
    """

    def __init__(self):
        self.__corp_user_id_key = "corpUserId"
        self.__user_name_cn_key = "userNameCn"
        self.__user_name_en_key = "userNameEn"
        self.__sex_key = "sex"
        self.__mobile_number_key = "mobileNumber"
        self.__phone_number_key = "phoneNumber"
        self.__corp_dept_code_key = "corpDeptCode"
        self.__user_email_key = "userEmail"
        self.__land_line_number_key = "landlineNumber"
        self.__address_code_key = "addressCode"
        self.__corp_secretary_key = "corpSecretary"
        self.__is_open_account_key = "isOpenAccount"
        self.__address_key = "address"
        self.__remark_key = "remark"
        self.__valid_key = "valid"
        self.__unnull_keywords = []
        self.__is_hide_mobile_number_key = "isHideMobileNumber"
        self.__order_in_depts_key = "orderInDepts"
        self.__valid_check_map = {
            self.__sex_key: (constants.SEX_LIST, constants.SEX_TRANS),
            self.__is_open_account_key: (
                constants.IS_OPEN_ACCOUNT_LIST,
                constants.IS_OPEN_ACCOUNT_TRANS,
            ),
            self.__valid_key: (
                constants.IS_VALID_LIST,
                constants.IS_VALID_TRANS,
            ),
            self.__is_hide_mobile_number_key: (
                constants.IS_HIDE_MOBILE_NUMBER_LIST,
                constants.IS_HIDE_MOBILE_NUMBER_TRANS,
            ),
        }
        self.__bounds_check_map = {
            self.__order_in_depts_key: (
                constants.MIN_ORDER_IN_DEPT,
                constants.MAX_ORDER_IN_DEPT,
            )
        }
        self.__data = dict()

    @property
    def corp_user_id(self):
        """
        string 必填 该用户在租户自身系统的登录标识，用于认证和邮箱登录（客户内唯一）
        """
        return self.__data.get(self.__corp_user_id_key, "")

    @corp_user_id.setter
    def corp_user_id(self, value):
        self.__data[self.__corp_user_id_key] = str(value)

    @property
    def user_name_cn(self):
        """
        string 必填 人员中文名称
        """
        return self.__data.get(self.__user_name_cn_key, "")

    @user_name_cn.setter
    def user_name_cn(self, value):
        self.__data[self.__user_name_cn_key] = str(value)

    @property
    def user_name_en(self):
        """
        string 非必填 人员英文名称
        """
        return self.__data.get(self.__user_name_en_key, "")

    @user_name_en.setter
    def user_name_en(self, value):
        self.__data[self.__user_name_en_key] = str(value)

    @property
    def sex(self):
        """
        string 必填 性别。仅：M/F, M: 男, F: 女
        """
        return self.__data.get(self.__sex_key, "")

    @sex.setter
    def sex(self, value):
        sex = str(value)
        self.valid_check(self.__sex_key, sex)
        self.__data[self.__sex_key] = sex

    @property
    def mobile_number(self):
        """
        string 必填 绑定手机号码
        """
        return self.__data.get(self.__mobile_number_key, "")

    @mobile_number.setter
    def mobile_number(self, value):
        self.__data[self.__mobile_number_key] = str(value)

    @property
    def phone_number(self):
        """
        string 必填 手机号码
        """
        return self.__data.get(self.__phone_number_key, "")

    @phone_number.setter
    def phone_number(self, value):
        self.__data[self.__phone_number_key] = str(value)

    @property
    def corp_dept_code(self):
        """
        string 必填 客户侧部门唯一编码，请先完成部门信息同步，否则传递该字段，
               系统无法识别该用户的部门
        """
        return self.__data.get(self.__corp_dept_code_key, "")

    @corp_dept_code.setter
    def corp_dept_code(self, value):
        self.__data[self.__corp_dept_code_key] = str(value)

    @property
    def user_email(self):
        """
        string 非必填 邮箱
        """
        return self.__data.get(self.__user_email_key, "")

    @user_email.setter
    def user_email(self, value):
        self.__data[self.__user_email_key] = str(value)

    @property
    def land_line_number(self):
        """
        string 非必填 座机
        """
        return self.__data.get(self.__land_line_number_key, "")

    @land_line_number.setter
    def land_line_number(self, value):
        self.__data[self.__land_line_number_key] = str(value)

    @land_line_number.deleter
    def land_line_number(self):
        if self.__land_line_number_key in self.__data:
            del self.__data[self.__land_line_number_key]

    @property
    def address_code(self):
        """
        string 非必填 邮政编码
        """
        return self.__data.get(self.__address_code_key, "")

    @address_code.setter
    def address_code(self, value):
        self.__data[self.__address_code_key] = str(value)

    @address_code.deleter
    def address_code(self):
        if self.__address_code_key in self.__data:
            del self.__data[self.__address_code_key]

    @property
    def corp_secretary(self):
        """
        string 非必填 秘书。在导入用户时，如果秘书帐号还不存在，需要先维护秘书用户信息，
               再重新同步
        """
        return self.__data.get(self.__corp_secretary_key, "")

    @corp_secretary.setter
    def corp_secretary(self, value):
        self.__data[self.__corp_secretary_key] = str(value)

    @corp_secretary.deleter
    def corp_secretary(self):
        if self.__corp_secretary_key in self.__data:
            del self.__data[self.__corp_secretary_key]

    @property
    def is_open_account(self):
        """
        string 必填 “1”：表示开户，“0”：表示仅同步不开户
        """
        return self.__data.get(self.__is_open_account_key, "")

    @is_open_account.setter
    def is_open_account(self, value):
        value = str(value)
        self.valid_check(self.__is_open_account_key, value)
        self.__data[self.__is_open_account_key] = value

    @property
    def address(self):
        """
        string 非必填 办公位置信息
        """
        return self.__data.get(self.__address_key, "")

    @address.setter
    def address(self, value):
        self.__data[self.__address_key] = str(value)

    @address.deleter
    def address(self):
        if self.__address_key in self.__data:
            del self.__data[self.__address_key]

    @property
    def remark(self):
        """
        string 非必填 备注信息
        """
        return self.__data.get(self.__remark_key, "")

    @remark.setter
    def remark(self, value):
        self.__data[self.__remark_key] = str(value)

    @remark.deleter
    def remark(self):
        if self.__remark_key in self.__data:
            del self.__data[self.__remark_key]

    @property
    def valid(self):
        """
        string 必填 默认为"1", "0"表示该用户已被移除即销户
        """
        return self.__data.get(self.__valid_key, "")

    @valid.setter
    def valid(self, value):
        value = str(value)
        self.valid_check(self.__valid_key, value)
        self.__data[self.__valid_key] = value

    @property
    def is_hide_mobile_number(self):
        """
        string 非必填 是否隐藏手机号码。1:公开（默认）；2：隐藏
        """
        return self.__data.get(self.__is_hide_mobile_number_key, "")

    @is_hide_mobile_number.setter
    def is_hide_mobile_number(self, value):
        value = str(value)
        self.valid_check(self.__is_hide_mobile_number_key, value)
        self.__data[self.__is_hide_mobile_number_key] = value

    @is_hide_mobile_number.deleter
    def is_hide_mobile_number(self):
        if self.__is_hide_mobile_number_key in self.__data:
            del self.__data[self.__is_hide_mobile_number_key]

    @property
    def order_in_depts(self):
        """
        string 非必填 人员在所在部门内排序。取值范围：1~9999。按数值正序排列。默认为10000。
        """
        return self.__data.get(self.__order_in_depts_key, "")

    @order_in_depts.setter
    def order_in_depts(self, value):
        value = utils.integer_check(
            value,
            self.__order_in_depts_key,
            class_name=self.__class__.__name__,
        )
        self.bounds_check(self.__order_in_depts_key, value)
        self.__data[self.__order_in_depts_key] = str(value)

    @order_in_depts.deleter
    def order_in_depts(self):
        if self.__order_in_depts_key in self.__data:
            del self.__data[self.__order_in_depts_key]

    @property
    def valid_check_map(self):
        """
        dict 参数白名单字典
        """
        return copy.deepcopy(self.__valid_check_map)

    @property
    def bounds_check_map(self):
        """
        dict 参数取值界限字典
        """
        return copy.deepcopy(self.__bounds_check_map)

    def valid_check(self, key, value):
        """
        参数白名单校验
        :param key: string 需要校验的参数的关键字
        :param value: 需要校验的参数的值
        """
        if key in self.valid_check_map:
            utils.attribute_valid_check(
                self.valid_check_map[key][0],
                value,
                key,
                self.__class__.__name__,
                self.valid_check_map[key][1],
            )

    def bounds_check(self, key, value):
        """
        参数界限校验
        :param key: string 需要校验的参数的关键字
        :param value: 需要校验的参数的值
        """
        if key in self.bounds_check_map:
            utils.attribute_bounds_check(
                value,
                self.bounds_check_map[key][0],
                self.bounds_check_map[key][1],
                self.__class__.__name__,
                key,
            )

    def unnull_check(self):
        """
        校验用户详情参数实例中的必填字段是否设置完成
        """
        for key in self.__unnull_keywords:
            if key not in self.__data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )

    def get_data(self):
        """
        以dict的形式获取用户详情参数实例的内容
        """
        return copy.deepcopy(self.__data)


class UserInfo(object):
    """用户简单信息参数对象"""

    def __init__(self):
        self.user_id_key = "userId"
        self.mobile_number_key = "mobileNumber"
        self.corp_user_id_key = "corpUserId"
        self.user_email_key = "userEmail"
        self.__data = dict()
        self.__valid_keys = (
            self.user_id_key,
            self.mobile_number_key,
            self.user_email,
            self.corp_user_id_key,
        )

    @property
    def user_id(self):
        """
        string 特殊可选 用户账号
        """
        return self.__data.get(self.mobile_number_key, "")

    @user_id.setter
    def user_id(self, value):
        self.__data[self.user_id_key] = str(value)

    @user_id.deleter
    def user_id(self):
        if self.user_id_key in self.__data:
            del self.__data[self.user_id_key]

    @property
    def mobile_number(self):
        """
        string 特殊可选 绑定手机号码
        """
        return self.__data.get(self.mobile_number_key, "")

    @mobile_number.setter
    def mobile_number(self, value):
        self.__data[self.mobile_number_key] = str(value)

    @mobile_number.deleter
    def mobile_number(self):
        if self.mobile_number_key in self.__data:
            del self.__data[self.mobile_number_key]

    @property
    def corp_user_id(self):
        """
        string 特殊可选 该用户在租户自身系统的登录标识，用于认证和邮箱登录（客户内唯一）
        """
        return self.__data.get(self.corp_user_id_key, "")

    @corp_user_id.setter
    def corp_user_id(self, value):
        self.__data[self.corp_user_id_key] = str(value)

    @corp_user_id.deleter
    def corp_user_id(self):
        if self.corp_user_id_key in self.__data:
            del self.__data[self.corp_user_id_key]

    @property
    def user_email(self):
        """
        string 特殊可选 邮箱
        """
        return self.__data.get(self.user_email_key, "")

    @user_email.setter
    def user_email(self, value):
        self.__data[self.user_email_key] = str(value)

    @user_email.deleter
    def user_email(self):
        if self.user_email_key in self.__data:
            del self.__data[self.user_email_key]

    @property
    def valid_keys(self):
        """
        list 用户简单信息对象有效参数数组
        :return:
        """
        return self.__valid_keys

    def get_data(self):
        """
        以dict的形式获取用户简单信息实例的内容
        """
        return copy.deepcopy(self.__data)

    def type_in_data(self, data=None):
        """
        录入用户简单信息
        :param data: dict 用户简单信息
        """
        if not data:
            return
        if not isinstance(data, dict):
            raise exceptions.ParameterException(
                "The parameter type of the input data must be dict. "
            )
        for key in self.valid_keys:
            if key not in data:
                continue
            self.__data[key] = str(data[key])

    def clear(self):
        """清空用户简单信息实例中设置的参数"""
        self.__data.clear()

    def unnull_check(self):
        """校验用户简单信息中的必填字段是否设置完成"""
        valid_params = set(
            [pname for pname in self.__data if pname in self.valid_keys]
        )
        if not valid_params:
            raise exceptions.ParameterException(
                "The {} parameters cannot be all empty. ".format(
                    self.valid_keys
                )
            )
