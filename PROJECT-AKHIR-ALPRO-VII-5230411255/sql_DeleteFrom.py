import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()



kursor.execute(f"DELETE FROM HEWAN WHERE jenis = 'Mamalia'")
koneksi.commit()

print("Berhasil Dihapus")
koneksi.close()
