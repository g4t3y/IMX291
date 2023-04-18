## a script that may help in seing the difference config changes (via CMS / ONVIF) have made
# useage:
# python -m investigate

from dvrip import DVRIPCam
from time import sleep
from deepdiff import DeepDiff
from pprint import pprint

# Variables
# camera IP Address
host_ip = '192.168.42.10'

cam = DVRIPCam(host_ip, user='admin', password='')
if cam.login():
	print("Success! Connected to " + host_ip)
else:
	print("Failure. Could not connect.")

## Change "options" below!
latest = None
while True:
    current = cam.get_info("Network") # or "Camera", "General", "Simplify.Encode", "NetWork", "NetWork.OnlineUpgrade"
    if latest:
        diff = DeepDiff(current, latest)
        if diff == {}:
            print("Nothing changed")
        else:
            pprint(diff['values_changed'], indent = 2)
    latest = current
    input("Change camera setting via UI and then press Enter,"
          " or double Ctrl-C to exit\n")

