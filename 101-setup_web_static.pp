# prepare webstatic
include stdlib

exec { 'one nginx right away':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['first_dir']

}

exec {'first_dir':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  before   => Exec['sec_dir']
}
exec {'sec_dir':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  before   => Exec['html']
}
exec {'html':
  command  => "echo 'new config' | sudo tee /data/web_static/releases/test/index.html &> /dev/null",
  provider => shell,
  before   => Exec['sym']
}
exec {'sym':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  before   => Exec['owner']
}

exec {'owner':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell,
  before   => File_line['www']
}

file_line { 'www':
  path   => '/etc/nginx/sites-enabled/default',
  line   => "listen 80 default_server\n\tlocation /hbnb_static { alias /data/web_static/current/;",
  match  => 'listen 80 default_server',
  before => Exec['restart']
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
