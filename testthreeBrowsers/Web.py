# coding:utf8

from selenium.webdriver import *
import time,os

# 用类封装打开浏览器的方法
class Browser():

    def __init__(self):
        # 保存打开的浏览器
        self.driver = None

    #定义打开浏览器的函数
    def openBrowser(self,browserType='gc',dir=None):


        if browserType == 'gc':
            if dir is None:
                dir = '../lib/chromedriver'
            option = ChromeOptions()  # 创建一个用来配置chrome属性的变量
            option.add_argument('disable-infobars')  # 去掉提示条
            # 获取用户目录，提升加载速度
            # userdir = os.environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data"
            # option.add_argument(r'--user-data-dir=' + userdir)
            self.driver = Chrome(executable_path="../lib/chromedriver.exe", options=option)
        elif browserType == 'ie':
            if dir is None:
                dir = '../lib/IEDriver.exe'
            self.driver = Ie(executable_path=dir)
        elif browserType=='ff':
            if dir is None:
                dir = '../lib/geckodriver.exe'
            self.driver = Firefox(executable_path="../lib/geckodriver.exe")


        else:
            print('暂未实现该浏览器')

    # 访问网站
    def get(self,url):
        self.driver.get(url)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    def sleep(self,t=3):
        time.sleep(t)

