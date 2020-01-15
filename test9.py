#!/bin/usr/python3

import time
import multiprocessing

link_list = []	
with open(r'D:\CL\gittest\spider\alexa.txt','r',newline="",encoding='utf-8') as file:
	file_list = file.readlines()
	for each in file_list:
		link = each.split('\r')[0]
		link_list.append(link)
workQueue = multiprocessing.Queue(10000)
for url in link_list:
	workQueue.put(url)

def crawler(q):
	url = q.get(timeout=2)
	try:
		r = requests.get(url,timeout=5)
		print (q.qsize(),r.status_code,url)
	except Exception as e:
		print (q.qsize(),url,'Error: ',e)
		
class myProcess(multiprocessing.Process):
	def __init__(self,q):
		multiprocessing.context.Process.__init__(self)
		self.q = q
	def run(self):
		print ("Start......",self.pid)
		while not self.q.empty():
			crawler(self.q)
		print ("Exiting......",self.pid)

if __name__ == '__main__':
	for pName in range(1,5):
		p = myProcess(workQueue)
		p.daemon = True
		p.start()

