# -*- coding: utf-8 -*- 
from protocol import Downloader
from screening import kisssub
from bs4 import BeautifulSoup as bsp
import re

##test kisssub.GotMagnet
aniname = 'Hand Shakers'
#k.GotSearchKey(name = aniname)
kiss = Downloader(url = "http://www.kisssub.org/")
k_html = kiss.HTMLdownload()
k = kisssub(html = k_html)
magtest = k.GotMagnet(search = aniname)
#print k.GotSearchKey(aniname)
#print type(magtest),len(magtest)
print magtest
#soup = bsp(magtest, 'lxml')
#findani = soup.find_all('span',class_ = re.compile('btc.*?'))
#print '\n',len(findani)
#for f in findani:
    #print "+", f.string, "+"




##test protocol.Downloader && kisssub.myanilist


#k_ani = k.myanilist(how = "today")
#for ani in k_ani:
    #print ani

    

    
