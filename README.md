# asynxpct
A combination of python subprocess, asyncio and pexpect libraries for network automation

## Introduction

This script demonstrates the cooperation between the Python packages pexpect, asyncio and subprocess for a certain network topology.


Modify before using according to your topology

## Summary

### Synchronous module

```ruby
(vntdvops) lab@netdevops:~/github/asynxpct$ python
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import xrshow
>>> xrshow.xrshow("pe1", ["show version", "show platform"])
---[ XRSHOW START ]---[ pe1 ]---[ show version ]---
Fri Mar 17 16:30:05.246 UTC
Cisco IOS XR Software, Version 7.5.2
Copyright (c) 2013-2022 by Cisco Systems, Inc.

Build Information:
 Built By     : ingunawa
 Built On     : Tue Apr 26 18:04:31 PDT 2022
 Built Host   : iox-ucs-061
 Workspace    : /auto/srcarchive14/prod/7.5.2/xrv9k/ws
 Version      : 7.5.2
 Location     : /opt/cisco/XR/packages/
 Label        : 7.5.2

cisco IOS-XRv 9000 () processor
System uptime is 1 day 17 hours 25 minutes

---[ XRSHOW END   ]---[ pe1 ]---[ show version ]---

---[ XRSHOW START ]---[ pe1 ]---[ show platform ]---
Fri Mar 17 16:30:05.375 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe1 ]---[ show platform ]---

>>> exit()
(vntdvops) lab@netdevops:~/github/asynxpct$
```


### Used by synchronous cli script

```ruby
(vntdvops) lab@netdevops:~/github/asynxpct$ ./xrshowcli -n pe1 -c "show version" "show platform"
---[ XRSHOW START ]---[ pe1 ]---[ show version ]---
Fri Mar 17 16:28:58.594 UTC
Cisco IOS XR Software, Version 7.5.2
Copyright (c) 2013-2022 by Cisco Systems, Inc.

Build Information:
 Built By     : ingunawa
 Built On     : Tue Apr 26 18:04:31 PDT 2022
 Built Host   : iox-ucs-061
 Workspace    : /auto/srcarchive14/prod/7.5.2/xrv9k/ws
 Version      : 7.5.2
 Location     : /opt/cisco/XR/packages/
 Label        : 7.5.2

cisco IOS-XRv 9000 () processor
System uptime is 1 day 17 hours 24 minutes

---[ XRSHOW END   ]---[ pe1 ]---[ show version ]---

---[ XRSHOW START ]---[ pe1 ]---[ show platform ]---
Fri Mar 17 16:28:58.716 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe1 ]---[ show platform ]---

(vntdvops) lab@netdevops:~/github/asynxpct$
```


### Finally the Asynchronous Script to use the cli script

```ruby
./asyncxpct.py
```

Kindly check the results folder for example of tests.
