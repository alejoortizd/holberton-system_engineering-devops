# create a manifest that kills a process named killmenow

exec {'killprocess':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
