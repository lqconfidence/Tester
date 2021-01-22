from configparser import ConfigParser
from scripts.constants import CONFIGS_FILE_PATH

class HandleConfig:
    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding='utf-8')

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        return eval(self.config.get(section, option))

    @staticmethod
    def write_config(datas, filename):
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return "数据不合法，应为嵌套字典的字典"

            config = ConfigParser()
            for key in datas:
                config[key] = datas[key]
            with open(filename, "w") as file:
                config.write(file)

do_config = HandleConfig(CONFIGS_FILE_PATH)

if __name__ == '__main__':
    pass