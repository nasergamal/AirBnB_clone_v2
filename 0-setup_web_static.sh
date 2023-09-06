#!/usr/bin/env bash
# config web static

if dpkg -s 'nginx' &>/dev/null
then
        EXIST=$(dpkg -s 'nginx' | grep "install ok installed")
        if [[ -z "$EXIST" ]]
        then
                sudo apt install nginx -y
        fi
else
        sudo apt install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo 'new config' | sudo tee /data/web_static/releases/test/index.html &> /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a        location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
