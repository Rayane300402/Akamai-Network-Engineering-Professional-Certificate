# Networking Fundamentals – Simple Peer-to-Peer Network  
Creating and Testing a Basic Direct Connection in Packet Tracer

This section introduces the foundational concept of networking: enabling two devices to communicate directly. The exercise demonstrates how hardware, cabling, and protocol configuration work together to establish connectivity between two PCs.

---

## Task: Create a Simple Network

In this task, a minimal network consisting of **two PCs connected directly with a Copper Cross-Over cable** is configured. Each device is assigned a **static IPv4 address**, and connectivity is verified using the `ping` command.

### What Was Done
- Added **two PC end devices** to the Packet Tracer logical workspace.
- Connected **PC0** and **PC1** using a **Copper Cross-Over Ethernet cable**.
- Assigned **static TCP/IP settings** to each computer:
  - **PC0:** `192.168.1.10` with subnet mask `255.255.255.0`
  - **PC1:** `192.168.1.11` with subnet mask `255.255.255.0`
- Confirmed the interface link status (both link lights **green**).
- Used the `ping` command to verify network connectivity.

---

### How to Test Functionality
1. Open **PC1 → Desktop → Command Prompt**
2. Verify its IP configuration:
   ```sh
   ipconfig
3. Test connectivity to PC0:
   ```sh
   ping 192.168.1.10
4. Expected Output: 4 reply messages confirming successful two-way communication.
