#!/usr/bin/python3

################################
######pip3 install requests######
######pip3 install bs4     ######
######pip3 install lxml    ######
######pip3 install selenium######
################################


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(firefox_path=r'C:\Program Files\Mozilla Firefox\firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps)
driver.get("http://www.santostang.com/2018/07/04/hello-world")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print (content.text)
