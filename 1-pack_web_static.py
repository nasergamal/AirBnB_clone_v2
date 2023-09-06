#!/usr/bin/python3
# create tar of webstatic
from fabric.api import local
from time import strftime


def do_pack():
    name = "versions/web_static_" + strftime("%Y%m%d%H%M%S")
    d = local("mkdir -p versions")
    p = local("tar -cvzf {}.tgz web_static".format(name))
    if p.succeeded and d.succeeded:
        return name
