# coding:utf8

from web.Web import Browser
import time

driver = Browser()
driver.openBrowser('chrome')
driver.get('http://112.74.191.10:8000/')


def login(driver):
    driver.click("//html/body/div[1]/div[1]/div/div/div/div[2]/a[1]")
    driver.input("//*[@id='username']",'13800138006')
    driver.input("//*[@id='password']",'123456')
    driver.input("//*[@id='verify_code']",'11111')
    driver.input("//*[@id='loginform']/div/div[6]/a")
    # driver.gettext('/html/body/div[1]/div/div/div/div[2].a[2]')
    if driver.text == '安全退出':
        print('pass')
    else:
        print('fail')

def userinfo(driver):
    print("测试PO模式")
login(driver)
driver.sleep(3)
driver.quit()
# 登录





