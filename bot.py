import socket
import json
from threading import Thread
from time import sleep
from irchandler import IRCHandler
class Bot():
    def __init__(self,filename):
        print('loading configuration from ' + filename)
        with open(filename) as file:
            data=json.load(file)
        self._sock = socket.socket()
        self._sock.connect((data['addr'],int(data['port'])))
        self._q = Queue()
        self._coninfo = data
        self._coninfo['sock'] = self._sock
        self._handler = IRCHandler(self._coninfo)
        self._handler._send = self._send
        self._listen_thread = Thread(target = self._listen)
        self._listening = True
        self._listen_thread.start()
        self._send('USER '+data['nick']+' 0 * : '+data['nick'])
        self._send('NICK '+data['nick'])
    def __del__(self):
        print('SIGTERM')
    def start(self):
        while 1:
            try:
                m = self._q.dequeue()
                self._handler.handle(m)
            except IndexError:
                sleep(1)
            except Exception as e:
                print(e)
                self._listening == False
                self._listen_thread.join()
    def _listen(self):
        while self._listening == True:
            try:
                buf = self._sock.recv(4096).decode()
                for b in buf.split('\r\n'):
                    self._q.enqueue(b.split())
            except:
                self._listening == False
    def _send(self,m):
        self._sock.send(m.encode()+b'\r\n')
class Queue():
    def __init__(self):
        self.d=[]
    def enqueue(self,e):
        self.d+=[e]
    def dequeue(self):
        to_ret = self.d[0]
        self.d.pop(0)
        return to_ret
