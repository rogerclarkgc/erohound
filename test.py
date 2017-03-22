# -*- coding: utf-8 -*- 
import re

from bs4 import BeautifulSoup as bsp

from protocol import Downloader
from screening import kisssub


##test kisssub.GotMagnet
searchname = 'hand shakers'
aniname = '小魔女学园'
#k.GotSearchKey(name = aniname)
kiss = Downloader(url = "http://www.kisssub.org/")
k_html = kiss.htmldownload()
k = kisssub(html = k_html)
magtest = k.GotMagnet(search = aniname, num = 0)
magtest2 = k.searchani(searchname)
#magtest2 = k.GotMagnet(search = aniname, num = 5)
#print k.GotSearchKey(aniname)
#print type(magtest),len(magtest)
#print magtest
#soup = bsp(magtest, 'lxml')
#findani = soup.find_all('span',class_ = re.compile('btc.*?'))
#print '\n',len(findani)
#for f in findani:
    #print "+", f.string, "+"




##test protocol.Downloader && kisssub.myanilist


k_ani = k.myanilist(how = "today")
for ani in k_ani:
    print ani

    

    
