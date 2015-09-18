#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


def do_math():
    return 1 + 3


def main():
    print do_math()
    print "This is an example of a file that does work"
    print "There is another line that was added in the pull request"


if __name__ == '__main__':
    main()
