#!/usr/bin/env puppet
# Fix internal server error by replacing "phpp" with "php" 
# in wp-settings.php file

exec { 'web stack debugging':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => ['/usr/local/bin', '/bin'],
  provider => shell,
}

