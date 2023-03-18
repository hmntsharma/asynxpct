```ruby
(vntdvops) lab@netdevops:~/asyncxpct$ grep -i sema asyncxpct.py
    limit = asyncio.Semaphore(2)
(vntdvops) lab@netdevops:~/asyncxpct$ ./asyncxpct.py
Collecting info from pe1                  Parent.pid: 39706      Child.pid: 39707
Collecting info from p2                   Parent.pid: 39706      Child.pid: 39710
Collecting info from p3                   Parent.pid: 39706      Child.pid: 39715
Collecting info from p4                   Parent.pid: 39706      Child.pid: 39719
Collecting info from pe5                  Parent.pid: 39706      Child.pid: 39723
Collecting info from p6                   Parent.pid: 39706      Child.pid: 39727
Collecting info from p7                   Parent.pid: 39706      Child.pid: 39731
Collecting info from p8                   Parent.pid: 39706      Child.pid: 39734
================================================================================
--------------------------------------------------------------------------------
Host: pe1
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ pe1 ]---[ show version ]---
Fri Mar 17 15:06:14.813 UTC
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
System uptime is 1 day 16 hours 1 minute

---[ XRSHOW END   ]---[ pe1 ]---[ show version ]---

---[ XRSHOW START ]---[ pe1 ]---[ show platform ]---
Fri Mar 17 15:06:14.930 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe1 ]---[ show platform ]---

---[ XRSHOW START ]---[ pe1 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:15.055 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/2                *PtoP*         Up    25   00:21:28 Yes None None

Total adjacency count: 1
---[ XRSHOW END   ]---[ pe1 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p2
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p2 ]---[ show version ]---
Fri Mar 17 15:06:15.835 UTC
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
Fri Mar 17 15:06:15.947 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p2 ]---[ show platform ]---

---[ XRSHOW START ]---[ p2 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:16.076 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
PE1            Gi0/0/0/2                *PtoP*         Up    25   00:21:28 Yes None None
P3             Gi0/0/0/0                *PtoP*         Up    26   00:21:27 Yes None None
P6             Gi0/0/0/1                *PtoP*         Up    23   00:21:28 Yes None None
P7             Gi0/0/0/3                *PtoP*         Up    26   00:21:27 Yes None None

Total adjacency count: 4
---[ XRSHOW END   ]---[ p2 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p3
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p3 ]---[ show version ]---
Fri Mar 17 15:06:16.344 UTC
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
Fri Mar 17 15:06:16.457 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p3 ]---[ show platform ]---

---[ XRSHOW START ]---[ p3 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:16.582 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/0                *PtoP*         Up    26   00:21:29 Yes None None
P4             Gi0/0/0/2                *PtoP*         Up    28   00:21:30 Yes None None
P7             Gi0/0/0/1                *PtoP*         Up    29   00:21:28 Yes None None

Total adjacency count: 3
---[ XRSHOW END   ]---[ p3 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p4
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p4 ]---[ show version ]---
Fri Mar 17 15:06:17.023 UTC
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
Fri Mar 17 15:06:17.132 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p4 ]---[ show platform ]---

---[ XRSHOW START ]---[ p4 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:17.256 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P3             Gi0/0/0/2                *PtoP*         Up    21   00:21:29 Yes None None
P8             Gi0/0/0/1                *PtoP*         Up    27   00:21:30 Yes None None
PE5            Gi0/0/0/0                *PtoP*         Up    24   00:21:31 Yes None None
P7             Gi0/0/0/4                *PtoP*         Up    24   00:21:28 Yes None None

Total adjacency count: 4
---[ XRSHOW END   ]---[ p4 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: pe5
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ pe5 ]---[ show version ]---
Fri Mar 17 15:06:18.168 UTC
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
Fri Mar 17 15:06:18.287 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ pe5 ]---[ show platform ]---

---[ XRSHOW START ]---[ pe5 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:18.421 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P4             Gi0/0/0/0                *PtoP*         Up    22   00:21:32 Yes None None

Total adjacency count: 1
---[ XRSHOW END   ]---[ pe5 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p6
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p6 ]---[ show version ]---
Fri Mar 17 15:06:18.706 UTC
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
Fri Mar 17 15:06:18.853 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p6 ]---[ show platform ]---

---[ XRSHOW START ]---[ p6 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:18.988 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/1                *PtoP*         Up    25   00:21:30 Yes None None
P7             Gi0/0/0/0                *PtoP*         Up    26   00:21:30 Yes None None

Total adjacency count: 2
---[ XRSHOW END   ]---[ p6 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p7
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p7 ]---[ show version ]---
Fri Mar 17 15:06:19.338 UTC
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
System uptime is 1 day 16 hours 1 minute

---[ XRSHOW END   ]---[ p7 ]---[ show version ]---

---[ XRSHOW START ]---[ p7 ]---[ show platform ]---
Fri Mar 17 15:06:19.450 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p7 ]---[ show platform ]---

---[ XRSHOW START ]---[ p7 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:19.577 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P2             Gi0/0/0/3                *PtoP*         Up    24   00:21:30 Yes None None
P4             Gi0/0/0/4                *PtoP*         Up    23   00:21:31 Yes None None
P3             Gi0/0/0/1                *PtoP*         Up    28   00:21:31 Yes None None
P6             Gi0/0/0/0                *PtoP*         Up    22   00:21:31 Yes None None
P8             Gi0/0/0/2                *PtoP*         Up    27   00:21:31 Yes None None

Total adjacency count: 5
---[ XRSHOW END   ]---[ p7 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Host: p8
--------------------------------------------------------------------------------
Output Displayed:
--------------------------------------------------------------------------------
---[ XRSHOW START ]---[ p8 ]---[ show version ]---
Fri Mar 17 15:06:19.296 UTC
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
System uptime is 1 day 16 hours 1 minute

---[ XRSHOW END   ]---[ p8 ]---[ show version ]---

---[ XRSHOW START ]---[ p8 ]---[ show platform ]---
Fri Mar 17 15:06:19.415 UTC
Node              Type                       State             Config state
--------------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
---[ XRSHOW END   ]---[ p8 ]---[ show platform ]---

---[ XRSHOW START ]---[ p8 ]---[ show isis adjacency ]---
Fri Mar 17 15:06:19.551 UTC

IS-IS IGP Level-2 adjacencies:
System Id      Interface                SNPA           State Hold Changed  NSF IPv4 IPv6
                                                                               BFD  BFD
P4             Gi0/0/0/1                *PtoP*         Up    27   00:21:33 Yes None None
P7             Gi0/0/0/2                *PtoP*         Up    29   00:21:31 Yes None None

Total adjacency count: 2
---[ XRSHOW END   ]---[ p8 ]---[ show isis adjacency ]---


--------------------------------------------------------------------------------
Time taken for the program run: 5.35 seconds
(vntdvops) lab@netdevops:~/asyncxpct$

```
