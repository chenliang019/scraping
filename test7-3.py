#!/bin/usr/python3

'''
逐个访问列表中的url，返回状态码
'''

import time
import requests
import _thread



with open(r'D:\CL\gittest\spider\alexa.txt','r',newline="",encoding='utf-8') as file:
	r = file.readlines()

link_list = []	
for each in r:
	link = each.split('\r')[0]
	link_list.append(link)

start = time.time()

for eachlink in link_list:
	try:
		url = requests.get(eachlink,timeout=5)
		print (url.status_code,eachlink)

	except Exception as e:
		print ('Error: ',e)

end = time.time()

print ('串行总时间：',end-start)