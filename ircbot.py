#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'truehyp'

import socket
import threading
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)


def nowtime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class ircbot(object):

    def __init__(self, server='irc.freenode.net', port=6667, botname='truehypbbb', channel='#buxingjie'):
        self.__server = server
        self.__port = port
        self.__botname = botname
        self.__channel = channel
        self.__irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        try:
            self.__irc_socket.connect((self.__server, self.__port))
            self.__irc_socket.send(bytes("NICK "+ self.__botname +"\r\n", encoding="utf8"))
            self.__irc_socket.send(bytes("USER " + self.__botname + " " + self.__botname + " "
                                   + self.__botname + " :" + self.__botname + "\r\n", encoding="utf8"))
            self.__irc_socket.send(bytes("JOIN " + self.__channel + "\r\n", encoding="utf8"))
        except Exception as e:
            print("Exception: ", e)
    '''
    return str
    '''
    def readline(self):
            buf = self.__irc_socket.recv(512)
            if buf:
                buf = buf.decode('utf-8')
                if (buf.startswith('PING')):
                    logging.info(nowtime()+' '+buf)
                    self.pong(buf)
                    self.sendmessage("hahah")
                    return None
                else:
                    return buf
            else:
                return None
    '''
    message need be str
    '''
    def pong(self, message):
        message = message.replace('PING', 'PONG', 1)
        logging.info(nowtime()+' '+message)
        self.__irc_socket.send(message.encode())
    def sendmessage(self, message):
        self.pong('PING irc.freenode.net\r\n')
        message = ('PRIVMSG'+' '+self.__channel+' :'+message+'\r\n')
        logging.info(nowtime()+' '+message)
        self.__irc_socket.send(message.encode())

if __name__ == '__main__':
    linuxbabot = ircbot()
    linuxbabot.connect()
    while True:
        buf = linuxbabot.readline()
        if buf is None:
            continue
        logging.info(nowtime()+' '+buf)

