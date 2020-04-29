# -*- coding: UTF-8 -*-
import unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    # 查找unittest测试类
    test_suite = unittest.defaultTestLoader.discover('.', pattern='PramaTest.py')   # .表示当前脚本所在文件夹，
    # 调用BeautifulReport执行测试类：还是在使用unittest执行
    result = BeautifulReport(test_suite)
    result.report(filename='test.html', description='***系统web自动化测试报告', log_path='.')



