# coding:utf8
from appium import webdriver
from common import logger
import traceback, time, os, threading
from appium.webdriver.common.touch_action import TouchAction


class APP():
    """
    这是APP自动化的关键字
    """

    def __init__(self, writer):
        self.driver = None
        self.t = 20
        self.port = '4723'
        self.writer = writer

    def runappium(self, path='', port='', t=''):
        '''
        启动appium服务
        :param path: 桌面版appium的安装路径,如C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium
        :param port: appium服务的启动端口
        :param t: appium启动等待时间
        :return:
        '''
        try:
            if path == '':
                cmd = 'node C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            else:
                cmd = 'node ' + path + '\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            if port == '':
                cmd += ' -p ' + self.port
            else:
                self.port = port
                cmd += ' -p ' + self.port
            if t == '':
                t = 5
            else:
                t = int(t)

            # 启动appium服务
            def run(cmd):
                try:
                    os.popen(cmd).read()
                except Exception as e:
                    pass

            th = threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(t)
            self.writer.write(self.writer.row, 7, "PASS")
            self.writer.write(self.writer.row, 8, "")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def runapp(self, caps, t=''):
        """
        连接appium服务器，并根据conf配置，启用待测试app
        :param conf: APP的启动配置，格式尽量为json格式字符串（尽量所有的值都用字符串，少用布尔值等其他格式）
        :return:
        """
        try:
            caps = eval(caps)
            if t == '':
                t = 20
            else:
                t = int(t)
            self.driver = webdriver.Remote("http://localhost:" + self.port + "/wd/hub", caps)
            self.driver.implicitly_wait(t)
            self.writer.write(self.writer.row, 7, "PASS")
            self.writer.write(self.writer.row, 8, "")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def __findele(self, path):
        """
        定位元素
        :param path:元素的定位路径，支持id,xpath, accessibility_id
        :return: 找到的元素，如未找到就返回None
        """
        ele = None
        try:
            if path.startswith("/"):
                # xpath定位
                ele = self.driver.find_element_by_xpath(path)
            # elif path.find(":id/")>0:  # 这种特殊情况下会有误判的可能
            else:
                try:
                    # 优先accessibility_id定位
                    self.driver.implicitly_wait(5)
                    ele = self.driver.find_element_by_accessibility_id(path)
                except:
                    # 其次id定位
                    # logger.error(str(traceback.format_exc()))
                    self.driver.implicitly_wait(self.t)
                    ele = self.driver.find_element_by_id(path)
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
        return ele

    def click(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
            self.writer.write(self.writer.row, 7, "FAIL")
        else:
            try:
                ele.click()
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def clear(self, path):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
        else:
            try:
                ele.clear()
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def input(self, path, text):
        ele = self.__findele(path)
        if ele is None:
            logger.error("No such element:" + path)
        else:
            try:
                ele.clear()
                ele.send_keys(text)
                self.writer.write(self.writer.row, 7, "PASS")
            except Exception as e:
                self.writer.write(self.writer.row, 7, "FAIL")
                self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def closeappium(self):
        try:
            os.system('taskkill /F /IM node.exe')
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def sleep(self,t=3):
        try:
            time.sleep(int(float(t)))
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def quit(self):
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def getsize(self):
        self.driver.get_window_size()

    def swipeup(self, n=1):
        '''定义向上滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    def swipedown(self, n=1):
        '''定义向下滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.9
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)

    def swipeleft(self, n=1):
        '''定义向左滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    def swiperight(self, n=1):
        '''定义向右滑动'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1)

    """TouchAction封装、暂时发现对部分元素容易出问题（如对微信，虽然实现了滑动，但是同时出现了长按导致出现【标记未读、置顶聊天、删除该聊天】这个小弹窗的问题，而swipe则较少出现这个问题）"""

    def touchdown(self):
        """向下滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width'] * 0.5
            height = size['height']
            TouchAction(self.driver).press(x=width, y=height * 0.2).move_to(x=width, y=height * 0.8).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchup(self):
        """向上滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width'] * 0.5
            height = size['height']
            TouchAction(self.driver).press(x=width, y=height * 0.8).move_to(x=width, y=height * 0.2).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchleft(self):
        """向左滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height'] * 0.5
            TouchAction(self.driver).press(x=width * 0.8, y=height).move_to(x=width * 0.2, y=height).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def touchright(self):
        """向右滑动"""
        try:
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height'] * 0.5
            TouchAction(self.driver).press(x=width * 0.2, y=height).move_to(x=width * 0.8, y=height).release().perform()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def resetinput(self):
        '''重置手机输入法'''
        try:
            def swipe_up(n=1):
                '''定义向上滑动'''
                size = driver.get_window_size()
                width = size['width']
                height = size['height']
                x1 = width * 0.5
                y1 = height * 0.9
                y2 = height * 0.25
                for i in range(n):
                    driver.swipe(x1, y1, x1, y2)

            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "8.0.0"
            caps["deviceName"] = "KWG5T16C29081222"
            caps["appPackage"] = "com.android.settings"
            caps["appActivity"] = ".HWSettings"
            caps["noReset"] = "true"
            # caps["unicodeKeyboard"] = "true"
            # caps["resetKeyboard"] = "true"
            driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            driver.implicitly_wait(10)
            swipe_up()
            try:
                driver.find_element_by_xpath('//*[contains(@text,"系统导航、系统更新、关于手机、语言和输入法")]').click()
            except:
                swipe_up()
                driver.find_element_by_xpath('//*[contains(@text,"系统导航、系统更新、关于手机、语言和输入法")]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[contains(@text,"语言和输入法")]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[contains(@text,"默认")]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[contains(@text,"百度输入法华为版")]').click()
            time.sleep(1)
            driver.quit()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
