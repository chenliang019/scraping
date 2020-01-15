#!/usr/bin/python3

######pip3 install selenium######

from selenium import webdriver

f = webdriver.FirefoxProfile()
f.set_preference('permissions.default.stylesheet',2)

driver = webdriver.Firefox(firefox_profile = f,executable_path = r'C:\Program Files\Python37\Scripts\geckodriver.exe')
driver.get("http://c2b.brightoilonline.com")


