from scapy.all import sniff, IP, TCP, UDP # type: ignore
def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:  # TCP
            protocol_name = "TCP"
            if TCP in packet:
                payload = str(packet[TCP].payload)
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
            if UDP in packet:
                payload = str(packet[UDP].payload)
        else:
            protocol_name = "Other"
            payload = "N/A"

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol_name}")
        print(f"Payload: {payload}")
        print("-" * 50)

def start_sniffing(interface=None):
    print("Starting packet capture...")
    sniff(iface=interface, prn=process_packet)

if __name__ == "__main__":
    interface = "eth0"  # Replace with your network interface
    start_sniffing(interface)
