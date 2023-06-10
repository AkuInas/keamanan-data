import random

# membuat karakter dan kunci
karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + " "
karakter = list(karakter)
kunci = karakter.copy()
random.shuffle(kunci)
print(kunci)
# enkripsi
plaintext = input("Masukan plain text : ")
ciphertext = ""

for kata in plaintext:
    index = karakter.index(kata)
    ciphertext += kunci[index]

print(f"enkripsi: {ciphertext}")

# dekripsi
ciphertext = input("Masukan cipher text: ")
plaintext = ""

for kata in ciphertext:
    index = kunci.index(kata)
    plaintext += karakter[index]

print(f"plain text : {plaintext}")
# 'FQPYDUZJIEBKGCNMLHV OXARWST'