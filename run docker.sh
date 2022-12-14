#install docker if not installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'docker is not installed.' >&2
  echo 'Installing docker...'
  sudo apt-get update
  sudo apt-get install -y docker.io
  sudo systemctl start docker
  sudo systemctl enable docker
fi

#create docker volume docker-vol
if ! [ -d "/var/lib/docker-vol" ]; then
  echo 'Creating docker volume on /var/lib/docker-vol'
  sudo mkdir /var/lib/docker-vol
  sudo chown -R $USER:$USER /var/lib/docker-vol
  docker volume create --driver local --opt type=none --opt device=/var/lib/docker-vol --opt o=bind docker-vol
fi

docker run -dp 3000:3000 -v docker-vol:/var/lib/jbang-spring-boot jbang-spring-boot
 :/etc/todos getting-started
