#!/bin/usr/python3

'''
每个线程从队列读取url访问，直至队列结束。
可以在range中自定义线程个数，range(1,101)为100个线程并行。
'''

import time
import requests
import threading
import queue as Queue

link_list = []	
with open(r'D:\CL\gittest\spider\alexa.txt','r',newline="",encoding='utf-8') as file:
	file_list = file.readlines()
    for each in file_list:
		link = each.split('\r')[0]
		link_list.append(link)
	
class myThread(threading.Thread):
	def __init__(self,name,queue):
		threading.Thread.__init__(self)
		self.name = name
		self.queue = queue
	def run(self):
		while True:
			try:
				crawler(self.name,self.queue)
			except:
				break

def crawler(threadName,q):
	url = q.get(timeout=2)
	try:
		r = requests.get(url,timeout=5)
		print (q.qsize(),threadName,r.status_code,url)
	except Exception as e:
		print (q.qsize(),threadName,url,'Error: ',e)

workQueue = Queue.Queue(10000)
for url in link_list:
	workQueue.put(url)

#threadList = ["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5"]		
threads = []

start = time.time()
#for tName in threadList:
for tName in range(1,101):
	thread = myThread("Thread-"+str(tName),workQueue)
	thread.start()
	threads.append(thread)

for t in threads:
	t.join()

end = time.time()

print ("均衡并行模式总时间：",end-start)