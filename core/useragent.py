#!/usr/bin/env python
# coding:utf-8

import os
import random
import colorama


class UserAgent(object):
        __debug = False
        __useragents = []

        def __init__(self, debug=False):
                self.__debug = debug
                colorama.init()
                if self.__debug:
                        print "\x1b[0;36;1m [INFO] LOADING USER AGENTS \x1b[0;0;0m"
                #
                try:
                        f = open('config/useragents.conf', "r")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                                self.__useragents.append(line.replace("\n", ""))

                        if self.__debug:
                                print "\x1b[0;36;1m [INFO] USER AGENTS LOADED \x1b[0;0;0m"

                except Exception, e:
                        if self.__debug:
                                print "\x1b[0;37;41m[FATAL ERROR] ERROR LOADING USER AGENTS -->", e, "\x1b[0;0;0m"

        def getRandomUserAgent(self):
                rnd = random.randint(0, len(self.__useragents) - 1)
                return self.__useragents[rnd]
