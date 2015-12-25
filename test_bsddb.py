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
    jieba.dt.FREQ = freq_dict
    jieba.posseg.initialize()
    jieba.posseg.dt.word_tag_tab = tag_dict

    jieba.posseg.cut("我爱北京天安门")



