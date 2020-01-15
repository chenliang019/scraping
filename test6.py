#!/usr/bin/python3
#coding=utf-8

################################
######pip3 install mysqlclient
################################

import requests
import lxml
from bs4 import BeautifulSoup
import MySQLdb

# conn = MySQLdb.connect(host='192.168.56.27',user='scraping',passwd='Pa626823@2019',db='scraping',charset='utf8')
# cur = conn.cursor()
# 
# cur.execute("insert into urls (url,content) values ('www.google.com','百度')")
# conn.commit()
# cur.close()

def get_page(link):
	headers = {
		'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
	r = requests.get(link,headers=headers)
	html = r.content
	html = html.decode('UTF-8')
	soup = BeautifulSoup(html,'lxml')
	return soup

def get_data(post_list):
	data_list = []
	for post in post_list:
		title_id = post.find('td',class_='p_title')
		title = title_td.find('a',id=True).text.strip()
		post_link = title_td.find('a',id=True)['href']
		post_link = 'https://bbs.hupu.com' + post_link
		
		author = post.find('td',class_='p_author').a.text.strip()
		author_page = post.find('td',class_='p_author').a['href']
		start_date = post.find('td',class_='p_author').contents[2]
		start_date = datetime.datetime.strptime(start_date,'%Y-%m-%d').date()
		
		reply_view = post.find('td',class_='p_re').text.strip()
		reply = reply_view.split('/')[0].strip()
		view = reply_view.split('/')[1].strip()
		
		data_list.append([title,post_link,author,author_page,start_date,reply,view])
		
	return data_list

link = "https://bbs.hupu.com/bxj"
soup = get_page(link)
post_list = soup.find_all('a',class_="truetit")
data_list = get_data(post_list)
for each in data_list:
	print (each)
	
		
