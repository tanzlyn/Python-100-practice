#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 2023.04.25.Tan
# 判断密码是否大于8位
def check_len(pwd):
    if len(pwd) >= 8:
        return True
    else:
        return False


#  检查密码是否有大小写字母，数字，其他字符组成
def check(pwd):
    check = [0, 0, 0, 0]
    for char in pwd:  # 遍历每一个密码字符
        if char.islower():
            check[0] = 1
        if char.isupper():
            check[1] = 1
        if char.isdigit():
            check[2] = 1
        if not (char.isalpha() | char.isdigit() | char.isspace()):
            check[3] = 1
    print(check)

    #  当列表中4个元素的值都是1，即各项之和是4，说明字符串符合条件（由大小写字母、数字、其他字符组成）
    #  如果小于4，则不全符合条件
    if sum(check) < 4:
        return False
    else:
        return True


#  判断字符串是否包含重复的、4位以上的子串
def check_rep(pwd):
    n = len(pwd)
    for i in range(n - 4):
        str1 = pwd[i:i + 4]
        str2 = pwd[i + 4::]
        if str1 in str2:
            return False
    return True


# 主函數
if __name__ == '__main__':
    meg = """
    1.密码必须由大小写字母，数字，其他字符组成
    2.密码长度必须是8位长
    3.重复不得包含长度为4的子串

    """
    print(meg)
    while True:
        pwd = input('请输入密码：')
        if pwd == 'q':
            print('退出程序。。。')
            break
        vcheck1 = check_len(pwd)
        if not vcheck1:
            print('密码长度不够')
            continue
        vcheck2 = check(pwd)
        if not vcheck2:
            print('密码不是由大小写字母，数字、其他字符组成、')
            continue
        vcheck3 = check_rep(pwd)
        if not vcheck3:
            print('密码含有2个以上重复子串')
            continue
        print('密码正确')
        break