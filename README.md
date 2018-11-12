You can query a single device or use the follow feature for it to find all neighbors, via SNMP and pull information such as the description, info about the connected device, ip and hostname:

Example output:
"x-yyyy-2570-s-poe.somedomain.xyz","10.x.x.x","cisco WS-C2960S-24PS-L","WS-C2960S-24PS-L","Cisco IOS Software C2960S Software (C2960S-UNIVERSALK9-M) Version 15.0(2)SE10a RELEASE SOFTWARE (fc3);Technical Support: http://www.cisco.com/techsupport;Copyright (c) 1986-2016 by Cisco Systems Inc.;Compiled Thu 03-Nov-16 13:52 by prod_rel_team",""
"x-yyyy-235-poe.somedomain.xyz","10.x.x.x.","cisco WS-C2960-24PC-S","WS-C2960-24PC-S","Cisco IOS Software C2960 Software (C2960-LANLITEK9-M) Version 15.0(2)SE2 RELEASE SOFTWARE (fc1);Technical Support: http://www.cisco.com/techsupport;Copyright (c) 1986-2013 by Cisco Systems Inc.;Compiled Tue 05-Feb-13 12:41 by prod_rel_team",""
"x-yyyy-poe-2.somedomain.xyz","10.x.x.x.","cisco WS-C2960X-24PS-L","WS-C2960X-24PS-L","Cisco IOS Software C2960X Software (C2960X-UNIVERSALK9-M) Version 15.0(2)EX1 RELEASE SOFTWARE (fc1);Technical Support: http://www.cisco.com/techsupport;Copyright (c) 1986-2013 by Cisco Systems Inc.;Compiled Fri 28-Jun-13 13:20 by prod_rel_team",""

Needed something to pull layer 2 inventory of devices that the switches/routers knew about.  

usage:
python cisco.py -d [some switch] -vf -c [read community name]
