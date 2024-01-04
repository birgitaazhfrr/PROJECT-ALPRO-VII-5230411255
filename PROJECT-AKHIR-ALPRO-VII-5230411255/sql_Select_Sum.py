import sqlite3

koneksi = sqlite3.connect('database_hewan.db')

kursor = koneksi.cursor()

kursor.execute("SELECT SUM(jml_skrng) FROM HEWAN")
total = kursor.fetchone()[0]

print(f"TOTAL POPULASI HEWAN LANGKA SAAT INI : {total}")

koneksi.close()
