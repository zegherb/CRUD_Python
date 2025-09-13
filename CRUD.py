data = []
def createdate():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    kelas = input("Masukkan kelas: ")
    data.append({"nama": nama, "nim": nim, "kelas": kelas})
    print("Data berhasil ditambahkan.")
    
def readdata():
    if not data :
        print("Datanya kosong")
    else:
        print(f"{'DATA MAHASISWA ILKOM':<20}")
        print("="*70)
        print(f"| {'Nama':^20} | {'NIM':^20} | {'Kelas':^20} |")
        print("="*70)
        for i in data :
            print(f"| {i['nama']:^20} | {i['nim']:^20} | {i['kelas']:^20} |")
        print("="*70)
            
    