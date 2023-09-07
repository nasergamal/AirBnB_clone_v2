#!/usr/bin/python3
'''remove old tar'''
from fabric.api import *
from time import strftime

env.hosts = ['3.94.185.113', '54.196.42.192']


def do_clean(number=0):
    '''pack webstatic dir'''
    if number == 0:
        number = 1
    number = int(number) + 1
    with lcd("versions"):
        local('ls -tp | tail -n +{} | tr "\n" " " \
               | xargs rm'.format(number))
    with cd("/data/web_static/releases"):
        sudo("ls -tp | tail -n +{} | tr '\n' ' ' \
              | xargs rm -r".format(number))
