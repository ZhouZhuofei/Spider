# -*- encoding = utf-8 -*-

__author__ = "zhouzhuofei"

import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import csv

#key : 关键词
#filename : 存储的文件名
#n : 爬取的页数

class spider_51 :
    def __init__(self, key = "大数据", filename = "zhipin_job", n =1) :
        self.key = key
        self.filename = filename + key
        self.n = n

    def setkey(self, key) :
        self.key = key
    def setfilename(self, filename) :
        self.filename = filename
    def setn(self, n) :
        self.n = n
    def Spider(self, key, filename, n) :
        self.n = n
        self.key = key
        self.filename = filename
        fp = open('/Users/zhouzhuofei/'+self.filename+'.csv','wt',newline='',encoding='utf_8_sig')
        wr = csv.writer(fp)
        headers = {'user-agent':'Safari/537.36'}
        url = 'https://www.zhipin.com/c100010000/'
        i = 0
        for j in range(0,self.n):
            p = url + '?query' + self.key + '?page=' + str(j)
            html = requests.get(p, headers=headers)
            html.raise_for_status()
            html.encoding = html.apparent_encoding
            soup = BeautifulSoup(html.text,'html.parser')
            liebiao = soup.find_all('div','info-primary')
            for item in liebiao:
                shuju = item.find('h3')
                link = shuju.find('a')['href']
                id = i + 1
                i = id
                print(id)
                time.sleep(0.5)
                dt_html = requests.get('https://www.zhipin.com/'+link, headers = headers).text
                f = etree.HTML(dt_html)
                job_name = f.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/h1/text()')
                print(job_name)
                company = f.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/text()')
                salary = f.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/span/text()')
                content = f.xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/text()')
                com_type = f.xpath('/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/p[4]/a/text()')
                loc = f.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[2]/p/text()')
                wr.writerow((id,job_name,company,salary,content,com_type,loc))
                time.sleep(3)

        fp.close()
def main () :
    s = spider_51()
    n = int(input("enter n:"))
    key = str(input("Enter key:"))
    filename = str(input("enter a name:"))
    s.Spider(key, filename, n)
main()
