import get_local_ip_address as host_ip
import scapy.all as scapy
from ipaddress import IPv4Interface

host_ip_address = host_ip.get_local_ip_address()
network=str(IPv4Interface(host_ip_address+"/24").network)
scapy.arping(network)