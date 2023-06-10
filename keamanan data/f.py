def vigenere_encrypt(plaintext, key):
    # Convert plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()
    # Initialize the ciphertext variable
    ciphertext = ""
    # Loop through the plaintext
    for i in range(len(plaintext)):
        # Get the i-th character of the plaintext and key
        plain_char = plaintext[i]
        key_char = key[i % len(key)]
        # Encrypt the plain character using the key character
        cipher_char = chr(((ord(plain_char) + ord(key_char)) % 26) + 65)
        # Add the encrypted character to the ciphertext
        ciphertext += cipher_char
    # Return the ciphertext
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    # Convert ciphertext and key to uppercase
    ciphertext = ciphertext.upper()
    key = key.upper()
    # Initialize the plaintext variable
    plaintext = ""
    # Loop through the ciphertext
    for i in range(len(ciphertext)):
        # Get the i-th character of the ciphertext and key
        cipher_char = ciphertext[i]
        key_char = key[i % len(key)]
        # Decrypt the cipher character using the key character
        plain_char = chr(((ord(cipher_char) - ord(key_char)) % 26) + 65)
        # Add the decrypted character to the plaintext
        plaintext += plain_char
    # Return the plaintext
    return plaintext

plaintext = "HELLO WORLD"
key = "SECRET"
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = vigenere_decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
