#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自定义异常模块
Created on 2020-02-29
@author: wecode@huawei.com
"""


class TopException(Exception):
    def __init__(self):
        self.errcode = None
        self.errmsg = None
        self.application_host = None
        self.service_host = None

    def __str__(self):
        return (
            "errcode="
            + str(self.errcode)
            + " errmsg="
            + str(self.errmsg)
            + " application_host="
            + str(self.application_host)
            + " service_host="
            + str(self.service_host)
        )


class RequestException(Exception):
    pass


class ParameterException(Exception):
    pass
