import unittest
import os
import HTMLTestRunner
import time


def allTest():
    suite = unittest.TestLoader().discover(

        start_dir=os.path.join(os.path.dirname(__file__),'case'),  # 当前地址
        pattern='test_*',  # 文件类型
        top_level_dir=None)
    return suite


def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))


def run():
    fp = os.path.join(os.path.dirname(__file__), 'result', getNowTime() + 'testReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp, 'wb'),
        title='自动化测试报告',
        description='自动化测试报告详细信息').run(allTest())



if __name__ == '__main__':
    run()
    
