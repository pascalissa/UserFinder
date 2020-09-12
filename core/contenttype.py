#!/usr/bin/env python
#coding:utf-8

class ContentType(object):

    @staticmethod
    def isHTML(res):
        ctype = res.info().type
        if(ctype == "text/html"):
            return True

        if (ctype == "text/plain"):
            return True

        return False

    @staticmethod
    def isAplication(res):
        ctype = res.info()
        if (ctype == "application/pdf"):
            return True

        if (ctype == "application/octet-stream"):
            return True

        return False
