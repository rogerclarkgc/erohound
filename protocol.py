# -*- coding: utf-8 -*- 
import urllib
import urllib2
import re
import itertools
import urlparse
import datetime

import itchat

from bs4 import BeautifulSoup as bsp
"""
class Downloader is a set of useful tools to download website content

"""

class Downloader:

    def __init__(self, url, user_agent='erohound', category = None):
        self.url = url
        self.user_agent = user_agent
        self.category = category
        self.status = None

    # Description: htmldownload(self, num_retries = the retry time of downloading)
    #
    # use this function to download basic html source code of the website
    #
    # the return value of this function is a long str instance which contain the source code of website
    
    def htmldownload(self, num_retries=2):
        print 'Downloading:', self.url
        headers = {'User-agent':self.user_agent}
        request = urllib2.Request(self.url, headers = headers)

        try:
            html = urllib2.urlopen(request).read()
            if len(html) > 0:
                self.status = '1'
                print"Done!\n"
        except urllib2.URLError as e:
            print 'Download error:', e.reason
            html = None
            self.status = '0'
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.reason < 600:
                    return Downloader.HTMLdownload(num_retries-1)
        return html







