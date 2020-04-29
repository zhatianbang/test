#coding:utf8

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def visibility_element_located(self, location_type, locator_expression, *args):
#     """
#     判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0
#     :param location_type:
#     :param locator_expression:
#     :param args:
#     :return:
#     """
#     try:
#         element = self.wait.until(EC.visibility_of_element_located())
#         return element
#     except Exception as e:
#         pass
driver = webdriver.Chrome(executable_path='../lib/chromedriver')
driver.get('http://www.baidu.com')
xpath ='//*[@id="kw"]'
# WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((driver.find_element_by_xpath(xpath))))
res = WebDriverWait(driver,10).until(EC.title_is(u"百度一下，你就知道"))
print('1判断title,返回布尔值:',res)

res = WebDriverWait(driver,10).until(EC.title_contains(u"百度一下"))
print('2判断title,返回布尔值:',res)

res = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw')))
print('3判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement:',res)


def findElement(loctor):
    '''args: loctor 传元祖，如（"id","xx"）        '''
    element = WebDriverWait(driver,10,0.5).until(lambda x: x.find_element(By.XPATH,loctor))
    return element

loctor ='//*[@id="kw"]'
findElement(loctor).send_keys("123")


