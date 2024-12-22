#! /usr/bin/env python
import re
import subprocess
import optparse

def get_arguments ():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to rename MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not (options.interface):
        parser.error("Please enter interface, Use --help for more info")
    elif not (options.new_mac):
        parser.error("Please enter New MAC, Use --help for more info")
    return options

def change_mac(interface,new_mac):
    print("[+] Changing mac address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changed mac address of " + interface + " to " + new_mac)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('ascii')
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-] Could not fetch MAC address. Please check interface input")

(options) = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC Address > " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address changed successfully to " + current_mac)
else:
    print("[-] MAC address haven't changed")
