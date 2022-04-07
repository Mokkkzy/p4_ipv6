import argparse
from email import message
import imp
import sys
import socket
import random
import struct

from scapy.all import sendp,send,get_if_list,get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether,IPv6,UDP

def get_if():
    ifs = get_if_list()
    iface = None
    for i in get_if_list():
        if "eth0" in i:
            iface = i
            break;
        if not iface:
            print('Cannot find eth0 interface')
            exit(1)
        return iface

def main():
    if len(sys.argv)<3:
        print("pass 3 arguments:<source><destination> "<message>"")
        exit(1)
    saddr = sys.argv[1]
    addr = sys.argv[2]
    iface = get_if()
    
    print("sending on interface %s to %s"%(iface,str(addr)))
    pkt = Ether(src=get_if_hwaddr(iface),dst="ff:ff:ff:ff:ff:ff")/ IPv6(src=saddr,dst=addr) / UDP(dport=4321, sport=1234) / sys.argv[3]
    pkt.show2()
    sendp(pkt,iface=iface,verbose=False)
    
if __name__ == '__main__':
    main()