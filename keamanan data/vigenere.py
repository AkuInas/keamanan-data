def enkripsi(plaintext, kunci):
    plaintext = plaintext.upper()
    kunci = kunci.upper()
    ciphertext = ""
    index_kunci = 0

    for char in plaintext:
        if char.isalpha():
            # mengubah karakter ke index 0-25
            char_value = ord(char) - ord('A')
            kunci_value = ord(kunci[index_kunci]) - ord('A')

            # rumus
            enkripsi_value = (char_value + kunci_value) % 26

            # mengubah ke karakter
            enkripsi_char = chr(enkripsi_value + ord('A'))
            ciphertext += enkripsi_char

            # pindah huruf selanjutnya
            index_kunci = (index_kunci + 1) % len(kunci)
        else:
            ciphertext += char
    return ciphertext


def dekripsi(ciphertext, kunci):
    ciphertext = ciphertext.upper()
    kunci = kunci.upper()
    plaintext = ""
    index_kunci = 0

    for char in ciphertext:
        if char.isalpha():
            char_value = ord(char) - ord('A')
            kunci_value = ord(kunci[index_kunci]) - ord('A')

            dekripsi_value = (char_value - kunci_value) % 26

            dekripsi_char = chr(dekripsi_value + ord('A'))
            plaintext += dekripsi_char

            index_kunci = (index_kunci + 1) % len(kunci)
        else:
            plaintext += char
    return plaintext

# isi bebas
with open('coba.txt') as f:
    contents = f.read()


plaintext = contents
kunci = "gaskeun"

# enkripsi
hasil_enkripsi = enkripsi(plaintext, kunci)
print("Enkripsi:", hasil_enkripsi)

# Dekripsi
hasil_dekripsi = dekripsi(hasil_enkripsi, kunci)
print("Dekripsi:", hasil_dekripsi)

