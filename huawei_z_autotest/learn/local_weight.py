# -*-coding:utf-8 -*-
# @Time:2020/8/14 9:43
# @Author:a'nan
# @Email:934257271
# @File:code_provicy_detection_new_0323.py

# 读取所有txt文件
import os







# 隐私政策文件判定
import re
import jieba.analyse
import chardet


def clean_html(s):
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 匹配html中的br标签 ，换行
    re_h = re.compile('</?\w+[^>]*>')  # 匹配HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    blank_line = re.compile('\n+')  # 去掉多余的空行
    re_c = re.compile(r'\{.*?\}')  # 去掉大括号间内容
    re_c2 = re.compile(r'\{[^}]*\}')
    # re_b = re.compile(r'\s+')

    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_cdata.sub('', s)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = blank_line.sub('\n', s)  # 去掉多余的空行
    s = re_comment.sub('', s)  # 去掉HTML注释
    s = re_c.sub('', s)  # 去掉大括号间内容
    s = re_c2.sub('', s)
    s = blank_line.sub('\n', s)  # 去掉多余的空行
    # s = re_b.sub('', s)
    return s

def local_weigth_test(text):
    #text = text.encode('utf-8')
    # 关键词
    text = clean_html(text)
    print(text)
    sed_word_list = ['个人信息', '手机', '授权', '法律法规', '收集', '数据', '权限', '账户', '合法权益', '权利', '披露', '政策', '保障', '存储', '储存',
                     '条款', '身份验证', '服务器', '隐私权', '共享', 'cookie', 'Cookie', '身份认证', '儿童', '设备识别码', 'IP', 'GPS', 'IMEI',
                     '隐私', '隐私保护', '隐私声明', '隐私政策', '个人隐私']

    # 加载停用词和用户自定义词典
    stopwords = []
    with open(r'D:\\PycharmProjects\\stop_word.txt', encoding='utf-8', mode='r')as rd:
        for line in rd.readlines():
            stopwords.append(line.strip())
    jieba.load_userdict(r'D:\\PycharmProjects\\user_dict.txt')

    tf_idf_100 = []
    worf_tf = dict()
    count = 0
    count_ = 0
    result = ''
    try:
        if count % 500 == 0:
            print(count)
        count += 1
        write_ = False
        if len(text) > 0:
            tf_idf_100 = jieba.analyse.extract_tags(text.strip(), topK=100, withWeight=False, allowPOS=())
            if len(re.findall('隐私政策|隐私协议|隐私声明|隐私的声明|隐私服务协议|隐私条款|隐私申明|隐私权政策|隐私说明', text)) >= 1:
                count_ += 3
            if len(re.findall(
                    '隐私保护|使用条款|服务协议|法律申明|法律声明|免责声明|用户协议|法律效力|用户注册协议|用户服务协议|隐私信息保护|用户行为规范|用户使用协议|使用声明|注册协议|服务条款|安全条款',
                    text)) >= 1:
                count_ -= 3
            for se_w in sed_word_list:
                if se_w in tf_idf_100:
                    count_ += 1
            if count_ >= 7:
                write_ = True
            if write_:
                result = True
                return result
            else:
                result = False
                return result
    except Exception as e:
        print("本地算法异常为"+e)


if __name__ == "__main__":
    with open(r"D:\AntiyData\3df936ee1ca6629b0357d38a707be6f9.txt", encoding='utf-8', mode='r') as wo:
        text = wo.read()
    #print(text)

    res = local_weigth_test(text)
    print(res)

