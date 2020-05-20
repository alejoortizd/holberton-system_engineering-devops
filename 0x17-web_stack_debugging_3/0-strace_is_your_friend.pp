# Apache is returning a 500 error
exec { ' fix double pp':
  command => "sed -i 's/phpp/php/' /vaar/www/html/wp-settings.php",
  path    => '/bin/',
}
