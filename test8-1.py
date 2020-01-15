#!/bin/usr/python3

'''
使用六个线程并行访问url，预先将列表中的url分配给指定线程上，线程完成自己的任务即退出。
'''

import time
import requests
import threading

with open(r'D:\CL\gittest\spider\alexa.txt','r',newline="",encoding='utf-8') as file:
	r = file.readlines()

link_list = []	
for each in r:
	link = each.split('\r')[0]
	link_list.append(link)


class myThread(threading.Thread):
    def __init__(self,name,link_range):
            threading.Thread.__init__(self)
            self.name = name
            self.link_range = link_range
    def run(self):
            crawler(self.name,self.link_range)


def crawler(threadName,link_range):
	for i in range(link_range[0],link_range[1]+1):
		try:
			url = requests.get(link_list[i],timeout=5)
			print (threadName,url.status_code,link_list[i])
		except Exception as e:
			print (threadName,'Error: ',e)


thread_list = []
link_range_list = [(0,200),(201,400),(401,600),(601,800),(801,1000)]

start = time.time()

for i in range(1,6):
	thread = myThread("Thread-"+str(i),link_range_list[i-1])
	thread.start()
	thread_list.append(thread)

for t in thread_list:
	t.join()

end = time.time()

print ("并行总时间：",end-start)

