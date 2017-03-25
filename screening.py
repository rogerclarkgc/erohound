# -*- coding: utf-8 -*- 
import urllib
import re
import itertools
import urlparse
import datetime
import itchat
from bs4 import BeautifulSoup as bsp

import protocol

"""
class kisssub is a link crawler to download anime date from www.kisssub.org.

Using BeatifulSoup4 to screen the HTML and export the anime's name and its recent magnet link

the coding system of HTML file is unicode, but in this file the coding system is utf-8


"""


class kisssub(object):

    # Initializing the model
    #
    # self.html:store the html data
    #
    # self.anilist:a dict to store the animations'name
    #
    # self.select:a dict to store possible input of data

    def __init__(self, html=None):
        self.status = False
        self.html = html
        self.anilist = {}
        self.select = {"mon": ["mon", "Mon", "Monday", "1"],
                       "tue": ["tue", "Tue", "Tuesday", "2"],
                       "wed": ["wed", "Wed", "Wednesday", "3"],
                       "thu": ["thu", "Thu", "Thursday", "4"],
                       "fri": ["fri", "Fri", "Friday", "5"],
                       "sat": ["sat", "Sat", "Saturday", "6"],
                       "sun": ["sun", "Sun", "Sunday", "7"],
                       "today": ["today", "Today", "now", "0"],
                       "all": ["all", "All", "9"]}


    # Description: myanilist(self, how = date your input)
    #
    # use this function to got the anime list of specified date,the input date must included in self.select
    #
    # the return value of this function is a list instance which including animes' name

    def myanilist(self, how="today"):
        today_ani = [None for i in range(0,0) ]
        
        # Description: SelectOneDay(html, select)
        #
        # use this function to select the specified date tag in HTML
        #
        # the return value of this function is a instance of bs4.element.tag,the coding system of str in this
        #
        # bs4 instance is unicode

        def SelectOneDay(html, select):
            kisssub_soup = bsp(html, 'lxml')
            ani_td = kisssub_soup.find_all("td",
                                           text = re.compile(select))
            print "find specified tag! len:", len(ani_td)
            if len(ani_td) <= 0:
                #raise RuntimeError('can not find specified tag')
                return 'None'
            s_td = ani_td[0].next_sibling.next_sibling
            return s_td

        if not self.anilist.has_key(how):
            if self.select["today"].__contains__(how):
                print "Today's animation are ....\n"
                kisssub_soup = bsp(self.html, 'lxml')
                today = kisssub_soup.find_all("a", href = "today-1.html")
                if len(today) <= 0:
                    self.anilist[how] = 'None'
                    raise RuntimeError('can not find specified tag')
                for t in today:
                    if t.parent.has_attr('style'):
                        today_td = t.parent.next_sibling.next_sibling
                        break
                    else:
                        self.anilist[how] = 'None'
                        raise RuntimeError('can not find "style" tag!')
                today_ani = [ani for ani in today_td.stripped_strings]
                self.anilist[how] = today_ani
                self.status = True

            elif self.select["mon"].__contains__(how):
                print "Monday's animations are:...\n"
                td_mon = SelectOneDay(select = '星期一'.decode('utf-8'),
                                      html = self.html)
                if td_mon.__contains__('None'):
                    self.anilist[how] = td_mon
                else:
                    today_ani = [ani for ani in td_mon.stripped_strings]
                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["tue"].__contains__(how):
                print "Tuesday's animations are:...\n"
                td_tue = SelectOneDay(select = '星期二'.decode('utf-8'),
                                      html = self.html)
                if td_tue.__contains__('None'):
                    self.anilist[how] = td_tue
                else:
                    today_ani = [ani for ani in td_tue.stripped_strings]

                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["wed"].__contains__(how):
                print "Wednesday's animations are:...\n"
                td_wed = SelectOneDay(select = '星期三'.decode('utf-8'),
                                      html = self.html)
                if td_wed.__contains__('None'):
                    self.anilist[how] = td_wed
                else:
                    today_ani = [ani for ani in td_wed.stripped_strings]
                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["thu"].__contains__(how):
                print "Thursday's animations are:...\n"
                td_thu = SelectOneDay(select = '星期四'.decode('utf-8'),
                                      html = self.html)
                if td_thu.__contains__('None'):
                    self.anilist[how] = td_thu
                else:
                    today_ani = [ani for ani in td_thu.stripped_strings]
                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["fri"].__contains__(how):
                print "Friday's animations are:...\n"
                td_fri = SelectOneDay(select = '星期五'.decode('utf-8'),
                                      html = self.html)
                if td_fri.__contains__('None'):
                    self.anilist[how] = td_fri
                else:
                    today_ani = [ani for ani in td_fri.stripped_strings]
                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["sat"].__contains__(how):
                print "Saturday's animations are:...\n"
                td_sat = SelectOneDay(select = '星期六'.decode('utf-8'),
                                      html = self.html)
                if td_sat.__contains__('None'):
                    self.anilist[how] = td_sat
                else:
                    today_ani = [ani for ani in td_sat.stripped_strings]
                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["sun"].__contains__(how):
                print "Sunday's animations are:...\n"
                td_sun = SelectOneDay(select = '星期日'.decode('utf-8'),
                                      html = self.html)
                if td_sun.__contains__('None'):
                    self.anilist[how] = td_sun
                else:
                    today_ani = [ani for ani in td_sun.stripped_strings]

                    self.anilist[how] = today_ani
                    self.status = True

            elif self.select["all"].__contains__(how):
                kiss_soup = bsp(self.html, 'lxml')
                td_all = kiss_soup.find_all("a",
                                            class_ = re.compile("bgm_score.*?"))
                if len(td_all) <= 0:
                    raise RuntimeError("can not find specified tag")
                    self.anilist[how] = 'None'
                else:
                    for td in td_all:
                        for ani in td.stripped_strings:
                            today_ani.append(ani)

                    self.anilist[how] = today_ani
                    self.status = True

            else:
                self.anilist[how] = 'None'
                #raise RuntimeError("wrong date")
            
        else:
            print self.status

            
        return self.anilist[how]

    # Description: GotSearchKey(self, aniname = the name of anime)
    #
    # use this function to got the search key of an anime, the name of anime must fully matched the index of kisssub.org
    #
    # the return value of this function is a str instance may look like "search.php?keyword=(the keyword)"

    def GotSearchKey(self, aniname = None):
        soup = bsp(self.html, 'lxml')
        soup_find = soup.find_all('a', text = aniname.decode('utf-8'))
        if len(soup_find) <= 0:
            key = 'None'
            #raise RuntimeError('can not find anime,check your input')
        else:
            key = urllib.quote(soup_find[0]['href'].encode('utf-8'), safe = '.?=')
        return key

    # Description: GotMagnet(self, search = the name of anime, num = 0, maxnum = 5)
    #
    # use this function to got the magnet link of an anime,the name of anime must fully match the index of kissub.org
    #
    # the function will got 5 magnetlink(control by param maxnum), but only return 1 magnet link, the param num can
    #
    # control the index of magnet link
    #
    # the return value of this function is a dict instance contains two key:'magnet' and 'message'

    def GotMagnet(self, search = None, num = 0, maxnum = 5):
        magnet_link = {'magnet': 'None',
                       'message': 'None'}
        if num >= maxnum:
            raise RuntimeError('check your param:num, because num must less than maxnum')
        key = self.GotSearchKey(aniname = search)  # use protocol.Downlaod to download search result page
        if key == 'None':
            pass
        else:
            baseURL = "http://www.kisssub.org/"
            abURL = baseURL + key
            downloader = protocol.Downloader(url = abURL)
            findHTML = downloader.htmldownload()
            find_soup = bsp(findHTML, 'lxml')
            if len(find_soup.find_all('td', colspan = re.compile('.*?'))) >= 1:  # check the search result
                raise RuntimeError('can not find anime! check your input')

            soup_time = find_soup.find_all('tr', class_ = re.compile('alt.*?'))  # find the animelist of search page
            down_link = soup_time[0:maxnum]
            link = [i.find_all('a', href = re.compile('show.*?'))[0]['href'] for i in down_link] # store the download page link
            downlink = [baseURL + l for l in link]
            magnet_down = protocol.Downloader(url = downlink[num])  # find the magnet link
            magnetHTML = magnet_down.htmldownload()
            magnet_soup = bsp(magnetHTML, 'lxml')
            magnet_link['magnet'] = magnet_soup.find_all('a', id = 'magnet')[0]['href']
            magnet_link['message'] = magnet_soup.find_all('a', href = link[num])[0].string
            print 'find tag:', len(magnet_link['message']) # test code
            print 'The information of this anime is:', magnet_link['message']
            print 'I have found the magnet link of', search.decode('utf-8'), ':\n', magnet_link['magnet']
        return magnet_link

    # Description: searchani(self, keyword = ani's name maxnum, maxnum = 5, num = 0)
    #
    # this function can search an anime and return it's magnet link
    #
    # may useful than GotMagnet(), beacause it would use the search.php of kisssub, don't need you input the correct
    #
    # name of an anime
    #
    # the return value of this function is a dict instance contains two key:'magnet' and 'message'

    def searchani(self, keyword = None, maxnum = 5, num = 0):
        magnet_link = {'magnet': 'None',
                       'message': 'None'}
        search_php = 'http://www.kisssub.org/search.php?keyword='
        base_url = 'http://www.kisssub.org/'
        search_url = search_php + urllib.quote(keyword)
        search_html = protocol.Downloader(search_url).htmldownload()
        search_soup = bsp(search_html, 'lxml')
        if len(search_soup.find_all('td', colspan = re.compile('.*?'))) >= 1:  #check the search result
            #raise RuntimeError('can not find the anime you input')
            pass
        else:
            search_result = search_soup.find_all('a', href = re.compile('show.*?'))[0:maxnum]
            search_link = [i['href'] for i in search_result]
            down_link = [base_url+l for l in search_link]

            magnet_html = protocol.Downloader(down_link[num]).htmldownload()
            magnet_soup = bsp(magnet_html, 'lxml')
            magnet_link['magnet'] = magnet_soup.find_all('a', id = 'magnet')[0]['href']
            magnet_link['message'] = magnet_soup.find_all('a', href = search_link[num])[0].string
            print 'find tag:', len(magnet_link['message'])  # test code
            print 'The information of', keyword.decode('utf-8'), 'is:\n', magnet_link['message']
            print 'I have found the magenet link of', keyword.decode('utf-8'), '\n', magnet_link['magnet']
        return magnet_link


class Email163:
    pass

    
                    




