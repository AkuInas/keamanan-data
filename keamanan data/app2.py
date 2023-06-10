from flask import Flask, render_template, request, send_file
import mysql.connector
app = Flask(__name__)

kunci = ""

# with open(input) as f:
#     contents = f.read()

# plaintext = contents

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enkripsi', methods=['GET', 'POST'])
def en():
    if request.method == 'POST':
        p = request.files['en']
        a = request.form['kunci']
        if p:
            content = p.read().decode('utf-8')
            ci = enkripsi(content, a)
            output_content = ci
            output_file_path = 'output_enkripsi.txt'
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_content)
            upload_file_en(content, output_content)
            return send_file(output_file_path, as_attachment=True)
        return render_template('index.html')

@app.route('/dekripsi', methods=['GET', 'POST'])
def de():
    if request.method == 'POST':
        c = request.files['de']
        b = request.form['kunci2']
        if c:
            content1 = c.read().decode('utf-8')
            pl = dekripsi(content1, b)
            output_content1 = pl
            output_file_path = 'output_dekripsi.txt'
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_content1)
            upload_file_de(content1, output_content1)
            return send_file(output_file_path, as_attachment=True)
        return render_template('index.html')

# enkripsi
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

# dekripsi
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

def koneksi_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="keamanan"
    )
    return db

def upload_file_en(file, file_en):
    db = koneksi_db()
    cursor = db.cursor()
    sql = "INSERT INTO enkripsi (file, hasil_enkripsi) VALUES (%s, %s)" 
    val = (file, file_en)
    cursor.execute(sql, val)
    db.commit()

def upload_file_de(file, file_de):
    db = koneksi_db()
    cursor = db.cursor()
    sql = "INSERT INTO dekripsi (file, hasil_dekripsi) VALUES (%s, %s)" 
    val = (file, file_de)
    cursor.execute(sql, val)
    db.commit()

app.run(debug=True)