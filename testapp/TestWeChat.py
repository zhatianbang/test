# coding:utf8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "KWG5T16C29081222"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 添加隐式等待
driver.implicitly_wait(10)

# el1 = driver.find_element_by_accessibility_id("微信")
# el1.click()
try:
    el2 = driver.find_element_by_id("com.tencent.mm:id/m6")
    el2.send_keys("12345")
    el3 = driver.find_element_by_id("com.tencent.mm:id/d0q")
    el3.click()
except:
    pass
time.sleep(5)
print("等待10秒结束")

# 我
# driver.find_element_by_id("com.tencent.mm:id/djv").click()
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/djv' and @text='我']").click()

# 设置
# driver.find_element_by_id("com.tencent.mm:id/dkm").click()
driver.find_element_by_xpath("//*[@resource-id='android:id/title' and @text='设置']").click()

# 向上滑动
time.sleep(1)
size = driver.get_window_size()
x = size['width']
y = size['height']
print("屏幕尺寸", x, y)

# 获取屏幕尺寸
x1 = int(x * 0.5)
y1 = int(y * 0.9)
y2 = int(x * 0.1)
driver.swipe(x1, y1, x1, y2, 500)

# 点击 退出
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/d8' and @text='退出']").click()

# 点击 退出登录
# driver.find_element_by_id("com.tencent.mm:id/mf").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/dc' and @text='退出登录']").click()

# 确认 退出
driver.find_element_by_id("com.tencent.mm:id/b47").click()

time.sleep(5)
# 退出app
driver.quit()
