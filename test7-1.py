#!/bin/usr/python3

import time
import requests
import _thread

def print_time(threadName,delay):
	count = 0
	while count < 3:
		time.sleep(delay)
		count += 1
		print (threadName,time.ctime())

_thread.start_new_thread(print_time,('t1',1))
_thread.start_new_thread(print_time,('t2',2))
print ("Main Finished")
