from scapy.all import *

conf.iface = "eth0"

source = "192.168.1.121"
target = "192.168.1.10"
message = "hello world"

packet = IP(dst = target, src = source) / ARP() / Raw(load = message)
print(packet)
send(packet)
