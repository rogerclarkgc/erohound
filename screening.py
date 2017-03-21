# -*- coding: utf-8 -*- 
import urllib, urllib2
import string
import re
import itertools
import urlparse
import datetime
import itchat
from bs4 import BeautifulSoup as bsp

import protocol


class kisssub:

    def __init__(self, html=None):
        self.status = False
        self.html = html
        self.anilist = {}
        self.select = {"mon" :["mon", "Mon", "Monday", "1"],
                       "tue" :["tue", "Tue", "Tuesday", "2"],
                       "wed" :["wed", "Wed", "Wednesday", "3"],
                       "thu" :["thu", "Thu", "Thursday", "4"],
                       "fri" :["fri", "Fri", "Friday", "5"],
                       "sat" :["sat", "Sat", "Saturday", "6"],
                       "sun" :["sun", "Sun", "Sunday", "7"],
                       "today" :["today", "Today", "now", "0"],
                       "all" :["all", "All", "9"]}



    def myanilist(self, how = "today"):
        today_ani = [None for i in range(0,0)]
        
        def SelectOneDay(html, select):
            kisssub_soup = bsp(html, 'lxml')
            ani_td = kisssub_soup.find_all("td", text =
                                           re.compile(select))
            print "find specified tag! len:", len(ani_td)
            if len(ani_td) <= 0:
                raise RuntimeError('can not find specified tag')
            s_td = ani_td[0].next_sibling.next_sibling
            return s_td

        if not self.anilist.has_key(how):
            if self.select["today"].__contains__(how):
                print "Today's animation are ....\n"
                kisssub_soup = bsp(self.html, 'lxml')
                today = kisssub_soup.find_all(href = "today-1.html")
                if len(today) <= 0:
                    raise RuntimeError('can not find specified tag')
                for t in today:
                    if t.parent.has_attr('style'):
                        today_td = t.parent.next_sibling.next_sibling
                for ani in today_td.stripped_strings:
                    today_ani.append(ani)
                self.anilist[how] = today_ani
                self.status = True

            elif self.select["mon"].__contains__(how):
                print "Monday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期一'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["tue"].__contains__(how):
                print "Tuesday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期二'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["wed"].__contains__(how):
                print "Wednesday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期三'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["thu"].__contains__(how):
                print "Thursday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期四'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["fri"].__contains__(how):
                print "Friday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期五'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["sat"].__contains__(how):
                print "Saturday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期六'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["sun"].__contains__(how):
                print "Sunday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期日'.decode('utf-8'),
                                      html = self.html)
                for ani in td_mon.stripped_strings:
                    today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            elif self.select["all"].__contains__(how):
                kiss_soup = bsp(self.html, 'lxml')
                td_all = kiss_soup.find_all("a",
                                            class_ = re.compile("bgm_score.*?"))
                if len(td_all) <= 0:
                    raise RuntimeError("can not find specified tag")
                for td in td_all:
                    for ani in td.stripped_strings:
                        today_ani.append(ani)

                self.anilist[how] = today_ani
                self.status = True

            else:
                raise RuntimeError("wrong date")
            
        else:
            print self.status

            
        return self.anilist[how]

    ##got an anime's search key ,the name of anime must fully match the index of kisssub.org
    ##the link which contained chines characters has transformed to qutet style
    def GotSearchKey(self, aniname = None):
        soup = bsp(self.html, 'lxml')
        soup_find = soup.find_all('a', text = aniname.decode('utf-8'))
        if len(soup_find) <= 0:
            raise RuntimeError('can not find anime,check your input')
        key = urllib.quote(soup_find[0]['href'].encode('utf-8'), safe = string.printable)
        return key

    ##got the magnet of an animat
    def GotMagnet(self, search = None):
        ##use protocol.Downlaod to download search result page
        key = self.GotSearchKey(aniname = search)
        baseURL = "http://www.kisssub.org/"
        abURL = baseURL + key
        downloader = protocol.Downloader(url = abURL)
        findHTML = downloader.HTMLdownload()
        find_soup = bsp(findHTML, 'lxml')
        if len(find_soup.find_all('td', colspan = re.compile('.*?'))) >= 1:
            raise RuntimeError('can not find anime! check your input')
        #find the animelist of search page
        soup_time = find_soup.find_all('tr', class_ = re.compile('alt.*?'))
        #find the first result of the search page
        down_link = soup_time[0].find_all('a', href = re.compile('show.*?'))
        #got the download page link
        link = down_link[0]['href']
        downlink = baseURL + link
        #find the magnet link
        magnet_down = protocol.Downloader(url = downlink)
        magnetHTML = magnet_down.HTMLdownload()
        magnet_soup = bsp(magnetHTML, 'lxml')
        magnet_link = magnet_soup.find_all('a', id = 'magnet')[0]['href']
        ani_message = magnet_soup.find_all('a', href = link)
        print 'The information of this anime is:', ani_message[0].string
        print 'I have found the magnet link of', search
        return magnet_link

class Email163:
    pass

    
                    




