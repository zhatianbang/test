# coding:utf8
from selenium import webdriver

# 打开 Firefox 点右上角设置>？（帮助）>故障排除信息>显示文件夹/配置文件夹
profile_directory = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\chehrjce.default-release"
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile,executable_path="../lib/geckodriver.exe")
driver.get("http://www.baidu.com")
