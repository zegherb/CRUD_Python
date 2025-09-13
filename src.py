import CRUD
import os

while True:
    print("\nMenu")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Exit")
    try:
        pilih = int(input("pilih menu: "))
        match pilih:
            case 1:
                CRUD.createdate()
            case 2:
                CRUD.readdata()
            case 3:
                print("Terima kasih telah menggunakan program ini.")
                break
            case _:
                print("Pilihan tidak tersedia, silakan coba lagi.\n")
    except ValueError:
        print("Inputan harus berupa angka!\n")