#! /usr/bin/env python

import subprocess
import optparse

# Parsing arguments
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to rename MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

# Inputs from parsing
interface = options.interface
new_mac = options.new_mac

# Code to change MAC address
print("[+] Changing mac address of "+interface+" to "+new_mac+"\n")
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Changed mac address of "+interface+" to "+new_mac)
subprocess.call(["ifconfig", interface])
