#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'truehyp'

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('irc.freenode.net', 6667))
while True:
    d = s.recv(1024)
    if d:
        print(d)
    else:
        break
s.close()