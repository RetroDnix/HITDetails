#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通用方法模块
Created on 2020-02-29
@author: wecode@huawei.com
"""
import datetime
import json
import re
import inspect

from welink.api import constants, exceptions


def check_params(params, unnull_params, keyword="header"):
    """
    校验参数字典中的必填字段是否设置完成
    :param params: dict 需要校验的参数字典
    :param unnull_params: list 参数字典中的必填字段数组
    :param keyword: string 参数所在位置标记
    """
    for param_name in unnull_params:
        if param_name not in params:
            raise exceptions.ParameterException(
                "The parameter [{}] in the request {} cannot be empty.".format(
                    param_name, keyword
                )
            )


def del_param_from_dict(params, keyword):
    """
    从参数字典中删除某个参数
    :param params: dict 待操作的参数字典
    :param keyword: string 需要删除的参数的关键字
    """
    if keyword in params:
        del params[keyword]


def add_param_appoint_type(params, value, class_obj):
    """
    向数组型参数中添加指定类型的元素
    :param params: list 待操作的数组型参数
    :param value: 需要添加的元素
    :param class_obj: type 指定的数据类型
    """
    type_check(value, class_obj)
    value.unnull_check()
    params.append(value.get_data())


def set_param_appoint_type_by_index(params, value, index, class_obj):
    """
    在数组型参数中指定索引位置添加指定类型的元素
    :param params: list 待操作的数组型参数
    :param value: 需要添加的元素
    :param index: int 指定的索引值
    :param class_obj: type 指定的数据类型
    """
    type_check(value, class_obj)
    value.unnull_check()
    try:
        params[index] = value.get_data()
    except Exception as e:
        raise exceptions.ParameterException(e)


def type_check(value, type_obj):
    """
    参数类型校验
    :param value: 需要校验的参数
    :param type_obj: type 需要校验的数据类型
    """
    if not isinstance(value, type_obj):
        raise exceptions.ParameterException(
            "The parameter type is incorrect. "
            "The parameter's type must be {}".format(type_obj.__name__)
        )


def del_param_by_index(params, index):
    """
    在数组型参数中删除指定索引位置的元素
    :param params: list 待操作的数组型参数
    :param index: int 指定的索引位置
    """
    try:
        del params[index]
    except Exception as e:
        raise exceptions.ParameterException(e)


def attribute_valid_check(scope, attribute, attr_name, class_name, translates):
    """
    参数白名单校验
    :param scope: list 需要校验的参数的白名单数组
    :param attribute: 需要校验的参数的值
    :param attr_name: string 需要校验的参数的关键字
    :param class_name: string 需要校验的参数所在的对象的名称
    :param translates: list 需要校验的参数的白名单对应的含义数组
    """

    def get_attribute_map(_scope, trans):
        return ", ".join(
            [
                '"{}"({})'.format(_scope[index], trans[index])
                for index in range(len(_scope))
            ]
        )

    if attribute not in scope:
        raise exceptions.ParameterException(
            "The [{}] attribute of {} must be one of [{}]".format(
                attr_name, class_name, get_attribute_map(scope, translates)
            )
        )


def attribute_bounds_check(
    attribute, min_boundary, max_boundary, class_name, attr_name
):
    """
    参数的取值界限校验
    :param attribute: 需要校验的参数的值
    :param min_boundary: 需要校验的参数取值范围的下限
    :param max_boundary: 需要校验的参数取值范围的上限
    :param class_name: string 需要校验的参数所在对象的名字
    :param attr_name: string 需要校验的参数的名称
    """
    if attribute < min_boundary or attribute > max_boundary:
        raise exceptions.ParameterException(
            "The attribute [{}] of {} must between {} and {}".format(
                attr_name, class_name, min_boundary, max_boundary
            )
        )


def check_page(value, attr_name, keyword):
    """
    校验列表查询时当前页参数的有效性
    :param value: 需要检查的参数的值
    :param attr_name: string 需要检查的参数的关键字
    :param keyword: string 需要检查的参数所在对象的名称
    """
    value = integer_check(value, attr_name, keyword)
    if value < constants.MIN_OFFSET:
        raise exceptions.ParameterException(
            "The value of [{}] in the request {} "
            "must be greater than {}.".format(
                attr_name, keyword, constants.MIN_OFFSET
            )
        )


def integer_check(value, attr_name, keyword="", class_name=""):
    """
    整形校验
    :param value: 需要校验的值
    :param attr_name: string 需要校验的参数的关键字
    :param keyword: string 需要校验的参数在请求实例中为位置（header/body）
    :param class_name: string 需要校验的关键字所在对象的名称
    :return int 转换成功的整形参数的值
    """
    content = ""
    if keyword:
        content = "request " + keyword
    elif class_name:
        content = class_name
    try:
        value = int(value)
    except Exception as e:
        raise exceptions.ParameterException(
            "The [{}] parameter in the {} "
            "must be an integer. error: {}".format(attr_name, content, e)
        )
    return value


def records_count_check(max_count, records_count, attr_name):
    """
    数组型参数长度校验
    :param max_count: int 需要校验的参数的长度限制
    :param records_count: int 需要校验的数组型参数的长度
    :param attr_name: string 需要校验的参数的关键字
    """
    if records_count > max_count:
        raise exceptions.ParameterException(
            "The number of {} must be less than {}. "
            "Currently, there are {} parameters.".format(
                attr_name, max_count, records_count
            )
        )


def bytes_length_check(max_length, value, attr_name):
    """
    校验字符串型参数的长度
    :param max_length: int 需要校验的参数的长度限制
    :param value: string 需要校验的参数的值
    :param attr_name: string 需要校验的参数的关键字
    """
    if len(value) > max_length:
        raise exceptions.ParameterException(
            "The length of the {} parameter cannot exceed {} bytes. ".format(
                attr_name, max_length
            )
        )


def bash_escape(value, unescaped_mark=""):
    """
    对Bash命令字符串中的特殊字符进行转义
    :param value: string 需要转义的字符串
    :param unescaped_mark: string 转义逃逸标记
    :return: string 转义之后的字符串
    """
    if not isinstance(value, str):
        return value
    if unescaped_mark:
        value = value.replace(unescaped_mark, "")
    return value.replace("'", "'\"'\"'")


def cmd_escape(value, unescaped_mark=""):
    """
    对Cmd命令字符串中的特殊字符进行转义
    :param value: string 需要转义的字符串
    :param unescaped_mark: string 转义逃逸标记
    :return: string 转义之后的字符串
    """
    if not isinstance(value, str):
        return value
    for c in constants.CMD_SPECIAL_CHAR_LIST:
        value = value.replace(c, "^" + c)
    value = value.replace("\\", "\\\\")
    if unescaped_mark:
        value = value.replace("%", "\\%")
        value = value.replace(unescaped_mark + "^", "")
    else:
        value = value.replace("%", "^%")
    value = value.replace('"', '\\"')
    value = value.replace("\\\\u", "\\u")
    return value


def add_unescaped_mark(value, mark):
    """
    为字符串添加转义逃逸标记
    :param value: string 待操作的字符串
    :param mark: string 转义逃逸标记
    :return: string 操作完成的字符串
    """
    for c in constants.CMD_SPECIAL_CHAR_LIST:
        value = value.replace(c, mark + c)
    return value


def is_json(myjson):
    """
    判断一个参数是否为json字符串
    :param myjson: string 需要检查的字符串
    :return: bool 检查结果
    """
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def bilingualism_check(value, class_obj):
    """
    检查某个参数是否为双语参数
    :param value: string 需要检查的参数
    :param class_obj: 需要检查的参数对应的双语对象
    :return: dict 进行双语转换后的字符串
    """
    if not is_json(value):
        return value
    value_obj = json.loads(value)
    new_value = class_obj()
    new_value.cn = value_obj.get(new_value.get_cn_key(), "")
    new_value.en = value_obj.get(new_value.get_en_key(), "")
    return json.dumps(new_value.get_data())


def datetime_format_check(value, datetime_format, attr_name):
    """
    检查时间字符串是否有效，并转换为datetime元组
    :param value: string 需要检查的参数
    :param datetime_format: string 时间参数的格式化字符串
    :param attr_name: string 需要检查的参数的关键字
    :return: datetime.datetime 转换后的datetime元组
    """
    try:
        value = datetime.datetime.strptime(value, datetime_format)
    except Exception as e:
        raise exceptions.ParameterException(
            "The parameter {} must be in the format of {}. error: {}".format(
                attr_name, datetime_format, e
            )
        )
    return value


def time_span_check(time_from, time_to, max_interval):
    """
    起止时间差校验
    :param time_from: datetime.datetime 起始时间
    :param time_to: datetime.datetime 截止时间
    :param max_interval: int 起止时间差最大界值
    """
    if (time_to - time_from).total_seconds() > max_interval:
        raise exceptions.ParameterException(
            "The time span must be shorter than {} hours.".format(
                max_interval / (60 * 60)
            )
        )


def translate_param_name(name):
    """
    返回变量的名字，并将下划线风格改为驼峰风格
    :param var: 要提取变量名的变量
    """
    if name is None:
        return ""
    name_list = name.split("_")
    if len(name_list) > 1:
        final_name_list = [name_list[0]]
        for s in name_list[1:]:
            final_name_list.append(s.title())
        return "".join(final_name_list)
    return name


def retrieve_name(var):
    """
    返回变量的名字
    :param var: 要提取变量名的变量
    :return: string
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for var_name, var_val in callers_local_vars:
        if var_val is var:
            return var_name


def string_re_check(value, re_str, attr_name):
    """
    字符串正则校验
    :param value: string 需要校验的字符串
    :param re_str: string 需要校验的正则表达式
    :param attr_name: string 需要校验的参数的关键字
    """
    pattern = re.compile(re_str)
    invalid_str_list = [s for s in pattern.split(value) if s]
    if invalid_str_list:
        raise exceptions.ParameterException(
            "These strings in the {} parameter are invalid: {}".format(
                attr_name, invalid_str_list
            )
        )


if __name__ == "__main__":
    string_re_check("example~", r"[0-9a-zA-Z]+", "")
