#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'truehyp'

class ircutil(object):
    a=0
    @staticmethod
    def isPing(s):
        if (s.startswith('PING')):
            return True
        return False
