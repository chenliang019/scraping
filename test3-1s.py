#!/usr/bin/python3

from selenium import webdriver
import time

def Fetch_Data():
    comments = driver.find_elements_by_css_selector('div.review-short')
    for eachcomment in comments:
        content = eachcomment.find_element_by_tag_name('div')
        print (content.text) 

driver = webdriver.firefox.webdriver.WebDriver(executable_path = r'C:\Program Files\Python37\Scripts\geckodriver.exe')
driver.implicitly_wait(20)
driver.get("https://movie.douban.com/subject/3097572/reviews")
time.sleep(5)

Fetch_Data()

for i in range(0,1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    load_more = driver.find_element_by_css_selector('span.next')
    load_more.click()
    time.sleep(2)
    Fetch_Data()