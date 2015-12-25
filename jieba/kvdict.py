#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
模块用途描述

Authors: zhangzhenhu(zhangzhenhu@baidu.com)
Date:    2015/12/20 16:56
"""
import bsddb3


def get_key(key):
    if isinstance(key, unicode):
        return key.encode("UTF-8")
    return str(key)


class Kvdict:
    def __init__(self, dict_file="word_dict.db"):
        self.__dict = bsddb3.hashopen(dict_file)

    def __getitem__(self, item, vtype=int):
        return vtype(self.__dict[str(item)])

    def __setitem__(self, key, value):
        self.__dict[get_key(key)] = str(value)

    def __iter__(self):
        return self.__dict.__iter__()

    def __contains__(self, item):

        return get_key(item) in self.__dict

    def update(self, target_dict):
        for key, value in target_dict.iteritems():
            self.__setitem__(key, value)

    def get(self, k, d=None):
        return self.__dict.get(get_key(k), d)

    def close(self):
        self.__dict.close()
