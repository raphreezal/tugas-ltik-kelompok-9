# FITUR LOGIN

def login():
    kesempatan = 3

    for i in range(kesempatan):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == "Daspro2023" and password == "Latihan":
            print("Login berhasil! Selamat datang.")
            return
        else:
            print("Username atau password salah. Kesempatan Anda tersisa:", kesempatan - (i + 1))
    
    print("Kesempatan habis! Akses ditolak.")

login()