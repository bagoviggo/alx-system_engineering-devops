#manifest to kill process killmenow

exec { 'killmenow':
  onlyif  => 'pgrep killmenow',
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
}

