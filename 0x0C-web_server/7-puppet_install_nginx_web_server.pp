# Installs and configures an nginx server

exec {'install': 
  provider => shell,
  command => ' sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;\n\trewrite ^\/redirect_me https:\/\/intranet.alxswe.com\/projects\/266 permanent;/" /etc/nginx/sites-available/default ; sudo service star ; sudo service reload',
}
