# useage:
# python -m imx_checkconfig
# references: https://github.com/CroatianMeteorNetwork/RMS/blob/master/Utils/CameraControl.py https://www.onvif.org/onvif/ver20/util/operationIndex.html https://github.com/alexshpilkin/dvrip/tree/master/dvrip

from dvrip import DVRIPCam
from time import sleep
import ipaddress as ip
import json
import pprint

##### comment out as necessary ####
# camera IP Address
host_ip = '192.168.42.10'


cam = DVRIPCam(host_ip, user='admin', password='password123')
if cam.login():
	print("\nSuccess! Connected to " + host_ip)
else:
	print("Failure. Could not connect.")

print("\nCamera time:", cam.get_time())

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

nue=cam.get_info('NetWork.Upnp.Enable')
print('\nUPNP enabled?:')
pprint.pprint(nue)

noac=cam.get_info("NetWork.OnlineUpgrade.Enable.")
print('\nOnline Automatic Upgrade enabled? True/False:')
pprint.pprint(noac)
print()

noa=cam.get_info('NetWork.OnlineUpgrade.AutoCheck')
print('When Online Automatic Upgrade is enabled this can then be disabled')
print('Online Automatic Upgrade Auto Check enabled? True/False:')
pprint.pprint(noa)

nos=cam.get_info('NetWork.OnlineUpgrade.ServerAddr')
print('\nAutomatic update server:')
pprint.pprint(nos)

nne=cam.get_info('NetWork.NetIPFilter.Enable')
print('\nIP filtering enabled?:')
pprint.pprint(nne)

#nnb=cam.get_info('NetWork.NetIPFilter.Banned')
#print('IPs Banned:')
#pprint.pprint(nnb)

#nnt=cam.get_info('NetWork.NetIPFilter.Trusted')
#print('IPs Trusted:')
#pprint.pprint(nnt)

dmd=cam.get_info('Detect.MotionDetect.[0].Enable')
print('\nMotion detection alarm enabled?')
pprint.pprint(dmd)

#print(cam.get_upgrade_info())
print()
##print(cam.get_system_info())
gsi=cam.get_system_info()
#pprint.pprint(gsi)
print('Serial Number:', (gsi['SerialNo']))
print('System:', (gsi['SoftWareVersion']))
print('Build date:', (gsi['BuildTime']))

#print(cam.get_info("NetWork.NetCommon.HostName"))

#print(cam.get_general_info())

################### VVV WORKING VVV ###########################

# Enable/disable cloud support 'True/False'
#cloudEnabled = False
#cam.set_info("NetWork.Nat", { "NatEnable" : cloudEnabled })

#print(cam.get_info("NetWork.Nat.NatEnable"))

# This returns all tiered under "NetWork"
#n=cam.get_info("NetWork")
#pprint.pprint(n)

#nn=cam.get_info('NetWork.Nat')
#pprint.pprint(nn)

print('\Obscure XMEyeconfig follows:\n')
# This returns all tiered under "NetWork.Nat"
xm=cam.get_info('NetWork.Nat')
#This gets the cloud config enabled 'True/False' status.
print('Cloud Config [XMeye] Enabled:', cam.get_info('NetWork.Nat.NatEnable'))
print('XMeye Cloud server  : ', (xm['Addr']))
print('DNS Server 1        : ', iptoString(xm['DnsServer1']))
print('DNS Server 2        : ', iptoString(xm['DnsServer2']))

nc=cam.get_info("NetWork.NetCommon")
#print(cam.get_info("NetWork.NetCommon"))
#pprint.pprint(nc)
print('\nIP camera network config:')
print('Hostname            : ', (nc['HostName']))
print('IP Address          : ', iptoString(nc['HostIP']))
print('Subnet mask         : ', iptoString(nc['Submask']))
print('Gateway             : ', iptoString(nc['GateWay']))

nnd=cam.get_info('NetWork.NetDNS')
#pprint.pprint(nnd)
print('DNS Server 1        : ', iptoString(nnd['Address']))
print('DNS Server 2        : ', iptoString(nnd['SpareAddress']))

#print(cam.get_upgrade_info())

# Disconnect
cam.close()