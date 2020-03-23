exec {'killprocess':
  command => 'pkill -f killmenow',
  provider => 'shell',
}
