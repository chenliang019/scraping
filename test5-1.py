#!/usr/bin/python3
# coding=gbk

import csv

div_list = ['������','�й���','�ձ���']
div_list2 = ["order","plugins"]

with open(r'D:\CL\gittest\spider\test.csv','a+',encoding='gbk',newline="") as csvfile:
    w = csv.writer(csvfile)
    w.writerow(div_list)

print ("line 2 start ......")

with open(r'D:\CL\gittest\spider\test.csv','a+',encoding='gbk',newline="") as csvfile:
    w = csv.writer(csvfile)
    w.writerow(div_list2)