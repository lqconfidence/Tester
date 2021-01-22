import re

from bs4 import BeautifulSoup


# 处理输入的隐私政策
class TextHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def clean_html_custom(self):
        html_result = open(self.file_path, 'r', encoding="utf-8")
        text_result = BeautifulSoup(html_result, 'lxml').get_text()
        new_word = "".join((re.sub("\n", " ", text_result)).split(" "))
        # print("ssssssssssssssssssssss" + new_word)
        # fh = open('./zeng123.txt', 'w', encoding='utf-8')
        # fh.write(new_word)
        # fh.close()
        return new_word


# text_handler = TextHandler(r'C:\Users\Tsang\Desktop\隐私政策.txt')
# text_handler.clean_html_custom()
# if __name__ == "__main__":
#     result = TextHandler(
#         r'C:\Users\zeng\Desktop\HW_Z_Project\筛选是否为隐私政策\100\输入的100样本\隐私政策\privacy.html').clean_html_custom()
#     time1 = time.localtime()
#     print(time.strftime("%Y-%m-%d %H:%M:%S", time1))

# print(result)

# if __name__ == '__main__':
#     main()
