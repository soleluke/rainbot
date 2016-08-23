import socket
from threading import Thread
from time import sleep
from irchandler import IRCHandler
class Bot():
    def __init__(self,addr,port,nick,channels):
        print('Initializing bot '+nick+' connecting to '+addr+':'+str(port)+' channels:'+str(channels))
        self._sock = socket.socket()
        self._sock.connect((addr,port))
        print('Socket connected to '+ addr +':'+str(port))
        self._q=Queue()
        #TODO: JSON IMPORT FOR CONINFO
        self._coninfo = {
            'addr':addr,
            'port':port,
            'nick':nick,
            'channels':channels,
            'sock':self._sock,
        }
        self._handler = IRCHandler(self._coninfo)
        self._handler._send = self._send
        self._listen_thread = Thread(target = self._listen)
        self._listening = True
        self._listen_thread.start()
        self._send('USER '+nick+' 0* :'+nick)
        self._send('NICK '+nick)
    def __del__(self):
        print('SIGTERM')
    def start(self):
        while 1:
            try:
                m = self._q.dequeue()
                print(m)
                self._handler.handle(m)
            except IndexError:
                sleep(1)
            except Exception as e:
                print(e)
                self._listening == False
                self._listen_thread.join()
    def _listen(self):
        while self._listening ==True:
            try:
                buf = self_.sock.recv(4096).decode()
                print(buf)
                for b in buf.split('\r\n'):
                    self.q.enqueue(b.split())
            except:
                self._listening == False
    def _send(self,m):
        print(m.encode()+b'\r\n')
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
