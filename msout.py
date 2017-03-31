# -*- coding: utf-8 -*-

import re

import itchat
from itchat.content import *

from screening import *
from protocol import *

"""
This module is will reive message from itchat.content and tring resolve it's meaning

"""

class messageout(object):

    def __init__(self, command = None, to = 'filehelper'):
        self.command = command
        self.rescommand = None
        self.param = None
        self.to_user = to
        self.commandlist = ['search', 'ani']

    def searchani(self):
        print self.rescommand, ":", self.param, "\n"
        k_html = Downloader(url = "http://www.kisssub.org/").htmldownload()
        k_mag = kisssub(html = k_html).searchani(keyword = self.param)
        message_send = u'片源:' + k_mag['message']
        return [message_send, k_mag['magnet']]

    def searchlist(self):
        print self.rescommand, ":", self.param, "\n"
        k_html = Downloader(url = "http://www.kisssub.org").htmldownload()
        anilist = kisssub(html = k_html).myanilist(how = self.param)
        if anilist[0].__contains__('N'):
            animessage = u'没有找到这一日期的列表，请检查输入'
        else:
            animessage = '\n'.join(anilist)
            #print animessage
        return [animessage]

    def resolve(self):
        if self.command is not None:
            rescommand = re.findall('(.*?)<.*?>', self.command)
            if len(rescommand ) <= 0:
                self.rescommand = None
            else:
                self.rescommand = rescommand[0]
                param = re.findall('.*?<(.*?)>', self.command)
                if len(param) <= 0:
                    self.param = None
                elif param[0] == '':
                    self.param = None
                else:
                    self.param = param[0]
                    self.param = self.param.encode('utf-8')
        else:
            raise RuntimeError('No key word input in resolve()!')
        if [self.rescommand, self.param].__contains__(None) == False:
            itchat.send(u'解析命令成功！', self.to_user)

    def action(self):

        if [self.rescommand, self.param].__contains__(None) == True:
            pass

        elif self.rescommand.lower() == u'search':
            message_send = self.searchani()
            for m in message_send:
                itchat.send(m, self.to_user)

        elif self.rescommand == u'ani':
            message_send = self.searchlist()
            for m in message_send:
                itchat.send(m, self.to_user)


    def testmessage(self):
        itchat.send('receive success!', 'filehelper')


if __name__ == '__main__':
    test_command = u'search<动物朋友>'
    m = messageout(command=test_command)
    m.resolve()
    messageout = m.action()
    print messageout



