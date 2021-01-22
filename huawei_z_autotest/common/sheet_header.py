# -*-coding:utf-8 -*-
# @Time:2020/7/8 16:02
# @Author:a'nan
# @Email:934257271
# @File:sheet_header.py


class SheetHeader:
    def __init__(self, head_data):
        for i in range(len(head_data)):
            self.__setattr__(head_data[i], i+1)



if __name__ == "__main__":
    a = SheetHeader(['2','333',"aaaaaaaa","dddddd","234234233"])
    b = a.__dict__
    print(a.__dict__)
    print(b.values())
    print(b.keys())
    for i in b.values():
        print(i)
    print(type(a), a)