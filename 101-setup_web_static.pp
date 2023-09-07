# config
include stdlib


package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
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
  before   => File['html']
}
file { 'html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => 'new config',
  before  => Exec['sym']
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
  line   => "listen 80 default_server\n\tlocation /hbnb_static { alias /data/web_static/current/; }",
  match  => 'listen 80 default_server',
  before => Exec['restart']
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
