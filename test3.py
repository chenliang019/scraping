#!/usr/bin/python3

######pip3 install selenium######

from selenium import webdriver
import time

driver = webdriver.firefox.webdriver.WebDriver(executable_path = r'C:\Program Files\Python37\Scripts\geckodriver.exe')
driver.implicitly_wait(20)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)

for i in range(0,3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    load_more = driver.find_element_by_css_selector('button.page-btn ')
    print (load_more)
    #load_more = driver.find_elements_by_xpath(".//button[@data-page='2']")
    load_more.click()
    driver.switch_to.default_content()
    time.sleep(2)

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)

