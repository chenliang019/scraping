#!/usr/bin/python3
# coding=gbk

################################
######pip3 install requests######
######pip3 install bs4     ######
######pip3 install lxml    ######
################################


import requests
import lxml
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }

    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers= headers,timeout= 10)
        print (str(i+1),"页响应状态码：",r.status_code)

        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_="hd")
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list

movies = get_movies()
print (movies)