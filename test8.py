#!/usr/bin/python3

import threading
import time

def print_time(threadName,delay):
	count = 0
	while count < 3:
		time.sleep(delay)
		count += 1
		print (threadName,time.ctime())

class MyThread(threading.Thread):
    def __init__(self,name,delay):
            threading.Thread.__init__(self)
            self.name = name
            self.delay = delay
    def run(self):
            print ("starting->>>>>>" + self.name)
            print_time(self.name,self.delay)
            print ("Exiting->>>>>>" + self.name )

thread1 = MyThread("td1",3)
thread2 = MyThread("td2",3)

thread1.start()
thread2.start()

threads = []
threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()
	print (t)

print ("Exiting Main Thread")