# -*- coding: utf-8 -*- 
import urllib, urllib2
import re
import itertools
import urlparse
import datetime
import itchat
from bs4 import BeautifulSoup as bsp

class Downloader:

    def __init__(self, url, user_agent='erohound', category = None):
        self.url = url
        self.user_agent = user_agent
        self.category = category
        self.status = None
    
    def HTMLdownload(self, num_retries=2):
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
                    return download(url, num_retries-1)
        return html





