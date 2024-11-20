import scapy.all as scapy

def protocol_name(protocol_number):
    protocol_map = {
        1: 'ICMP',
        6: 'TCP',
        17: 'UDP',
    }
    return protocol_map.get(protocol_number, str(protocol_number))  # Default to number if not found

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = protocol_name(packet.proto)  # Get the protocol name

        # Handling the payload based on the protocol
        payload = packet.payload
        if hasattr(payload, 'load'):
            payload_data = payload.load.decode(errors='ignore')  # Decoding payload if possible
        else:
            payload_data = str(payload)

        # Display packet details
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload_data}\n")

def start_sniffing(interface):
    # Start sniffing packets on the specified network interface
    print(f"[*] Sniffing on {interface}...")
    scapy.sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (e.g., eth0 or wlan0): ")
    start_sniffing(interface)
