# -*- coding: utf-8 -*-
import re
import better_exceptions
from bs4 import BeautifulSoup as bsp
import chardet

from protocol import Downloader
from screening import kisssub


##test kisssub.GotMagnet
searchname = '命运石'
aniname = '小魔女学园'
print chardet.detect(aniname)

#k.GotSearchKey(name = aniname)
kiss = Downloader(url = "http://www.kisssub.org/")
k_html = kiss.htmldownload()
print chardet.detect(k_html)
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
    #pass
