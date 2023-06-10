from flask import Flask, render_template, request
app = Flask(__name__)
import random
# membuat karakter dan kunci
karakter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
karakter = list(karakter)
# kunci = karakter.copy()
# random.shuffle(kunci)
kunci = "FQPYDUZJIEBKGCNMLHV OXARWST"
kunci = list(kunci)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enkripsi', methods=['GET', 'POST'])
def en():
    if request.method == 'POST':
        p = request.form['en']
        c = enkripsi(p)
        return render_template('index.html', ciphertext=c, plaintext1=p)

@app.route('/dekripsi', methods=['GET', 'POST'])
def de():
    if request.method == 'POST':
        c = request.form['de']
        p = dekripsi(c)
        return render_template('index.html', plaintext=p, ciphertext1=c)

# enkripsi
def enkripsi(plaintext):
    ciphertext = ""

    for kata in plaintext:
        index = karakter.index(kata)
        ciphertext += kunci[index]
    return ciphertext

# dekripsi
def dekripsi(ciphertext):
    plaintext = ""

    for kata in ciphertext:
        index = kunci.index(kata)
        plaintext += karakter[index]
    return plaintext

app.run(debug=True)