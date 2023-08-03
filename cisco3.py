from easysnmp import *
import getopt
import sys
import csv
import os.path
import socket
from collections import Counter


def usage():
    print("""
    -d, --device        Device to scan
    -c, --community     SNMP community string
    -v, --verbose
    -f, --follow        Follow all the cdp neighbors
    -i, --ignore        Disable the Ignore List

   """)

def cdpCacheDeviceID(session):
  list = []
  try:
    enterprises = '.1.3.6.1.4.1'
    cdpCacheDeviceOID = '.9.9.23.1.2.1.1.6'

    system_items = session.walk(enterprises + cdpCacheDeviceOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid.encode('utf-8').strip()
      #print(index.decode('utf8').strip())
      name = item.value
      index = item.oid
      index2 = index.replace('iso.3.6.1.4.1' + cdpCacheDeviceOID + '.', "")
      list.append([index2, name])
#      print('%s - %s' % (index2, name))
  except Exception as excp:
     print (excp)

  return list

def cdpCacheAddress(session):
  list = []

  try:
    enterprises = '.1.3.6.1.4.1'
    cdpCacheAddressOID = '.9.9.23.1.2.1.1.4'

    system_items = session.walk(enterprises + cdpCacheAddressOID)

    for item in system_items:
      localip = '.'.join([ str(ord(piece)) for piece in item.value ])
      #index = item.oid.encode('utf-8').strip()
      index = item.oid
      index2 = index.replace('iso.3.6.1.4.1' + cdpCacheAddressOID + '.', "")
      list.append([index2, localip])
#      print('%s - %s' % (index2, localip))

  except Exception as excp:
    print(excp)

  return list


def cdpRemotePort(session):
  list = []
  try:
    enterprises = '.1.3.6.1.4.1'
    cdpRemotePortOID = '.9.9.23.1.2.1.1.7'

    system_items = session.walk(enterprises + cdpRemotePortOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid.encode('utf-8').strip()
      #index2 = index.replace('enterprises' + cdpRemotePortOID + '.', "")
      name = item.value
      index = item.oid
      index2 = index.replace('iso.3.6.1.4.1' + cdpRemotePortOID + '.', "")
      list.append([index2, name])
#      print('%s - %s' % (index2, name))

  except Exception as excp:
     print (excp)

  return list


def cdpRemoteDeviceType(session):
  list = []
  try:
    enterprises = '.1.3.6.1.4.1'
    cdpRemoteDeviceTypeOID = '.9.9.23.1.2.1.1.8'

    system_items = session.walk(enterprises + cdpRemoteDeviceTypeOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid.encode('utf-8').strip()
      name = item.value
      index = item.oid
      index2 = index.replace('iso.3.6.1.4.1' + cdpRemoteDeviceTypeOID + '.', "")
      list.append([index2, name])
#      print('%s - %s' % (index2, name))

  except Exception as excp:
     print (excp)

  return list

def ifName(session):
  list = []
  try:
    #IfShortNameOID = '1.3.6.1.2.1.31.1.1.1.1'
    IfLongNameOID = '1.3.6.1.2.1.2.2.1.2'

    system_items = session.walk(IfLongNameOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid_index.encode('utf-8').strip()
      name = item.value
      index = item.oid_index
      list.append([index, name])
#      print('%s - %s' % (index, name))

  except Exception as excp:
     print (excp)

  return list

def VLANNames(session):
  list = []
  try:
    VLANSNamesOID = '1.3.6.1.4.1.9.9.46.1.3.1.1.2.1'

    system_items = session.walk(OID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid_index.encode('utf-8').strip()
      name = item.value
      index = item.oid_index
      list.append([index, name])
#      print('%s - %s' % (index, name))

  except Exception as excp:
     print (excp)

  return list


def ifDesc(session):
  list = []
  try:
    IfDescOID = '1.3.6.1.2.1.2.2.1.2'

    system_items = session.walk(IfDescOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid_index.encode('utf-8').strip()
      name = item.value
      index = item.oid_index
      list.append([index, name])
#      print('%s - %s' % (index, name))

  except Exception as excp:
     print (excp)

  return list


def ifSpeed(session):
  list = []
  try:
    IfSpeedOID = '1.3.6.1.2.1.2.2.1.5'
    IfHighSpeedOID = '1.3.6.1.2.1.31.1.1.1.15'

    system_items = session.walk(IfHighSpeedOID)

    for item in system_items:
      #speed = item.value.encode('utf-8').strip()
      #index = item.oid_index.encode('utf-8').strip()
      speed = item.value
      index = item.oid_index
      list.append([index, speed])
#      print('%s - %s' % (index, speed))

  except Exception as excp:
     print (excp)

  return list


def IsTrunk(session):
# this does not appear to work correctly will have to dig into more later
  list = []
  try:
    enterprises = '.1.3.6.1.4.1'
    IsTrunkOID = '.9.9.46.1.6.1.1.14'

    system_items = session.walk(enterprises + IsTrunkOID)

    for item in system_items:
      #name = item.value.encode('utf-8').strip()
      #index = item.oid.encode('utf-8').strip()
      name = item.value
      index = item.oid
      index2 = index.replace('iso.3.6.1.4.1' + IsTrunkOID + '.', "")
      if name == '2':
        trunk = 'Trunk'
      else:
        trunk = 'Not Trunk'
      list.append([index2, trunk])
#      print('%s - %s' % (index2, trunk))




  except Exception as excp:
     print (excp)

  return list


def combine (list1, list2, list3):
  tlist = []
  list = []
  for item1 in list1:
    for item2 in list2:
#      print(item1[0])
      if item1[0] == item2[0]:
        tlist.append([item1[0], item1[1], item2[1]])  #index, data1, data2
  for titem in tlist:
    for item3 in list3:
      if item3[0] == titem[0]:
        list.append([titem[1], titem[2], item3[1]])
  return list


def hostlookup(n, i):
  info1 = ''
  info2 = ''
  info3 = ''
  info4 = ''
  info5 = ''
  info6 = ''

  try:
    an = socket.gethostbyaddr(i)
    if verbose == True:
      print (n + ' ' + i)
    if an[2][0] != i:
      info1 = 'hostname does not match ip in dns'
      if verbose == True:
        print (info1)
        print (an)
    if an[0] == '':
      info2 = 'hostname not in dns'
      if verbose == True:
        print (info2)
        print (an)
  except:
    info5 = 'ip does not exist in dns - exception'

  try:
    ai = socket.gethostbyname(n)
    if ai != i:
      info3 = 'ip does not match name in dns'
      if verbose == True:
        print (info3)
        print (ai)
    if ai[0] == '':
      info4 = 'hostname not in dns'
      if verbose == True:
        print (info4)
        print (ai)
  except:
    info6 = 'hostname not in dns - exception'

  info = ''
  if info1 != '':
    info = info + '; ' + info1
  if info2 != '':
    info = info + '; ' + info2
  if info3 != '':
    info = info + '; ' + info3
  if info4 != '':
    info = info + '; ' + info4
  if info5 != '':
    info = info + '; ' + info5
  if info6 != '':
    info = info + '; ' + info6
  if info != '':
   info = info[2:]

  return info


def main ():

  printDifferences = True
  printFailed = True
  #printDifferences = False
  #printFailed = False

  ScannedList = []
  ToBeScannedList = []
  ScannedListFull = []
  if (ignore == True):
    IgnoreList = []
  else:
    IgnoreList = ['FAS6220', 'FAS8020', 'FAS8060', 'FAS8200', 'N10-S6100', 'UCS-FI-6', 'VMware ESX', 'cisco AIR-CAP', 'cisco AIR-AP', 'cisco AIR-LAP', 'cisco C9120AXI', 'Cisco IP Phone', 'Communicator (', 'Cisco ATA 1', 'Polycom SoundPoint IP', 'Polycom VVX']
  #IgnoreList = ['FAS6220', 'FAS8020', 'FAS8060', 'FAS8200', 'N10-S6100', 'UCS-FI-6', 'VMware ESX', 'Cisco IP Phone', 'Communicator (', 'Cisco ATA 1', 'Polycom SoundPoint IP', 'Polycom VVX']
  FailedToConnect = []

  #prepopulate the list, by doing it this way we will scan device 1 two times

  try:
    session = Session(hostname=device, community=community, version=2)

    names=cdpCacheDeviceID(session)
    ips=cdpCacheAddress(session)
    remotetype=cdpRemoteDeviceType(session)
#    speeds=ifSpeed(session)
    intName=ifName(session)
    desc=ifDesc(session)
    remoteport=cdpRemotePort(session)
#    trunk=IsTrunk(session)
    inv = combine(names, ips, remotetype)
#    print inv

    #populate scan list
#    for item in inv:
#      if (item not in ToBeScannedList):
#        ToBeScannedList.append(item)
    for item in inv:
      if (item not in ScannedList) and (item not in ToBeScannedList):
         found = 0
         for ignoreitem in IgnoreList:
           if item[2].find(ignoreitem) != -1:
             found = 1
         #we only add it if it wasn't found in the ignore list
         if found == 0:
           ToBeScannedList.append(item)

  except Exception as excp:
     print (excp)

  #temporary break point for now.
  count = 0
  maxCount = 10
  if follow == True:
#    while (len(ToBeScannedList) > 0) and (count < maxCount):
    while (len(ToBeScannedList) > 0):
      count = count + 1
      id = ToBeScannedList.pop(0)
      name = id[0]
      orgName = name
      #some of our devices have info like '(SSI151306CJ)' in the name returned, removing this as most also have bad info for IP address
      i = name.find('(')
      if i > 0:
        name = name[:i]
      lip = id[1]
      remote = id[2]
      error = ''
      desc = ''
      SysDevice = ''

      try:
        inv = []
        if verbose == True:
          print ("connecting to:  " + name + "(" + lip + ")")
        session = Session(hostname=name, community=community, version=2)
        description = session.get('.1.3.6.1.2.1.1.1.0')
        #description = session.get('sysDescr.0')
        desc = description.value.replace('\r\n', ';')
        desc = desc.replace(',', '')
        desc = desc.encode('utf-8').strip()
        SysDevice = session.get('.1.3.6.1.4.1.9.5.1.2.16.0')
        SysDevice = SysDevice.value.encode('utf-8').strip()
        names=cdpCacheDeviceID(session)
        ips=cdpCacheAddress(session)
        remotetype=cdpRemoteDeviceType(session)
#        speeds=ifSpeed(session)
        for ip in ips:
          if ip[1] == lookup:
            print ("found it " + name)
        for item in names:
          if item[1] == lookup:
            print ("found it " + name)
        inv = combine(names, ips, remotetype)
      except EasySNMPConnectionError as excp:
        if verbose == True:
          print ("  failed to connect by Name, retrying with IP")
        error = "failed to connect by Name"

        try:
          inv = []
          if verbose == True:
            print ("connecting to:  " + lip)
          session = Session(hostname=lip, community=community, version=2)
          description = session.get('.1.3.6.1.2.1.1.1.0')
          desc = description.value.replace('\r\n', ';')
          desc = desc.replace(',', '')
          desc = desc.encode('utf-8').strip()
          SysDevice = session.get('.1.3.6.1.4.1.9.5.1.2.16.0')
          SysDevice = SysDevice.value.encode('utf-8').strip()

          names=cdpCacheDeviceID(session)
          ips=cdpCacheAddress(session)
          remotetype=cdpRemoteDeviceType(session)
#          speeds=ifSpeed(session)

          inv = combine(names, ips, remotetype)
        except EasySNMPConnectionError as excp:
          if verbose == True:
            print ("  failed to connect by IP")
          error = "failed to connect by Name and IP"
          FailedToConnect.append([name, lip, remote, SysDevice, desc, error])

        except EasySNMPTimeoutError as excp:
          if verbose == True:
            print ("  timeout by Name")
          error = "timed out"
          FailedToConnect.append([name, lip, remote, SysDevice, desc, error])

      except EasySNMPTimeoutError as excp:
        if verbose == True:
          print ("  timeout by Name")
        error = "timed out"
        FailedToConnect.append([name, lip, remote, SysDevice, desc, error])

      info = hostlookup(name, lip)
      error = error + '; ' + info
      if error[0] == ';':
        error = error[2:]

      #orgName replaced name in following 2 because of loop created on ones "fixed"...
      ScannedListFull.append([orgName, lip, remote, SysDevice, desc, error])
      ScannedList.append([orgName, lip, remote])

      for item in inv:
        if (item not in ScannedList) and (item not in ToBeScannedList):
           found = 0
           for ignoreitem in IgnoreList:
             if item[2].find(ignoreitem) != -1:
               found = 1
           #we only add it if it wasn't found in the ignore list
           if found == 0:
             ToBeScannedList.append(item)
      if verbose == True:
        print ("Scanned:  " + str(len(ScannedList)) + " Left: " + str(len(ToBeScannedList)))

    print("1")
    with open('current.csv', 'w') as csvfile:
      current = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
      current.writerow(["name", "ip", "remote", "model", "description", "error"])
      for item in ScannedListFull:
        current.writerow(item)

    if os.path.isfile('baseline.csv'):
      pass
    else:
      print("2")
      with open('baseline.csv', 'w') as csvfile:
        baseline = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        baseline.writerow(["name", "ip", "remote", "model", "description", "error"])
        for item in ScannedListFull:
          baseline.writerow(item)

    with open('baseline.csv', 'r') as t1, open('current.csv', 'r') as t2:
      print("3")
      baseline = t1.readlines()
      current = t2.readlines()

    if (printDifferences == True):
      print ("--- Differences in Baseline ---")
      for line in baseline:
        if line not in current:
          print (line)
          pass

      print ("--- Differences in Current ---")
      for line in current:
        if line not in baseline:
          print (line)
          pass


    if (printFailed == True):
      print ("--- Failed to Connect to ---")
      for line in FailedToConnect:
        print (line)

  else:
    print (ToBeScannedList)


try:
     opts, args = getopt.getopt(sys.argv[1:], "c:d:l:fiv",
     [ 'community=', 'device=', 'lookup=', 'ignore', 'verbose', 'follow' ]
     )
except getopt.error:
     usage()

community = device = ignore = verbose = follow = lookup = None

for opt, val in opts:
    if opt in ('-c', '--community'):
        community = val
    if opt in ('-d', '--device'):
        device = val
    if opt in ('-i', '--ignore'):
        ignore = True
    if opt in ('-f', '--follow'):
        follow = True
    if opt in ('-v', '--verbose'):
        verbose = True
    if opt in ('-l', '--lookup'):
        lookup = val



if __name__ == '__main__':
    main()

