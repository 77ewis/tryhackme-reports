#!/usr/bin/env python3

hex_string = "3f091821235a203934272e39211b271f753631302a2f276932070d2c320619352c6a2619391a282e"
xored_bytes = bytes.fromhex(hex_string)

known_start = "THM{"
key_bytes = []

for i, ch in enumerate(known_start):
    key_bytes.append(xored_bytes[i] ^ ord(ch))

derived_key_start = ''.join([chr(k) for k in key_bytes])
print("First 4 characters of key:", derived_key_start)

last_key_char = xored_bytes[-1] ^ ord('}')
full_key = derived_key_start + chr(last_key_char)
print("Full 5-character key:", full_key)

def xor_decrypt(data_bytes, key):
    return ''.join([chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(data_bytes)])

flag1 = xor_decrypt(xored_bytes, full_key)
print("Decrypted Flag 1:", flag1)
print("Use this key to submit to the server for Flag 2:", full_key)