#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
部门信息参数模块
Create on 2020-03-09
@author wecode@huawei.com
"""
import copy
from welink.api import constants, exceptions, utils


class DeptCode(object):
    """
    部门编码对象
    """

    def __init__(self):
        self.__dep_code_key = "deptCode"
        self.__data = dict()
        self.__unnull_keys = (self.__dep_code_key,)
        self.__valid_keys = (self.__dep_code_key,)

    @property
    def dept_code(self):
        """
        string 必填 部门编码，从用户详细信息中获取部门编码
        """
        return self.__data.get(self.__dep_code_key, "")

    @dept_code.setter
    def dept_code(self, value):
        self.__data[self.__dep_code_key] = str(value)

    def get_data(self):
        """
        以dict形式获取部门编码实例的内容
        :return: dict 部门编码实例的内容
        """
        return copy.deepcopy(self.__data)

    def type_in_data(self, data=None):
        """
        录入部门编码
        :param data: dict 需要录入的信息
        """
        if not data:
            return
        if not isinstance(data, dict):
            raise exceptions.ParameterException(
                "The parameter type of the input data must be dict. "
            )
        for key in self.__valid_keys:
            if key not in data:
                continue
            self.__data[key] = str(data[key])

    def unnull_check(self, keyword=""):
        """
        检查部门编码实例中的必填字段是否设置完成
        :param keyword: string 需要检查的参数关键字
        """
        content = " of the request %s" % keyword if keyword else ""
        for key in self.__unnull_keys:
            if key not in self.__data:
                raise exceptions.ParameterException(
                    "The parameter [%s]%s cannot be empty" % (key, content)
                )


class DeptDetail(object):
    """
    部门详情对象
    """

    def __init__(self):
        self.__corp_dept_code_key = "corpDeptCode"
        self.__corp_parent_code_key = "corpParentCode"
        self.__dept_name_cn_key = "deptNameCn"
        self.__dept_name_en_key = "deptNameEn"
        self.__dept_level_key = "deptLevel"
        self.__manager_id_key = "managerId"
        self.__valid_key = "valid"
        self.__order_number_key = "orderNo"
        self.__visible_range_key = "visibleRange"
        self.__unnull_keys = (
            self.__corp_dept_code_key,
            self.__corp_parent_code_key,
            self.__dept_name_cn_key,
            self.__dept_name_en_key,
            self.__dept_level_key,
            self.__valid_key,
        )
        self.__valid_check_map = {
            self.__valid_key: (
                constants.IS_VALID_LIST,
                constants.IS_VALID_TRANS,
            ),
            self.__visible_range_key: (
                constants.VISIBLE_RANGE_LIST,
                constants.VISIBLE_RANGE_TRANS,
            ),
        }
        self.__bounds_check_map = {
            self.__order_number_key: (
                constants.MIN_DEPT_ORDER,
                constants.MAX_DEPT_ORDER,
            )
        }
        self.__data = dict()

    @property
    def corp_dept_code(self):
        """
        string 必填 客户侧部门唯一编码
        """
        return self.__data.get(self.__corp_dept_code_key, "")

    @corp_dept_code.setter
    def corp_dept_code(self, value):
        self.__data[self.__corp_dept_code_key] = str(value)

    @property
    def corp_parent_code(self):
        """
        string 必填 客户侧上一级部门编码。注意：同步1级部门时该字段值设置为“0”
        """
        return self.__data.get(self.__corp_parent_code_key, "")

    @corp_parent_code.setter
    def corp_parent_code(self, value):
        self.__data[self.__corp_parent_code_key] = str(value)

    @property
    def dept_name_cn(self):
        """
        string 必填 部门中文名称
        """
        return self.__data.get(self.__dept_name_cn_key, "")

    @dept_name_cn.setter
    def dept_name_cn(self, value):
        self.__data[self.__dept_name_cn_key] = str(value)

    @property
    def dept_name_en(self):
        """
        string 必填 部门英文名称
        """
        return self.__data.get(self.__dept_name_en_key, "")

    @dept_name_en.setter
    def dept_name_en(self, value):
        sex = str(value)
        self.__data[self.__dept_name_en_key] = sex

    @property
    def dept_level(self):
        """
        string 必填 部门级别。1：表示1级部门，2：表示二层部门，以此类推
        """
        return self.__data.get(self.__dept_level_key, "")

    @dept_level.setter
    def dept_level(self, value):
        value = utils.integer_check(
            value, self.__dept_level_key, class_name=self.__class__.__name__
        )
        if value < constants.MIN_DEPT_LEVEL:
            raise exceptions.ParameterException(
                "The attribute %s of %s must be greater than %s"
                % (
                    self.__order_number_key,
                    self.__class__.__name__,
                    constants.MIN_DEPT_LEVEL,
                )
            )
        self.__data[self.__dept_level_key] = str(value)

    @property
    def manager_id(self):
        """
        string 非必填 部门主管的ID
        """
        return self.__data.get(self.__manager_id_key, "")

    @manager_id.setter
    def manager_id(self, value):
        self.__data[self.__manager_id_key] = str(value)

    @manager_id.deleter
    def manager_id(self):
        if self.__manager_id_key in self.__data:
            del self.__data[self.__manager_id_key]

    @property
    def valid(self):
        """
        string 必填 部门状态。1：有效（有效根据是否存在corpDeptCode判断新增还是更新）；
               0：无效（无效表示已删除）
        """
        return self.__data.get(self.__valid_key, "")

    @valid.setter
    def valid(self, value):
        value = str(value)
        self.valid_check(self.__valid_key, value)
        self.__data[self.__valid_key] = value

    @property
    def order_no(self):
        """
        string 非必填 部门排序。取值范围：1~999。按数值正序排列。默认为1000。
        """
        return self.__data.get(self.__order_number_key, "")

    @order_no.setter
    def order_no(self, value):
        value = utils.integer_check(
            value, self.__order_number_key, self.__class__.__name__
        )
        self.bounds_check(self.__order_number_key, value)
        self.__data[self.__order_number_key] = str(value)

    @order_no.deleter
    def order_no(self):
        if self.__order_number_key in self.__data:
            del self.__data[self.__order_number_key]

    @property
    def visible_range(self):
        """
        int 非必填 部门可见权限标记
        """
        return self.__data.get(self.__visible_range_key, "")

    @visible_range.setter
    def visible_range(self, value):
        value = str(value)
        self.valid_check(self.__visible_range_key, value)
        self.__data[self.__visible_range_key] = value

    @visible_range.deleter
    def visible_range(self):
        if self.__visible_range_key in self.__data:
            del self.__data[self.__visible_range_key]

    @property
    def bounds_check_map(self):
        """
        参数取值边界字典
        """
        return copy.deepcopy(self.__bounds_check_map)

    @property
    def valid_check_map(self):
        """
        参数白名单字典
        """
        return copy.deepcopy(self.__valid_check_map)

    def bounds_check(self, key, value):
        """
        检查参数取值是否超过限定范围
        :param key: 需要检查的参数关键字
        :param value: 需要检查的参数的值
        """
        if key in self.bounds_check_map:
            utils.attribute_bounds_check(
                value,
                self.bounds_check_map[key][0],
                self.bounds_check_map[key][1],
                self.__class__.__name__,
                key,
            )

    def valid_check(self, key, value):
        """
        检查参数的值是否在白名单内
        :param key: 需要检查的参数关键字
        :param value: 需要检查的参数的值
        """
        pass

    def unnull_check(self):
        """
        检查部门详情实例中的关键字是否设置完成
        """
        for key in self.__unnull_keys:
            if key not in self.__data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )
        if self.dept_level == "1" and self.corp_parent_code != "0":
            raise exceptions.ParameterException(
                "The corpParentCode parameter must be set to 0 "
                "when level-1 departments are synchronized. "
            )

    def get_data(self):
        """
        以dict的形式获取部门详细信息实例的内容
        :return: dict 部门详细信息实例的内容
        """
        return copy.deepcopy(self.__data)


class CorpDeptCode(object):
    """
    客户侧部门唯一编码对象
    """

    def __init__(self):
        self.__corp_dept_code_key = "corpDeptCode"
        self.__unnull_keys = (self.__corp_dept_code_key,)
        self.__valid_keys = (self.__corp_dept_code_key,)
        self.__data = dict()

    @property
    def corp_dept_code(self):
        """
        string 必填 客户侧部门唯一编码
        """
        return self.__data.get(self.__corp_dept_code_key, "")

    @corp_dept_code.setter
    def corp_dept_code(self, value):
        self.__data[self.__corp_dept_code_key] = str(value)

    def get_data(self):
        """
        以dict的形式获取客户侧部门唯一编码实例的内容
        :return: dict 客户侧部门唯一编码实例的内容
        """
        return copy.deepcopy(self.__data)

    def unnull_check(self):
        """
        检查客户侧部门唯一编码实例中的必填字段是否设置文昌
        """
        for key in self.__unnull_keys:
            if key not in self.__data:
                raise exceptions.ParameterException(
                    "The parameter [%s] cannot be empty" % key
                )
