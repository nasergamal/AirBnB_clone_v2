#!/usr/bin/python3
''' create and deploy tar '''
from fabric.api import env, run, put
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
