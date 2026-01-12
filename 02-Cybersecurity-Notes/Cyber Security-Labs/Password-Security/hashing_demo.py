import hashlib

# Original password (example only, never hardcode real passwords)
password = "CyberMode@123"

# Convert password to bytes and apply SHA-256 hashing
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Output results
print("Original Password:", password)
print("SHA-256 Hash:", hashed_password)


# Demonstrating another hashing algorithm (MD5 - insecure, for learning only)
md5_hash = hashlib.md5(password.encode()).hexdigest()
print("MD5 Hash:", md5_hash)