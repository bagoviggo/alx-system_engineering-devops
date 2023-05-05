#!/usr/bin/env bash
# Script that transfers file from client to a server

# Set parameters
path_to_file=$1
ip=$2
username=$3
path_to_ssh_key=$4

# Check if at least 4 parameters are passed
if [ $# -lt 4 ]; then
    echo "Usage: $0 PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
    exit 1
else
	scp -o StrictHostKeyChecking=no -i "$path_to_ssh_key" "$path_to_file" "$username"@"$ip":/home/"$username"
fi

#!/usr/bin/env bash
# This script installs Nginx and configures it to port 80

# Update the package list and install Nginx
apt-get update
apt-get -y install nginx

# Configure Nginx to listen on port 80
sed -i 's/listen 80 default_server;/listen 80;/g' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

# Create a file containing the "Hello World!" message
echo "Hello World!" > /var/www/html/index.html

# Test that Nginx is serving the "Hello World!" message
if curl http://localhost | grep -q "Hello World!"; then
  echo "Nginx is serving the Hello World! message."
else
  echo "Error: Nginx is not serving the Hello World! message."
fi

bagoviggo.tech
#!/usr/bin/env bash
# Script that  configures a new server with redirection

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Update Nginx configuration file to redirect /redirect_me
sudo sed -i 's/location \/ {/location \/redirect_me {\n        return 301 https:\/\/www.google.com;\n    }\n\n    location \/ {\n/' /etc/nginx/sites-available/default

# Restart Nginx service
sudo service nginx restart

# Verify the redirection is working
if curl -I http://localhost/redirect_me | grep -q "301 Moved Permanently"; then
  echo "Redirection is working as expected."
else
  echo "Error: Redirection is not working."
fi

#!/usr/bin/env bash
# Configures a new ubuntu machine by installing
# Nginx where it should be listening on port 80
# Serve a page that would return a Hello World string
#
# colors
blue='\e[1;34m'
brown='\e[0;33m'
green='\e[1;32m'
reset='\033[0m'

echo -e "${blue}Updating and installing ${brown}Nginx${blue}.${reset}\n"
sudo apt-get update -y -qq && \
	 sudo apt-get install nginx -y

echo -e "\n${blue}Setting up some minor stuff.${reset}\n"

# starting nginx service
sudo service nginx start

# allowing nginx on firewall
sudo ufw allow 'Nginx HTTP'

# Give the user ownership to website files for easy editing
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www

# Backup default index
cp /var/www/html/index.nginx-debian.html /var/www/html/index.nginx-debian.html.bckp

# Creating new index
echo -e "Hello World!" > /var/www/html/index.nginx-debian.html

# Setting up /redirect_me to a youtube video
sudo sed -i '24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default

# Set up a 404 page
echo "Ceci n'est pas une page" >> /var/www/html/error_404.html
sudo sed -i '25i\	error_page 404 /error_404.html;' /etc/nginx/sites-available/default

# Restarting nginx
sudo service nginx restart

echo -e "\n${green}Completed.${reset} ✅\n"
# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
# 0x0C web server
