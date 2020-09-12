#!/usr/bin/env python
#coding:utf-8

import os

class Config(object):
        __urls = None
        __errors = None

        def __init__(self):
                conf_file = 'config/urls.conf'
                if os.path.exists(conf_file):
                        try:
                                f = open(conf_file, 'r')
                                lines = f.readlines()
                                f.close()

                                self.__urls = []

                                for line in lines:
                                        self.__urls.append(line.strip())

                        except Exception, e:
                                print e

                conf_file = 'config/errors.conf'
                if os.path.exists(conf_file):
                        try:
                                f = open(conf_file, 'r')
                                lines = f.readlines()
                                f.close()

                                self.__errors = []

                                for line in lines:
                                        self.__errors.append(line.strip())

                        except Exception, e:
                                print e


        def getUrls(self):
                return self.__urls

        def getErrors(self):
                return self.__errors