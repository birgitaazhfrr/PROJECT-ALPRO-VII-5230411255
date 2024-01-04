import sqlite3

koneksi = sqlite3.connect('database_hewan.db')

kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN")

baris_tabel = kursor.fetchall()

print('Data Hewan')
print('=' * 105)
print('{:<10} {:<20} {:<12} {:<16} {:<18} {:<20}'.format('ID HEWAN',
                                                'NAMA HEWAN',
                                                'JENIS',
                                                'ASAL',
                                                'JUMLAH SAAT INI',
                                                'TAHUN TERAKHIR DITEMUKAN'
                                                ))
print('=' * 105)

for baris in baris_tabel:
    print('{:<10} {:<20} {:<12} {:<20} {:<23} {:<19}'.format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()
