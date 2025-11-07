biodata = {}

while True:
    print("\n------- Menu -------\n1. Masukkan Biodata\n" \
    "2. Tampilkan Biodata\n3. Selesai")

    menu = input("Pilih menu  : ")

    if menu == "1":
        biodata["Nama Lengkap"] = input("\nNama Lengkap : ")
        biodata["NIM"] = input("NIM          : ")
        biodata["Kelas"] = input("Kelas        : ")
        biodata["Program Studi"] = input("Program Studi: ")
        biodata["Umur"] = input("Umur         : ")
        biodata["No. Telepon"] = input("No. Telepon  : ")
        print("\nBiodata tersimpan!")
    elif menu == "2":
        if biodata:
            print("\n----- Biodata Anda -----")
            for key, value in biodata.items():
                print(f"{key} :  {value}")
        else:
            print("\nBiodata tidak tersedia, silakan masukkan biodata terlebih dahulu!")
    elif menu == "3": exit()
    else:
        print("\nMenu tidak tersedia!")