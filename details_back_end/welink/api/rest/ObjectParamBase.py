#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wecode@huawei.com
"""
from welink.api import utils


class ObjectParamBase(object):
    def get_data(self):
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params
