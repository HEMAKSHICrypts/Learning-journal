# Commands Used – Network & Linux Basics

## Networking Commands

ip a
ip route
ping google.com

## Linux File Permission Commands

ls -l
chmod 644 public.txt
chmod 600 secret.txt
chmod u+x file
chown user:group file

## Network Scanning (Intro Level)

nmap scanme.nmap.org
sudo nmap scanme.nmap.org
## Linux File Permissions

- chmod 644 → Owner: read/write, Others: read
- chmod 700 → Owner only (used for scripts/keys)
- chown → Change ownership (critical in servers)
- stat → View detailed file metadata

Security Insight:
Misconfigured permissions are a common cause of privilege escalation.