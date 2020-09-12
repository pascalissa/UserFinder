#!/usr/bin/env python
#coding:utf-8
import argparse

from core.core import Core


def banner():
        print """
UserFinder v1.0.1
   
Written by Strider for legal use purposes, don't be evil
GPLv3
"""

def main():
	banner()
	parser = argparse.ArgumentParser(description='UserFinder v1.0.1')
	parser.add_argument('-u', '--url', type=str, help='Crawl specific url', default=None)
	parser.add_argument('-n', '--name', type=str, help='Crawl specific name', default=None, required=True)
	parser.add_argument('-v', "--verbose", action='store_true', default=False)
	args = parser.parse_args()

	c = Core(name=args.name, url=args.url, verbose=args.verbose)
	c.run()

if __name__ == '__main__':
	main()
