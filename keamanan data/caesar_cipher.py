import string

huruf  = string.ascii_lowercase

pilih = input("enkripsi(e) atau dekripsi(d) \n".lower())
text = list(input('masukan text: \n').lower())
key = int(input("masukan key 1-25: \n"))

end_program = False

while not end_program:
    if pilih == 'e':
        for i in range(len(text)):
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = huruf.index(text[i]) + key
                text[i] = huruf[new_letter]
        print(''.join(map(str, text)))
        end_program = True
    elif pilih == 'd':
        for i in range(len(text)):
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = huruf.index(text[i]) + key
                text[i] = huruf[new_letter]
        print(''.join(map(str, text)))
        end_program = True
