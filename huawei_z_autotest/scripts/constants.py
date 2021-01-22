import os

# 获取项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件configs所在目录的路径
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR, 'testcase.conf')

# 日志文件所在目录路径
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# 测试报告所在目录路径
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

CASES_DIR = os.path.join(BASE_DIR, 'cases')

# 测试数据所在的目录路径
DATAS_DIR = os.path.join(BASE_DIR, 'datas')

# 测试数据excel文件的路径
TEST_DATAS_FILES_PATH = os.path.join(DATAS_DIR, 'hwz-case.xlsx')

pass