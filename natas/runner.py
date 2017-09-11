#!/usr/bin/python2
password = ''
for x in range(0, 11):
    current_level = x
    next_level = x+1
    print "{$} Lets go from %d to %d" %(current_level, next_level)
    code = "from natas import level%d;password=level%d.exploit(password)" %(current_level, current_level)
    exec(code)
    print "{!} Got %s" %password
