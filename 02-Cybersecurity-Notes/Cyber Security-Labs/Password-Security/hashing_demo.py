import hashlib

password = "CyberMode@123"

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("SHA-256 Hash:", hashed_password)