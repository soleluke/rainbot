#handles all IRC message passing and connections
import socket
from threading import Thread
from subprocess import Popen
from time import sleep
import random
import re
import json
import urllib.parse
import urllib.request
import sys
class IRCHandler():
    def __init__(self,coninfo): # initializes an IRC handler for the given connection info
#coninfo is a dictionary with the following members
#   Required members:
#       addr    :   the server address 'irc.example.com'
#       port    :   the port to connect to (normally 6667
#       nick    :   the nick to use when connecting to a network
#       channels:   a list of channels to connect to ["#chan1","#chan2",...}
#       sock    :   the socket to be used (we will use a generated one in the Bot class
#   Optional members:
#       password:   password for nickserv identification NOTE: this recuired that the nick already be registered on the server manually
#       autojoin:   'true' or 'false'. if it is true, then the bot will automatically join any channel it is invited to. Defaults to false if not set
#       
        self.coninfo = coninfo
        if 'autojoin' not in coninfo.keys():
            coninfo['autojoin'] = 'true'
        self._sock = coninfo['sock']
        print('IRC Handler initialized')
    def _send(self):
        pass
    def say(self,c,m): #send a message (m) to the given channel (c)
        self._send('PRIVMSG '+c+' :'+m)
    def handle(self,buf): #handle any given message from the IRC server
        print(buf)
        if buf[0] == 'PING':
            self._on_ping(buf)
        if buf[1] == '001':
            self._on_welcome(buf)
#       normally, you'd want some sort of privmsg handling. Rainbot doesn't really need this since all it does is send alerts
#       if buf[1] == 'PRIVMSG':
#            self._on_privmsg(buf)
        if buf[1] == 'INVITE':
            self._on_invite(buf)
    def _on_ping(self,buf):
        self._send('PONG ' + buf(buf.index('PING'+1)))
    def _on_welcome(self,buf):
        print('Connection Established, joining channels')
        if 'password' in coninfo.keys(): #nickserv identification if password exists
            self._send('PRIVMSG nickserv : identify '+ coninfo['password'])
        for channel in self._coninfp['channels']:
            self._send('JOIN '+channel)
        # TODO: implement auto-inviting via chanserv if channel access is restricted or maybe just knocking
    def _on_invite(self,buf):
        if self.coninfo['autojoin'] == 'true':
            self._confinfo['channels']+=[buf[3]]
            self._send('JOIN '+buf[3])
#TODO: implement an overridable privmesg handling function for more general use
    def _on_privmsg(self,buf):
        pass 
