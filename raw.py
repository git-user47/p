import socket
import struct

s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)

print("Start capturing packets...")

try:
    while True:
        packet,addr=s.recvfrom(65535)

        if len(packet)<20:
            continue

        ip_header=packet[:20]
        iph=struct.unpack('!BBHHHBBH4s4s',ip_header)
        version=iph[0]>>4
        total_length=iph[2]
        proto=iph[6]
        source_address=socket.inet_ntoa(iph[8])
        destination_address=socket.inet_ntoa(iph[9])

        if proto==1:
            protocol_name="ICMP"
        elif proto==6:
            protocol_name="TCP" 
        elif proto==17:
            protocol_name="UDP"
        else:
            protocol_name="Other"

except KeyboardInterrupt:
    print("Packet capturing stopped")

s.close()