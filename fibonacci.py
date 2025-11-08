#s9al1
#def fibonacci(n):
#    a, b = 0, 1
#hasil = []
 #   for _ in range(n):
 #       hasil.append(a)
  #      a, b = b, a + b
   # return hasil

# Contoh penggunaan
#jumlah = int(input("Masukkan jumlah deret Fibonacci: "))
#print("Deret Fibonacci:", fibonacci(jumlah))
#soal2
#import math

#def volume_tabung(r, t):
#    return math.pi * r**2 * t

#r = float(input("Masukkan jari-jari: "))
#t = float(input("Masukkan tinggi: "))

#print(f"Volume tabung = {volume_tabung(r, t):.2f}")
#soal3
def hitung_total_dan_rata(*angka):
    total = sum(angka)
    rata = total / len(angka)
    return total, rata
total, rata = hitung_total_dan_rata(2, 3, 5, 10)
print(f"Total: {total}")
print(f"Rata-rata: {rata}")


