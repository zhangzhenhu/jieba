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
        self.convert_value = lambda x: x

    def __getitem__(self, item):
        return self.convert_value(self.__dict[get_key(item)])

    def __setitem__(self, key, value):
        self.__dict[get_key(key)] = str(value)

    def __iter__(self):
        return self.__dict.__iter__()

    def __contains__(self, item):
        return get_key(item) in self.__dict

    def __delitem__(self, key):

        self.__dict.__delitem__(key)

    def update(self, target_dict):
        for key, value in target_dict.iteritems():
            self.__setitem__(key, value)

    def get(self, k, d=None):
        return self.convert_value(self.__dict.get(get_key(k), d))

    def close(self):
        self.__dict.close()

    def _get_value(self, value):
        return value


if __name__ == "__main__":
    import sys
    import jieba

    freq_dict = Kvdict("word_freq.db")
    tag_dict = Kvdict("word_tag.db")
    jieba.dt.initialize()

    for k, v in jieba.dt.FREQ.iteritems():
        freq_dict[k] = v

    for k, v in jieba.dt.word_tag_tab.iteritems():
        tag_dict[k] = v
    jieba.dt.FREQ = freq_dict
    jieba.dt.word_tag_tab = tag_dict

    for line in sys.stdin:
        line = line.strip().split('\t')
        word = line[0]
        # freq_dict[word] = 1000000
        # tag_dict[word] = "n"
        jieba.dt.add_word(word,1000000,"n")

    freq_dict.close()
    tag_dict.close()
