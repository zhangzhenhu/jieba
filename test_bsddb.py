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
import sys


if __name__ == "__main__":

    freq_dict = Kvdict("word_freq.db")
    tag_dict = Kvdict("word_tag.db")
    jieba.dt.initialize()
    freq_dict.convert_value = lambda x: x if x is None else int(x)
    jieba.dt.FREQ = freq_dict
    from jieba import posseg as pg
    pg.initialize()
    pg.dt.word_tag_tab = tag_dict
    # import pdb
    # pdb.set_trace()
    pg.dt.add_word("上海电力股份有限公司",1000000,"n")
    for line in sys.stdin:
        line = line.strip()
        print line,jieba.dt.FREQ[line],
        for x, y in pg.cut(line.strip()):
            print (u"(%s,%s)" % (x, y)).encode("utf8"),
        print
    freq_dict.close()
    tag_dict.close()


