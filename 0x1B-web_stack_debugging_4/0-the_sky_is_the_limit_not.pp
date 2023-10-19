# Task 0: Sky is the limit, let's bring that limit higher

# Fix Nginx limits

exec { 'Update-Limit':

  command => '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx',

}

exec { '/usr/bin/env service nginx restart': }