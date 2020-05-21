import logging

# 实例化loginer对象
logger = logging.getLogger('cms')

# 设置文件级别
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 创建一个handler。用于输出到控制台
console = logging.StreamHandler()
console
logger.addHandler(console)
logger.debug('teste')

console.close()
logger.removeHandler(console)
