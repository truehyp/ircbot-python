#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'truehyp'

import socket
import threading

class ircbot(object):

    def __init__(self, server='irc.freenode.net', port=6667, botname='truehypaaa', channel='#buxingjie'):
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
    #TODO 最好是把PONG放这里，不是PONG消息的话，再返回
    def readline(self):
            buf = self.__irc_socket.recv(512)
            if buf:
                return buf
            else:
                return None
    #TODO 向sock写消息
    def sendline(self, message):
        pass



if __name__ == '__main__':
    linuxbabot = ircbot()
    linuxbabot.connect()
    while True:
        print(linuxbabot.readline())

