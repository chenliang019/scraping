#!/bin/usr/python3

import time
import requests
import _thread

def get_url(tN,delay):
	url = requests.get(tN,timeout=delay)
	print (url.status_code,tN)

with open(r'D:\CL\gittest\spider\alexa2.txt','r',newline="",encoding='utf-8') as file:
	r = file.readlines()

link_list = []	
for each in r:
	link = each.split('\r')[0]
	link_list.append(link)

start = time.time()

for each in link_list:
	try:
		_thread.start_new_thread(get_url,(each,10))
		
	except Exception as e:
		print ('Error: ',e)

end = time.time()

print ('串行总时间：',end-start)