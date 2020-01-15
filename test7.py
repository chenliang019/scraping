#!/bin/usr/python3

import time
import requests
import _thread

def get_url(tN,delay):
	try:
		url = requests.get(tN,timeout=delay)
		print (url.status_code,tN)

	except Exception as e:
		print ('Error: ',e)

with open(r'D:\CL\gittest\spider\alexa2.txt','r',newline="",encoding='utf-8') as file:
	r = file.readlines()

link_list = []	
for each in r:
	link = each.split('\r')[0]
	link_list.append(link)

start = time.time()

for each in link_list:
	_thread.start_new_thread(get_url,(each,10))

end = time.time()

print ('串行总时间：',end-start)