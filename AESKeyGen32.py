import os
import binascii

# Generate a 16-byte (128-bit) AES key
key = os.urandom(16)

# Convert the key to a 32-character hexadecimal format
key_hex = binascii.hexlify(key).decode('utf-8').upper()

# Verify that the length is 32 characters
print("32-character AES key:", key_hex)
print("Key length:", len(key_hex))