#!/usr/bin/python3
'''remove old tar'''
from fabric.api import *
from os import listdir
env.hosts = ['3.94.185.113', '54.196.42.192']


def do_clean(number=0):
    '''pack webstatic dir'''
    if number == 0:
        number = 1
    number = int(number) + 1

    files = sorted(listdir("versions"))
    [files.pop() for i in range(number - 1)]
    with lcd("versions"):
        [local("rm ./{}".format(f)) for f in files]
    with cd("/data/web_static/releases"):
        sudo("ls -tp | tail -n +{} | tr '\n' ' ' | xargs rm -r"
             .format(number))
