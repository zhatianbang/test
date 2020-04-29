# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

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

# time.sleep(4)
driver.quit()