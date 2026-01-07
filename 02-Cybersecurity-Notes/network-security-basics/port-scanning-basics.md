# Port Scanning Basics

## What is a Port?
A port is a communication endpoint on a computer that allows software to send and receive data.

## Why Hackers Scan Ports?
- To find open doors into a system
- To check which services are running
- To identify vulnerabilities in outdated services

## Common Ports
- 22 → SSH
- 80 → HTTP
- 443 → HTTPS
- 53 → DNS

1. What is Port Scanning?
Port scanning is a technique used to identify open ports and running services on a target machine. It helps security professionals find potential entry points and understand how a system is exposed to the internet.
2. Commands Used

nmap scanme.nmap.org

nmap -sV -sC scanme.nmap.org

3. Explanation of Each Command
Command 1: nmap scanme.nmap.org
Performs a basic scan
Shows open ports
Displays the state (open/closed/filtered)
Identifies basic service info
Command 2: nmap -sV -sC scanme.nmap.org
-sV → Detects service versions
-sC → Runs default NSE (Nmap Scripting Engine) scripts
Provides more detailed info about services
Helps identify possible vulnerabilities

4. Output Screenshot
Add your terminal screenshot here.
(Example: attach the output showing open ports like 22, 80, etc.)