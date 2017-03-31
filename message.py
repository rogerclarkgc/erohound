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
from msout import messageout

# 无法实现类似菜单式的递进消息处理，如输入'搜索'进入搜索模式，在搜索模式下输入'退出'则退出搜索模式
#
# 现在采用命令行方式的交互方法，把搜索命令和搜索关键词整合在一句中
#
# 使用的命令为’命令<参数>'的方式

@itchat.msg_register(TEXT)
def reply_message(msg):

    message = messageout(command=msg['Text'])
    message.resolve()
    print message.param, message.rescommand
    #message.testmessage()
    message.action()





itchat.auto_login(True)
itchat.run()






