import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

jml_skrng_update = 900
id_hewan = 1

kursor.execute(f"UPDATE HEWAN SET jml_skrng = {jml_skrng_update} WHERE id_hewan = {id_hewan}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

koneksi.close()
