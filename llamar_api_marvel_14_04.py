import hashlib
import requests
import json
import sqlite3

def main_api():
    public = 'ace282eea63c73f774b97eebc779124e'
    private = 'ef600dedc18ce438612d4b1e9c96625da64b4953'
    ts = '1'
    hash = hashlib.md5((ts + private + public).encode()).hexdigest()

    base = 'http://gateway.marvel.com/v1/public/'
    caracter = requests.get(base + 'characters', params={'apikey': public,'ts' : ts, 'hash' : hash, 'name': 'spider-man'} ).json()
    nombre = (caracter ['data']['results'][0]['name'])
    descripcion = (caracter ['data']['results'][0]['description'])

    con = sqlite3.connect("C:/Users/Ricardo/Desktop/bd")
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS MARVEL
                    (NOMBRE TEXT NOT NULL,
                     DESCRIPCION TEXT NOT NULL)''')
    cursor.execute('''INSERT INTO MARVEL (NOMBRE,DESCRIPCION) VALUES(?,?)''',(nombre, descripcion))
    con.commit()
    cursor.execute('''SELECT * FROM MARVEL''')
    print(cursor.fetchall())
    con.close()

if __name__ == '__main__':
    main_api()
