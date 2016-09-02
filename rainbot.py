#!/usr/bin/env python3
from bot import Bot
import sys
import json
import random

#try:
#    addr = sys.argv[1]
#     nick = sys.argv[2]
#except IndexError:
#    print('usage: '+sys.argv[0]+' irc_server nick [channel1 ....]')
#try:
#    addr = sys.argv[1].split(':',maxplist=1)[0]
#    port = sys.argv[1].split(':',maxplist=1)[1]
#except:
#    port = 6667
#nick = sys.argv[2]
#channels = sys.argv[3:]
try:
    filename = sys.argv[1]
except IndexError:
    print('usage: ' + sys.argv[0]+' <path-to-json-config-file>')
bot = Bot(filename)
random.seed()
bot.start()
