# Latihan
print("Nama : Fadhlurohman Fatikh Navintino")
print("NIM  : 312210368")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'Sukasno': '0812665648', 'Darto': '08767563586'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # Sukasno    |  ", kontak['Sukasno'], '|')
print("|   # Darto   |  ", kontak['Darto'], '|')
print("============================")
print()

# Tampilkan kontaknya Sukasno
print("# Tampilkan kontaknya Sukasno")
print("===========================")
print("|    Sukasno     | ", kontak['Sukasno'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama Indra, nomor 0873648584
print("# Tambah kontak baru dengan nama Indra, nomor 0873648584")
kontak['Indra'] = '0873648584'
print("===========================")
print("|    Indra    | ", kontak['Indra'], '|')
print("===========================")
print()

# Ubah kontak Darto dengan nomor baru 088999776
print("# Ubah kontak Darto dengan nomor baru 088999776")
kontak['Darto'] = '088999776'
print("===========================")
print("|    Darto    | ", kontak['Darto'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()

# Menghapus kontak Darto
print("# Hapus kontak Darto")
print("=========================================================")
kontak.pop('Darto')
print(kontak.items())
print("=========================================================")