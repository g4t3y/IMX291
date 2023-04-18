# useage:
# python -m imx_secureconfig
# references: https://github.com/CroatianMeteorNetwork/RMS/blob/master/Utils/CameraControl.py https://www.onvif.org/onvif/ver20/util/operationIndex.html https://github.com/alexshpilkin/dvrip/tree/master/dvrip

from dvrip import DVRIPCam
from time import sleep

import ipaddress as ip
#import argparse
import json
import pprint
import time

# some variables:
# camera IP Address
host_ip = '192.168.42.10'

# This ensures the operator is aware the script can make changes to the IP camera configuration
while True:
   answer = input('This will CHANGE the IP camera configuration, enter "y" to continue, "n" to quit: ')
   if answer.lower().startswith("y"):
      print("ok, carry on then")
      time.sleep(2)
      break
   elif answer.lower().startswith("n"):
      print("ok, byeee")
      exit()

# This logs into the camera, note empty password field
cam = DVRIPCam(host_ip, user='admin', password='')
if cam.login():
	print("\nSuccess! Connected to " + host_ip)
else:
	print("Failure. Could not connect.")

print("\nCamera time:", cam.get_time())
print()

# This converts the IP addresses which are stored as Hex to human readable format
def iptoString(s):
    """Convert an IP address in hex network order to a human readable string 
    Args:
        s (string): the encoded IP address eg '0x0A01A8C0' 
    Returns:
        string: human readable IP in host order eg '192.169.1.10'
    """
    a=s[2:]
    addr='0x'+''.join([a[x:x+2] for x in range(0,len(a),2)][::-1])
    ipaddr=ip.IPv4Address(int(addr,16))
    return ipaddr

#ggi=cam.get_general_info()
#pprint.pprint(ggi)

##print(cam.get_system_capabilities())
#gsc=cam.get_system_capabilities()
#print("get_system_capabilities:")
#pprint.pprint(gsc)

print('Device Hostname:')
print(cam.get_info("NetWork.NetCommon.HostName"))
print()

nue=cam.get_info('NetWork.Upnp.Enable')
print('UPNP enabled?:')
pprint.pprint(nue)
print()

noa=cam.get_info('NetWork.OnlineUpgrade.AutoCheck')
print('Online Automatic Upgrade enabled? 0=False:')
pprint.pprint(noa)
print()

nos=cam.get_info('NetWork.OnlineUpgrade.ServerAddr')
print('Automatic update server:')
pprint.pprint(nos)
print()

nne=cam.get_info('NetWork.NetIPFilter.Enable')
print('IP filtering enabled?:')
pprint.pprint(nne)
print()

#nnb=cam.get_info('NetWork.NetIPFilter.Banned')
#print('IPs Banned:')
#pprint.pprint(nnb)

#nnt=cam.get_info('NetWork.NetIPFilter.Trusted')
#print('IPs Trusted:')
#pprint.pprint(nnt)

#print(cam.get_upgrade_info())

##print(cam.get_system_info())
#gsi=cam.get_system_info()
#pprint.pprint(gsi)

# print(cam.get_general_info())

## Enable/disable Video Motion Alarm 'True/False'
AlarmEnabled=False
cam.set_info("Detect.MotionDetect.[0]", { "Enable" : AlarmEnabled })

## print the result of the change
dmd=cam.get_info('Detect.MotionDetect.[0].Enable')
print('\nAfter change is the Motion detection alarm enabled?')
pprint.pprint(dmd)

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

## Enable/disable online upgrades 'True/False'
## It is likely this setting controls automatic updates being 'pushed' by update services
OnlineUpgrade=False
cam.set_info("NetWork.OnlineUpgrade", { "Enable" : OnlineUpgrade })

## print the result of the change
## This is accurate for Setting > Advanced > Automaintain: Online Upgrade: Automatic firmware...
noue=cam.get_info("NetWork.OnlineUpgrade.Enable.")
print('\nAfter change is Online Automatic Upgrade enabled?:')
pprint.pprint(noue)
print()

#print('Setting > Advanced > Automaintain: Online Upgrade: enabled?')
#print(cam.get_info("NetWork.OnlineUpgrade.Enable."))

## Enable/disable automatic online upgrade autocheck 'True/False'
## It is likely this setting controls automatic updates being 'requested'
AutoOnlineUpgrade=False
cam.set_info("NetWork.OnlineUpgrade", { "AutoCheck" : AutoOnlineUpgrade })

## print the result of the change
noac=cam.get_info('NetWork.OnlineUpgrade.AutoCheck')
print('\nAfter change is Automatic Upgrade AutoCheck enabled?' )
pprint.pprint(noac)
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

#print(cam.get_info("NetWork.Nat.NatEnable"))

# This returns all tiered under "NetWork"
#n=cam.get_info("NetWork")
#pprint.pprint(n)

#nn=cam.get_info('NetWork.Nat')
#pprint.pprint(nn)

## This will Enable/disable XMeye cloud support 'True/False'
cloudEnabled=False
cam.set_info("NetWork.Nat", { "NatEnable" : cloudEnabled })

## This section reports the current XMeye cloud configuration
xm=cam.get_info('NetWork.Nat')
#This gets the cloud config enabled 'True/False' status.
print('Cloud Config [XMeye] \nEnabled             : ', cam.get_info('NetWork.Nat.NatEnable'))
print('XMeye Cloud server  : ', (xm['Addr']))
#print('DNS Server 1        : ', iptoString(xm['DnsServer1']))
#print('DNS Server 2        : ', iptoString(xm['DnsServer2']))

## This section reports the current camera IP configuration
nc=cam.get_info("NetWork.NetCommon")
#print(cam.get_info("NetWork.NetCommon"))
#pprint.pprint(nc)
print('\nIP camera network config:')
print('Hostname            : ', (nc['HostName']))
print('IP Address          : ', iptoString(nc['HostIP']))
print('Subnet mask         : ', iptoString(nc['Submask']))
print('Gateway             : ', iptoString(nc['GateWay']))

## This section manages the changing of the Network DNS lookup addresses
## note, if no addresses are entered e.g. '0.0.0.0', lookups are still apparently made using embedded addresses
## setting the IPs to DNS sinkhole / pihole hosts is suggested to prevent resolution
## also note the Hex format is apparently non standard...
## see ipconvert3.py for conversion script

#print('hex DNS 1')
#print(cam.get_info("NetWork.NetDNS.Address"))
#print(cam.get_info("NetWork.NetDNS.SpareAddress"))

## setting the primary DNS name, change the hex number to the IP required with ipconvert3.py
## NB odd hex format?
dns1=0x00000000
cam.set_info("NetWork.NetDNS", { "Address" : dns1 })

## setting the spare DNS name, change the hex number to the IP required with ipconvert3.py
dns2=0x00000000
cam.set_info("NetWork.NetDNS", { "SpareAddress" : dns2 })

## check the address changes are as expected due to the odd format
nnd=cam.get_info('NetWork.NetDNS')
#pprint.pprint(nnd)
print('DNS Server 1        : ', iptoString(nnd['Address']))
print('DNS Server 2        : ', iptoString(nnd['SpareAddress']))
print()

#print(cam.get_upgrade_info())

## Disconnect the session
cam.close()