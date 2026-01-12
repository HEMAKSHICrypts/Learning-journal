# Networking Basics (Cybersecurity Notes)

## 1. IP Address
An IP Address is a unique number assigned to each device on a network.  
Example: 192.168.1.1

## 2. MAC Address
A MAC Address is a hardware address burned into the network card.  
Example: AB:CD:EF:12:34:56

## 3. DNS
DNS (Domain Name System) translates domain names like google.com into IP addresses.

## 4. Port Number
A port number identifies a specific process/service on a device.  
Example:  
- 80 → HTTP  
- 443 → HTTPS  
- 22 → SSH

## 5. HTTP vs HTTPS
HTTP sends data in plain text.  
HTTPS encrypts data and is secure.

## 6. Firewall
A firewall monitors and controls network traffic to protect systems from attacks.



# Networking Basics 

## 1. IP Address
An IP address uniquely identifies a device on a network. It can be IPv4 or IPv6.

## 2. Default Gateway
The default gateway connects the local network to external networks like the internet.

## 3. Ping Command
Ping is used to test connectivity between two systems and measure network latency.

## Commands Used
- ip a
- ip route
- ping google.com


## DNS Issue Observed
Ping to google.com failed due to DNS resolution error.
Error: Temporary failure in name resolution

This indicates that IP connectivity was present but DNS was not configured properly.


## Ping Test Result
Ping to google.com was successful after DNS configuration.
Packets were transmitted and received successfully with low latency.

Ping command was terminated using CTRL + C.


## Key Learnings
- Understood how devices communicate over networks
- Learned how DNS issues affect connectivity
- Practiced real networking commands instead of theory