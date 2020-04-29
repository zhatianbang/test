# coding:utf8

# 启动方法一
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="../lib/chromedriver.exe")
# driver.get("http://www.baidu.com")


# 启动方法二
from selenium.webdriver import *
import time
import os

option = ChromeOptions()  # 创建一个用来配置chrome属性的变量
option.add_argument('disable-infobars')  # 去掉提示条
# 获取用户目录，提升加载速度
userdir = os.environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data"
# option.add_argument(r'--user-data-dir=' + userdir)
driver = Chrome(executable_path="../lib/chromedriver",options=option)

