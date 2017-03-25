# -*- coding: utf-8 -*-


"""
Logic of this model:

this model is the middle layer of the whole project,

the detailed  of this model might look like this diagram below:

itchat use itchat to push message to wechat
||
message.py to resolve the user's input
||
screening.py



"""

import thread
import time
import better_exceptions
import urllib
import re

import itchat
from itchat.content import *
import chardet

from screening import kisssub
from protocol import Downloader
# 无法实现类似菜单式的递进消息处理，如输入'搜索'进入搜索模式，在搜索模式下输入'退出'则退出搜索模式
#
# 现在采用命令行方式的交互方法，把搜索命令和搜索关键词整合在一句中
#
# 使用的命令为’命令<参数>'的方式

@itchat.msg_register(TEXT)
def reply_message(msg):

    if msg['Text'].__contains__('search<'):

        aniname = re.findall('search<(.*?)>',msg['Text'])
        print aniname, len(aniname)

        itchat.send(u'搜索中...', 'filehelper')
        k_html = Downloader(url = "http://www.kisssub.org/").htmldownload()
        k_mag = kisssub(html = k_html).searchani(keyword = aniname[0].encode('utf-8'))
        message_send = u'片源：'+ k_mag['message']
        itchat.send(message_send, 'filehelper')
        itchat.send(k_mag['magnet'], 'filehelper')

    if msg['Text'].__contains__('ani<'):
        date = re.findall('ani<(.*?)>', msg['Text'])
        print date, len(date)

        itchat.send(u'搜索动漫列表中...', 'filehelper')
        k_html = Downloader(url = "http://www.kisssub.org").htmldownload()
        anilist = kisssub(html = k_html).myanilist(how = date[0].encode('utf-8'))
        if anilist[0].__contains__('N'):
            itchat.send(u'没有找到这一日期的列表，请检查输入', 'filehelper')
        else:
            animessage = '\n'.join(anilist)
            print animessage
            itchat.send(animessage, 'filehelper')




itchat.auto_login(True)
itchat.run()






