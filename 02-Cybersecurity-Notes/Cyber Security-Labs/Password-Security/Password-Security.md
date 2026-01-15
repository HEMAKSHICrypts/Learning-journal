# Password Security Basics

## Why Password Security Matters
Weak or reused passwords are one of the biggest causes of data breaches.

## Common Password Attacks
- Brute Force Attack
- Dictionary Attack
- Credential Stuffing
- Rainbow Table Attack

## Best Practices
- Use long passwords (12+ characters)
- Never reuse passwords
- Use a password manager
- Always store passwords as hashes, not plain text

📊 netstat Output Explanation
The output mainly shows UNIX domain sockets, which are used for inter-process communication within the system.
Key Fields Observed:
Proto: unix → Local system communication
Type:
STREAM → Reliable, TCP-like communication
DGRAM → UDP-like communication
State:
CONNECTED → Active connection
LISTENING → Waiting for connections
📌 These sockets are normal and indicate healthy OS activity.
🔍 ss Command Analysis (Modern Tool)
Incorrect Command Attempted
ss-tuln
This resulted in:
command not found
❌ Error reason: Missing space between ss and options.
Correct Command
ss -tuln
Command Flags Explained
t → TCP connections
u → UDP connections
l → Listening ports
n → Numeric output (no DNS resolution)
🛠️ ss Tool Availability
If ss is missing, it can be installed using:

sudo apt install iproute2
ss is the modern replacement for netstat and is preferred in current Linux systems.
🔐 Cybersecurity Relevance
Identifies open and listening ports
Helps detect unauthorized services
Useful in network reconnaissance
Essential for incident response and system hardening
Understanding these tools helps security professionals monitor network behavior and identify suspicious connections.