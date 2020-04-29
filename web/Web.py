# coding:utf8

from selenium.webdriver import *
import time,os
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

# 用类封装打开浏览器的方法
class Browser():

    def __init__(self,writer):
        # 保存打开的浏览器
        self.writer = writer
        self.driver = None
        self.text = '' # 断言时会用到
        self.title = ''
        self.jsres = '' # 执行js后的返回值

    #定义打开浏览器的函数
    def openbrowser(self,browserType='gc',dir=None):


        if browserType == 'gc' or browserType=='chrome' or browserType == '' or browserType == None:
            if dir is None or dir == '':
                dir = './lib/chromedriver'
            option = ChromeOptions()  # 创建一个用来配置chrome属性的变量
            option.add_argument('disable-infobars')  # 去掉提示条
            # 获取用户目录，提升加载速度
            # userdir = os.environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data"
            # option.add_argument(r'--user-data-dir=' + userdir)
            self.driver = Chrome(executable_path=dir, options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
        elif browserType == 'ie':
            if dir is None or dir == '':
                dir = './lib/IEDriver.exe'
            self.driver = Ie(executable_path=dir)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.writer.write(self.writer.row, 7, 'PASS')
        elif browserType=='ff':
            if dir is None or dir == '':
                dir = './lib/geckodriver.exe'
            self.driver = Firefox(executable_path=dir)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            self.writer.write(self.writer.row, 7, 'PASS')
        else:
            print('暂未实现该浏览器')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '暂未实现该浏览器')

    # 访问网站
    def get(self,url):
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, 7, 'PASS')
            # self.writer.write(self.writer.row, 8, 'url')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)

    def click(self,xpath):
        try:
            ele = self.__find_element(xpath)
            ele.click()
            self.writer.write(self.writer.row, 7, 'PASS')
            # self.writer.write(self.writer.row, 8, 'xpath')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)


    def clear(self,xpath):
        try:
            ele = self.__find_element(xpath)
            ele.clear()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)

    def input(self,xpath,value):
        try:
            ele = self.__find_element(xpath)
            ele.clear()
            ele.send_keys(value)
            # self.find_element(xpath).send_keys(value)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, e)



    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    def sleep(self,t=3):
        try:
            time.sleep(int(float(t)))
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row,8, e)

    def gettext(self,xpath):
        self.text = self.__find_element(xpath).text

    def intoiframe(self,xpath):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))

    def outiframe(self):
        self.driver.switch_to.default_content()

    def gettitle(self):
        self.title = self.driver.title


    def switchwindow(self,index=0):
        """切换到指定下标的窗口"""
        print(self.driver.window_handles)
        h = self.driver.window_handles
        self.driver.switch_to.window(h[int(index)])

    def assertequals(self,act,value):
        try:
            act = act.replace('{text}',self.text)
            act = act.replace('{jsres}',self.jsres)
            act = act.replace('{title}',self.title)
            if str(act) == value:
                self.writer.write(self.writer.row, 7, 'PASS')
            else:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, str(act))
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))



    def quitbrowser(self):
        """退出驱动关闭所有窗口"""
        self.driver.quit()

    def closecurrentwindow(self):
        # 关闭selenium当前定位的窗口
        self.driver.close()

    # 滚动到指定元素（适合元素可见可定位，否则使用js滚动）
    def moveto(self,xpath):
        actions = ActionChains(self.driver)
        ele = self.__find_element(xpath)
        actions.move_to_element(ele).perform()

    def executejs(self,js):
        self.driver.execute_script(js)

    def elementisdisplay(self, element):
        flag = element.is_displayed()
        if flag == True:
            return element
        else:
            return False

    def forward(self):
        """浏览器前进按钮"""
        self.driver.forward()
    def back(self):
        """浏览器后退按钮"""
        self.driver.back()


    def refreshf5(self):
        '''强制刷新'''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()

    # def find_element(self,xpath):
    #     logger.info("测试")
    #     self.find_element(xpath)

    def savepng(self):
        """保存到项目根目录下的Screenshots下"""
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        now_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + now_time + '.png'
        self.driver.get_screenshot_as_file(screen_name)


    def runjsclick(self,xpath):
        try:
            button = self.__find_element(xpath)
            self.driver.execute_script("$(arguments[0]).click()", button)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            # logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(e))

    def __find_element(self,xpath):
        try:
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, xpath))
            return element
        except Exception as e:
            logger.exception(str(traceback.format_exc()))