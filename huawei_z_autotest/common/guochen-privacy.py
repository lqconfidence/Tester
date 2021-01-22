# -*-coding:utf-8 -*-
# @Time:2020/6/12 15:10
# @Author:a'nan
# @Email:934257271
# @File:guochen-privacy.py

# 读取所有txt文件
import os


def get_files(fload_path, files_list):
    f_list = os.listdir(fload_path)
    for file_name in f_list:
        f_path = os.path.join(fload_path, file_name)
        if os.path.isdir(f_path):
            get_files(f_path, files_list)
        else:
            # if f_path.split('.')[-1]=='html':
            files_list.append(f_path)
    return files_list


files_list = []
data_path = r'E:\工作\华为Z隐私合规\隐私-服务协议-李柯言\服务协议'
files_list = get_files(data_path, files_list)


# 清洗HTML文件
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


# 隐私政策文件判定
import re
import jieba.analyse

# 关键词
sed_word_list = ['个人信息', '信息', '服务', '手机', '授权', '隐私', '隐私政策', '法律法规', '收集', '数据',
                 '权限', '账户', '合法权益', '权利', '披露', '政策', '保障', '存储', '储存', '条款', '身份验证', '合法', '法律责任', '服务器',
                 '隐私权']

# 加载停用词和用户自定义词典
stopwords = []
with open(r'E:\工作\华为Z隐私合规\隐私-服务协议-李柯言\stop_word.txt', encoding='utf-8', mode='r')as rd:
    for line in rd.readlines():
        stopwords.append(line.strip())
# jieba.load_userdict(r'F:\Project\隐私检测\data\user_dict.txt')

tf_idf_100 = []
worf_tf = dict()
count = 0
for file_path in files_list:
    try:
        if count % 500 == 0:
            print(count)
        count += 1
        write_ = False
        with open(file_path, encoding='utf-8', mode='r')as rd:
            count_ = 0
            text = rd.read()
            #print("文本内容为{}".format(text))
            if file_path.split('.')[-1] == 'html':
                text = clean_html(text)
            if len(text) > 0:
                tf_idf_100 = jieba.analyse.extract_tags(text.strip(), topK=100, withWeight=False, allowPOS=())
                if len(re.findall('隐私政策|隐私协议|隐私声明|隐私的声明|隐私服务协议|隐私条款|隐私申明|隐私权政策|隐私说明', text)) >= 1:
                    count_ += 3
                if len(re.findall(
                        '隐私保护|使用条款|服务协议|法律申明|知识产权|法律声明|免责声明|用户协议|法律效力|用户注册协议|隐私权保护|用户服务协议|隐私信息保护|用户行为规范|用户使用协议|使用声明|服务协议|注册协议|服务条款|安全条款',
                        text)) >= 1:
                    count_ -= 3
                for se_w in sed_word_list:
                    if se_w in tf_idf_100:
                        count_ += 1
                if count_ >=8:
                    write_ = True
                if write_:
                    with open('E:\\工作\\华为Z隐私合规\\隐私-服务协议-李柯言\\is_privacy_fuwu\\' + file_path.split('\\')[-1],
                              encoding='utf-8', mode='a+')as wt:
                        wt.write(text)
                else:
                    with open('E:\\工作\\华为Z隐私合规\\隐私-服务协议-李柯言\\is_not_privacy_fuwu\\' + file_path.split('\\')[-1],
                              encoding='utf-8', mode='a+')as wt2:
                        wt2.write(text)
    except Exception as e:
        print('错误{},文件{}'.format(e, file_path))
