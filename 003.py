#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 2023.05.03.Tan
def passwd_pre(pwd):
    vert = []
    for char in pwd:
        if char in 'abc':
            char = '!'
        elif char in 'def':
            char = '@'
        elif char in 'ghi':
            char = '#'
        elif char in 'jkl':
            char = '$'
        elif char in 'mno':
            char = '%'
        elif char in 'pqr':
            char = '^'
        elif char in 'stu':
            char = '&'
        elif char in 'vwx':
            char = '*'
        elif char in 'yz':
            char = '('
        elif char in 'Z':
            char = 'a'
        elif char.isupper():
            # 对于大写字母，先转换成小写字母，然后转成16位数值并加1.
            # 最后转换为字母，即当前字母转换为下一个字母的小写形式。
            char = chr(ord(char.lower()) + 1)  # ASCII码值
            # A转换为a,ord把a转换为a的ASCII值为97，chr（98）把ASCII值转换为字母，即小写b.
            vert.append(char)
            print("vert:",vert)
            return ''.join(vert)  # 把列表中的各项连接成字符串并返回


def change_txt(pwd, str1, str2):
    vert = ''
    pwd = pwd.lower()
    for char in pwd:
        j = str1.find(char)  # 取得在str1中的索引值
        if j == -1:  # 在str1中没有该字符，就返回-1
            vert = vert + char  # 没有索引值就保留原字符
        else:
            vert = vert + str2[j]  # 找到索引值，根据这个索引值在str2中取得一个字符替换原字符
    return vert


def change_password(pwd):
    if pwd == None:
        return '-1'
    vert = ''
    vpre = passwd_pre(pwd)
    vlen = len(pwd)
    vstr = change_txt(pwd, "1234567890abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz1234567890")
    if vlen <= 4:
        vert = str(vpre) + vstr[0:vlen]
    else:
        vert = str(vpre) + vstr[0:4]
    return vert


if __name__ == '__main__':
    while True:
        pwd = input('请输入密码：')
        if pwd == 'q':
            print('退出程序')
            break
        else:
            pwdnew = change_password(pwd)
            print('密码是：', pwd, '加密后：', pwdnew)
