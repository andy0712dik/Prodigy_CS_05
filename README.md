# Prodigy_CS_05
# **Network Packet Sniffer**

A Python-based network packet sniffer built using the `Scapy` library. This tool captures network packets in real-time, extracts relevant details such as source/destination IP addresses and protocol types, and displays them in a readable format.  

---

## **Features**
- **Real-Time Packet Sniffing**: Captures packets on a specified network interface.  
- **Protocol Identification**: Identifies common protocols like TCP, UDP, and ICMP.  
- **Payload Extraction**: Attempts to decode and display the packet payload.  
- **Customizable Interface**: Works on any valid network interface (e.g., `eth0`, `wlan0`).  

---

## **How It Works**
1. **Packet Capture**: Uses `Scapy` to capture packets from the specified network interface.  
2. **Protocol Mapping**: Maps protocol numbers to human-readable names (e.g., `6 → TCP`, `17 → UDP`).  
3. **Payload Handling**: Decodes and displays payload data when possible, with graceful handling for undecodable payloads.  
4. **Output Details**: Displays the following for each captured packet:  
   - Source IP  
   - Destination IP  
   - Protocol (e.g., TCP, UDP, ICMP)  
   - Payload (decoded or raw)  

---

## **Usage Instructions**
### **Requirements**
1. **Python 3.6 or later**  
2. **Scapy library**: Install with:  
   ```bash
   pip install scapy
   ```

### **Running the Sniffer**
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/network-packet-sniffer.git
   cd network-packet-sniffer
   ```
2. Run the script with administrative/root privileges (required for sniffing):  
   ```bash
   sudo python packet_sniffer.py
   ```
3. Enter the network interface to monitor when prompted (e.g., `eth0` or `wlan0`).  

---

## **Output Example**
```plaintext
[*] Sniffing on wlan0...
Source IP: 192.168.1.2  
Destination IP: 93.184.216.34  
Protocol: TCP  
Payload: GET / HTTP/1.1  
```

---

## **Security Note**
- Ensure you have explicit permission to capture network packets on the specified interface. Unauthorized sniffing may violate privacy laws and organizational policies.  

---

## **Use Cases**
- **Network Analysis**: Monitor real-time traffic for debugging or learning.  
- **Protocol Understanding**: Learn about TCP/IP, UDP, and ICMP in action.  
- **Payload Inspection**: Extract and analyze packet payloads for insights.  

---

## **Limitations**
- Payload decoding depends on the protocol and may fail for encrypted or non-standard payloads.  
- Requires root or administrative privileges to run.  

---

## **License**
This project is licensed under the **MIT License**. Feel free to use, modify, and share responsibly.  

---

## **Contributions**
Contributions, suggestions, and feedback are welcome! Open an issue or submit a pull request to enhance this project.  
