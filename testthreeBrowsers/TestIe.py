# coding:utf8

from selenium import webdriver

driver = webdriver.Ie(executable_path='../lib/IEDriver.exe')
driver.get("http://www.baidu.com")