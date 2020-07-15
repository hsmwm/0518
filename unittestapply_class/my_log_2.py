

import logging
from config.read_ini import conf

class MyLogger(logging.Logger):

    def __init__(self, file=None):
        super().__init__(conf.get('log','name'),conf.get('log','level'))

        #设置日志格式
        formt='%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter=logging.Formatter(formt)

        #控制台渠道输出
        handle1=logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)
        #文件渠道输出
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


if conf.getboolean('log','file_ok'):
    file_name=conf.get('log','file_name')
else:
    file_name=None
logger=MyLogger(file_name)
logger.info('配置log')