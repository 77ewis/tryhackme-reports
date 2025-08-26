Lab Title: W1seGuy

Objective:

The purpose of this lab was to analyze and decrypt a XOR-encrypted message provided by a remote server. The goal was to derive the encryption key from a known plaintext, decrypt the first flag locally, and then submit the key to retrieve the second flag. This lab demonstrates practical cryptography skills and Python scripting for cryptanalysis.

Tools / Concepts Used:

Tools: Python 3, Netcat (nc)

Concepts: XOR encryption, known-plaintext attacks, ASCII encoding/decoding, TCP client-server interaction, key repetition in ciphers

Steps Taken:

Connection and Data Acquisition:

Connected to the server on the provided IP and port 1337 using Netcat to retrieve the XOR-encrypted hexadecimal string representing the first flag.

Hexadecimal Conversion:

Converted the received hex string to bytes in Python to facilitate analysis and manipulation of the ciphertext.

Key Derivation Using Known Plaintext:

Observed that the server used a 5-character repeating key for XOR encryption.

Used the assumption that the plaintext starts with THM{ and ends with } to derive the key.

XORed the first four ciphertext bytes with THM{ to recover the first four characters of the key.

XORed the last ciphertext byte with } to recover the fifth key character.

Decryption of Flag 1:

Implemented a Python script (wiseguy.py) to XOR the ciphertext with the derived key repeatedly.

Successfully decrypted the full first flag locally.

Retrieval of Flag 2:

Submitted the derived 5-character key to the server via Netcat.

The server validated the key and returned the second flag, completing the challenge.

Findings / Outcome:

Flag 1: Decrypted Locally

Derived 5-character key: Fully recovered and used to decrypt the ciphertext.

Flag 2: Retrieved successfully from the server after submitting the key.

Demonstrated the vulnerability of XOR encryption to known-plaintext attacks when the key is short and repeats.

Reflection / Learnings:

Gained practical experience with XOR cryptography and key repetition vulnerabilities.

Developed Python scripts to automate cryptanalysis tasks efficiently.

Learned the importance of key length and randomness in secure encryption.

Next steps: Explore more advanced encryption schemes and automate key discovery for larger challenges.



Decryption Script:
The Python script used to derive the key and decrypt the flag is included in this folder as wiseguy.py.
