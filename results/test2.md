```ruby
(vntdvops) lab@netdevops:~/asyncxpct$ grep -i sema asyncxpct.py
    limit = asyncio.Semaphore(10)
(vntdvops) lab@netdevops:~/asyncxpct$ ./asyncxpct.py
Collecting info from pe1                  Parent.pid: 39661      Child.pid: 39662
Collecting info from p2                   Parent.pid: 39661      Child.pid: 39665
Collecting info from p3                   Parent.pid: 39661      Child.pid: 39668
Collecting info from p4                   Parent.pid: 39661      Child.pid: 39670
Collecting info from pe5                  Parent.pid: 39661      Child.pid: 39673
Collecting info from p6                   Parent.pid: 39661      Child.pid: 39676
Collecting info from p7                   Parent.pid: 39661      Child.pid: 39680
Collecting info from p8                   Parent.pid: 39661      Child.pid: 39682
================================================================================
--------------------------------------------------------------------------------
Host: pe1
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ pe1 ]---[ show version ]---
Fri Mar 17 15:05:42.494 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ pe1 ]---[ show version ]---

---[ XRSHOW START ]---[ pe1 ]---[ show platform ]---
Fri Mar 17 15:05:42.615 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe1 ]---[ show platform ]---

---[ XRSHOW START ]---[ pe1 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:42.749 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/2                *PtoP*         Up    28   00:20:56 Yes None None

Total adjacency count: 1
---[ XRSHOW END   ]---[ pe1 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p2
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p2 ]---[ show version ]---
Fri Mar 17 15:05:43.618 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p2 ]---[ show version ]---

---[ XRSHOW START ]---[ p2 ]---[ show platform ]---
Fri Mar 17 15:05:43.733 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p2 ]---[ show platform ]---

---[ XRSHOW START ]---[ p2 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.862 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
PE1            Gi0/0/0/2                *PtoP*         Up    21   00:20:56 Yes None None
P3             Gi0/0/0/0                *PtoP*         Up    25   00:20:55 Yes None None
P6             Gi0/0/0/1                *PtoP*         Up    28   00:20:56 Yes None None
P7             Gi0/0/0/3                *PtoP*         Up    25   00:20:55 Yes None None

Total adjacency count: 4
---[ XRSHOW END   ]---[ p2 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p3
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p3 ]---[ show version ]---
Fri Mar 17 15:05:42.846 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p3 ]---[ show version ]---

---[ XRSHOW START ]---[ p3 ]---[ show platform ]---
Fri Mar 17 15:05:42.957 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p3 ]---[ show platform ]---

---[ XRSHOW START ]---[ p3 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.087 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/0                *PtoP*         Up    23   00:20:56 Yes None None
P4             Gi0/0/0/2                *PtoP*         Up    29   00:20:57 Yes None None
P7             Gi0/0/0/1                *PtoP*         Up    28   00:20:55 Yes None None

Total adjacency count: 3
---[ XRSHOW END   ]---[ p3 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p4
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p4 ]---[ show version ]---
Fri Mar 17 15:05:43.469 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p4 ]---[ show version ]---

---[ XRSHOW START ]---[ p4 ]---[ show platform ]---
Fri Mar 17 15:05:43.579 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p4 ]---[ show platform ]---

---[ XRSHOW START ]---[ p4 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.719 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P3             Gi0/0/0/2                *PtoP*         Up    27   00:20:55 Yes None None
P8             Gi0/0/0/1                *PtoP*         Up    24   00:20:57 Yes None None
PE5            Gi0/0/0/0                *PtoP*         Up    24   00:20:57 Yes None None
P7             Gi0/0/0/4                *PtoP*         Up    22   00:20:55 Yes None None

Total adjacency count: 4
---[ XRSHOW END   ]---[ p4 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: pe5
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ pe5 ]---[ show version ]---
Fri Mar 17 15:05:43.338 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ pe5 ]---[ show version ]---

---[ XRSHOW START ]---[ pe5 ]---[ show platform ]---
Fri Mar 17 15:05:43.448 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe5 ]---[ show platform ]---

---[ XRSHOW START ]---[ pe5 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.618 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P4             Gi0/0/0/0                *PtoP*         Up    21   00:20:57 Yes None None

Total adjacency count: 1
---[ XRSHOW END   ]---[ pe5 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p6
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p6 ]---[ show version ]---
Fri Mar 17 15:05:43.827 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p6 ]---[ show version ]---

---[ XRSHOW START ]---[ p6 ]---[ show platform ]---
Fri Mar 17 15:05:43.939 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p6 ]---[ show platform ]---

---[ XRSHOW START ]---[ p6 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:44.084 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/1                *PtoP*         Up    26   00:20:56 Yes None None
P7             Gi0/0/0/0                *PtoP*         Up    28   00:20:55 Yes None None

Total adjacency count: 2
---[ XRSHOW END   ]---[ p6 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p7
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p7 ]---[ show version ]---
Fri Mar 17 15:05:43.205 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p7 ]---[ show version ]---

---[ XRSHOW START ]---[ p7 ]---[ show platform ]---
Fri Mar 17 15:05:43.315 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p7 ]---[ show platform ]---

---[ XRSHOW START ]---[ p7 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.469 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/3                *PtoP*         Up    25   00:20:54 Yes None None
P4             Gi0/0/0/4                *PtoP*         Up    26   00:20:55 Yes None None
P3             Gi0/0/0/1                *PtoP*         Up    27   00:20:55 Yes None None
P6             Gi0/0/0/0                *PtoP*         Up    21   00:20:55 Yes None None
P8             Gi0/0/0/2                *PtoP*         Up    29   00:20:55 Yes None None

Total adjacency count: 5
---[ XRSHOW END   ]---[ p7 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p8
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p8 ]---[ show version ]---
Fri Mar 17 15:05:43.010 UTC
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
System uptime is 1 day 16 hours

---[ XRSHOW END   ]---[ p8 ]---[ show version ]---

---[ XRSHOW START ]---[ p8 ]---[ show platform ]---
Fri Mar 17 15:05:43.132 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p8 ]---[ show platform ]---

---[ XRSHOW START ]---[ p8 ]---[ show isis adjacency ]---
Fri Mar 17 15:05:43.274 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P4             Gi0/0/0/1                *PtoP*         Up    20   00:20:57 Yes None None
P7             Gi0/0/0/2                *PtoP*         Up    29   00:20:55 Yes None None

Total adjacency count: 2
---[ XRSHOW END   ]---[ p8 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
Time taken for the program run: 1.46 seconds
(vntdvops) lab@netdevops:~/asyncxpct$
```
