import logging

from common.yaml_handler import myconf


class MyLogger(object):
    isinstance = None
    count = 0

    def __new__(cls, *args, **kwargs):
        mylog = logging.getLogger(myconf.get('loger', 'name'))
        mylog.setLevel(myconf.get('loger', 'log_level'))
        sh = logging.StreamHandler()
        sh.setLevel(myconf.get('loger', 's_level'))
        mylog.addHandler(sh)
        fh = logging.FileHandler(myconf.get('loger', 'file_path'), encoding='utf8')
        fh.setLevel(myconf.get('loger', 'f_level'))
        mylog.addHandler(fh)
        fmt = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        formatter = logging.Formatter(fmt)
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        mylog.removeFilter(fh)
        mylog.removeFilter(sh)

        return mylog


mylog = MyLogger()
if __name__ == '__main__':
    pass
