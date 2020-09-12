#!/usr/bin/env python
# coding:utf-8
import socket
import urllib2
import sys
import config
import contenttype
import useragent


class Core(object):
        __urls = None
        __verbose = None
        __nick_name = None
        __useragent = None

        def __init__(self, name, url=None, verbose=False):
                self.__nick_name = name
                self.__verbose = verbose
                self.__useragent = useragent.UserAgent()

                if url is not None:
                        self.__urls = [url]

                else:
                        self.__urls = config.Config().getUrls()

		if name is None:
			print u"\x1b[1;37;41m[ERROR] No user specified! \x1b[0;0;0m"
			sys.exit(1)

                print "\x1b[1;36;40m [INFO]", len(self.__urls), "urls loaded ... \x1b[0;0;0m"

        def __fetchContent(self, url):
                ua = {'User-Agent': self.__useragent.getRandomUserAgent()}
                try:
                        if not (url is None):
                                socket.setdefaulttimeout(10)
                                client = urllib2.urlopen(urllib2.Request(url, None, ua))
                                if contenttype.ContentType.isHTML(client):
                                        data = client.read()
                                        del client
                                        return data

                                del client

                except ValueError, e:
                        if not (url is None):
                                socket.setdefaulttimeout(10)
                                client = urllib2.urlopen(urllib2.Request(u'http://' + url, None, ua))
                                if contenttype.ContentType.isHTML(client):
                                        data = client.read()
                                        del client
                                        return data

                                del client

                except Exception, e:
                        if self.__verbose:
                                print u"\x1b[1;37;41m[ERROR]", unicode(e), "-->", url, u"\x1b[0;0;0m"

                return None

        def __validate(self, url):
                fails = config.Config().getErrors()

                try:
                        content = self.__fetchContent(url)
                        if content is not None:
                                for fail in fails:
                                        if fail in content:
                                                return False

                                return True

                except Exception, e:
                        print e

                return False

        def run(self):
                success = 0
                for url in self.__urls:
                        url = url.replace('{u}', self.__nick_name)
                        if self.__validate(url):
                                print "\x1b[1;32;40m [FOUND]", url , "\x1b[0;0;0m"
                                success += 1

                print "\x1b[1;36;40m [INFO]", success, '/', len(self.__urls), "urls found \x1b[0;0;0m"

