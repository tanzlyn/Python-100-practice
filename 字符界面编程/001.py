#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 2023.04.24.Tan
import re
def get_char(txt):  # 定义分词函数
    vlist = re.split('[,;:."\s]\s*', txt)  # 依据分词符用split函数分词
    print("分词结果：",vlist)
    vdic_frequency = dict()  # 创建一个字典
    print("所有单词词频（空的）：",vdic_frequency)
    for vchar in vlist:  # 遍历所有字符，并统计字符出现的个数
        if vchar in vdic_frequency:  # 判断是否在字典中
            vdic_frequency[vchar] += 1
            #如果在字典中，则次数加1
        else:
            vdic_frequency[vchar] = 1
            #不在字典中，说明第一次出现，次数为1
    print("所有单词词频：",vdic_frequency)
    vdic_sort = sorted(vdic_frequency.items(), key=lambda item: item[1],
                       reverse=True)  # 排序.items()将字典转化为列表中元组的形式，lambda对item进行操作，item[0]表示键名，item【1】表示键值，这里排序依据是键值。逆序排序
    return vdic_sort


if __name__ == '__main__':
    with open('E:\python100\dataset\\read.txt', 'r') as f:  # \t表示转义字符，\\t才能读取地址
        vtext = f.read()
    vstr = get_char(vtext)
    print("排序之后的词频结果：",vstr)