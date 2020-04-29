# coding:utf8
from threeBrowsers.Web import Browser


browser = Browser()

browser.openBrowser(browserType='ie')
browser.get("http://www.baidu.com")

browser.sleep(4)
browser.quit()