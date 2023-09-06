#!/usr/bin/python3
''' create tar of webstatic '''
from fabric.api import local, sudo, put, env
from time import strftime
env.user = 'ubuntu'
env.hosts = ['3.94.185.113', '54.196.42.192']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    '''depoly to servers'''
    if not archive_path:
        return False
    try:
        put(archive_path, "/tmp/")
        archive_path = archive_path.split("/")[1].split(".")[0]
        new_path = "/data/web_static/releases/{}/".format(archive_path)
        run("sudo mkdir -p {}".format(new_path))
        run("sudo tar -xzf /tmp/{}.tgz -C {}".format(archive_path, new_path))
        run("sudo rm /tmp/{}.tgz".format(archive_path))
        run("sudo mv {}web_static/* {}".format(new_path, new_path))
        run("sudo rm -rf {}web_static/".format(new_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_path))
    except Exception as e:
        return False
    return True


def do_pack():
    '''create tar'''
    name = "versions/web_static_" + strftime("%Y%m%d%H%M%S") + '.tgz'
    d = local("mkdir -p versions")
    p = local("tar -cvzf {} web_static".format(name))
    if p.succeeded and d.succeeded:
        return name


def deploy():
    '''create and deploy tar to server'''
    arch_path = do_pack()
    if not arch_path:
        return False
    return do_deploy(arch_path)
