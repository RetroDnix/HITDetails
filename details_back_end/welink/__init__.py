#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request

DEBUG = False


def set_proxy(proxy_domain):
    """
    设置全局proxy
    :param proxy_domain: proxy域名 {username}:{password}@{domain}:{port}
    或者{domain}:{port}
    """
    proxy_handler = request.ProxyHandler(
        {"http": str(proxy_domain), "https": str(proxy_domain)}
    )
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)
