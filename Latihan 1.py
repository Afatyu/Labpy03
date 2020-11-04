x = int(input("Masukkan Nilai N:"))

jumlah = x+1
start = 1
stop = jumlah
for i in range(start, stop):
    import random
    a = random.uniform(0, 0.5)
    print("Data ke", i, "=>", a)
print("Selesai")