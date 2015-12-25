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

import jieba
from jieba.kvdict import Kvdict



if __name__ == "__main__":

    freq_dict = Kvdict("word_freq.db")
    tag_dict = Kvdict("word_tag.db")
    jieba.dt.initialize()
    freq_dict.convert_value = lambda x: int(x)
    jieba.dt.FREQ = freq_dict
    from jieba import posseg as pg
    pg.initialize()
    pg.dt.word_tag_tab = tag_dict

    pg.cut("我爱北京天安门")



