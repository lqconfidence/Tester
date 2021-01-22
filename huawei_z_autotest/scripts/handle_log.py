import os
import logging

from scripts.handle_config import do_config
from scripts.constants import LOGS_DIR

class HandleLog:
    def __init__(self):
        # 定义日志收集器
        self.case_logger = logging.getLogger(do_config.get_value("log", "logger_name"))

        # 指定日志收集器的日志等级
        # NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
        self.case_logger.setLevel(do_config.get_value("log", "logger_level"))

        # 定义日志输出渠道
        # 输出到控制台
        console_handle = logging.StreamHandler()

        # 输出到文件
        file_handle = logging.FileHandler(os.path.join(LOGS_DIR, do_config.get_value("log", "log_filename")), encoding='utf-8')

        # 指定日志输出渠道的日志等级
        console_handle.setLevel(do_config.get_value("log", "console_level"))
        file_handle.setLevel(do_config.get_value("log", "file_level"))

        # 定义日志显示的格式
        simple_formatter = logging.Formatter(do_config.get_value("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(do_config.get_value("log", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)   #控制台显示简洁的日志
        file_handle.setFormatter(verbose_formatter)     #日志文件中显示详细日志

        # 对接，将日志收集器与输出渠道对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger

do_logger = HandleLog().get_logger()

if __name__ == '__main__':
    do_log = HandleLog()
    case_logger = do_log.get_logger()
    case_logger.debug("这是一个debug级别的日志")  # 手动记录日志
    case_logger.info("这是一个info级别的日志")
    case_logger.warning("这是一个warning级别的日志")
    case_logger.error("这是一个error级别的日志")
    case_logger.critical("这是一个critical级别的日志")