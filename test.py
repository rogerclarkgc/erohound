# -*- coding: utf-8 -*- 
from protocol import Downloader
from screening import kisssub
from bs4 import BeautifulSoup as bsp
import re

url = 'http://www.kisssub.org/'
k = Downloader(url)
k_html = k.HTMLdownload()
soup = bsp(k_html, 'lxml')

k_screen = kisssub(html = k_html)

k_ani = k_screen.myanilist(how = "9")
for ani in k_ani:
    print ani

    

    
