#!/usr/bin/python2
password = ''
for x in range(0, 3): # there exists 0 -> 9 levels. we currently do 0, 1, 2. next steps doing 3...9
    current_level = x
    next_level = x+1
    print "{$} Lets go from %d to %d" %(current_level, next_level)
    code = "from narnia import level%d;password=level%d.exploit(password)" %(current_level, current_level)
    exec(code)
    print "{!} Got %s" %password
sky@kitten:~/projects/narnia/auto
