#! /usr/bin/env python

# Importing Module
import subprocess

# variable for user input 
interface = input("Interface > ")
new_mac = input("New mac > ")

# Code to change MAC address
print("[+] Changing mac address of "+interface+" to "+new_mac+"\n")
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Changed mac address of "+interface+" to "+new_mac)
subprocess.call(["ifconfig", interface])
