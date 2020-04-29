# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time,os,threading

def run():
    cmd ='node C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js -p 4723'
    os.system(cmd)
th = threading.Thread(target=run,args=())
th.start()
time.sleep(10)

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "KWG5T16C29081222"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = "true"
caps["unicodeKeyboard"] = "true"
caps["resetKeyboard"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)

# 点击登录
# el1 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
# el1.click()

# 输入用户名
# el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
# # el2.clear()
# # el2.send_keys("120517972")
# #
# # # 输入密码
# # el3 = driver.find_element_by_accessibility_id("密码 安全")
# # el3.clear()
# # el3.send_keys("dkjdkj1990qq")

# 点击登录
el4 = driver.find_element_by_accessibility_id("登 录")
el4.click()

# 账户及设置

driver.find_element_by_accessibility_id("帐户及设置").click()

# 设置
driver.find_element_by_accessibility_id("设置").click()

# 账号管理
driver.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()

# 退出当前账号
driver.find_element_by_accessibility_id("退出当前帐号按钮").click()
#确定
driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()

driver.quit()



def close_appium():
    try:
        os.system('taskkill /F /IM node.exe')
    except Exception as e:
        pass

close_appium()
