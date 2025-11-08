#program 2
n=5
bilangan=[]

for i in range(n):
    nilai = int(input("masukkan bilangan ke-(): ".format(i+1)))
    bilangan.append(nilai)
    print(bilangan)
#menghitung rata rata
bilangan.sort()
mx= max(bilangan)
mn = min(bilangan)
rata = sum(bilangan)/n
print(bilangan)
print(rata)
print(mx)
print(mn)

selisih_kuadrat = []
for i in range(n):
    t=(bilangan[i]-rata)**2
    selisih_kuadrat.append(t)
print(selisih_kuadrat)
sd = (sum(selisih_kuadrat)/(n-1))**(1/2)
print(sd)