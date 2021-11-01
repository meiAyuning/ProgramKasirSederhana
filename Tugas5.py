print("==========")
print("Program Kasir Sederhana")
print("Selamat Datang Di Warung Maknyusss")
keranjangBelanja = []
while True:
    menu_pilihan = input(' 1.Menu Makanan\n 2.Menu Minuman\n 3.Menu Snack\n Masukkan menu utama 1-3: \n')
    if menu_pilihan == "1":
        print("==========")
        print("Anda memilih nomor 1 : Menu Makanan")
        print("Pilih menu makanan anda :")
        makanan = ["Nasi Geprek", "Rujak Soto", "Nasi Tempong"]
        while True:
            for a in range(0, len(makanan)):
                print(f'{a + 1}.{makanan[a]}')
            list_makanan = input('Pilih Menu 1-3:\n')
            if list_makanan == "1":
                keranjangBelanja.append(makanan[0])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            elif list_makanan == "2":
                keranjangBelanja.append(makanan[1])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            elif list_makanan == "3":
                keranjangBelanja.append(makanan[2])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            else:
                print("==========")
                print("Menu tidak tersedia\n")
                continue
    elif menu_pilihan == "2":
        print("==========")
        print("Anda memilih nomor 2 : Menu Minuman")
        print("Pilih menu minuman anda :")
        minuman = ["Es Teh","Es Mojitos","Jus Buah"]
        while True:
            for a in range(0, len(minuman)):
                print(f'{a + 1}.{minuman[a]}')
            list_minuman = input('Pilih Menu 1-3:\n')
            if list_minuman == "1":
                keranjangBelanja.append(minuman[0])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            elif list_minuman == "2":
                keranjangBelanja.append(minuman[1])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            elif list_minuman == "3":
                keranjangBelanja.append(minuman[2])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}  1x')
                break
            else:
                print("==========")
                print("Menu tidak tersedia\n")
                continue
    elif menu_pilihan == "3":
        print("==========")
        print("Anda memilih nomor 3 : Menu Snack")
        print("Pilih menu snack anda :")
        snack = ["Kucur","Piscok","Samosa"]
        while True:
            for a in range(0, len(snack)):
                print(f'{a + 1}.{snack[a]}')
            list_snack = input('Pilih Menu 1-3:\n')
            if list_snack == "1":
                keranjangBelanja.append(snack[0])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}    1x')
                break
            elif list_snack == "2":
                keranjangBelanja.append(snack[1])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}    1x')
                break
            elif list_snack == "3":
                keranjangBelanja.append(snack[2])
                print('==== list keranjang ====')
                for b in range(0,len(keranjangBelanja)):
                    print(f'{b+1}.{keranjangBelanja[b]}    1x')
                break
            else:
                print("==========")
                print("Menu tidak tersedia\n")
                continue
    else:
        print("Menu tidak tersedia")
        continue

    validasi_menu = input('Ada yang ingin ditambahkan ? Y/n\n')
    if validasi_menu == "Y" or validasi_menu == "y":
        print("==========")
        continue
    else:
        print("Pesanan anda akan di antar")
        break