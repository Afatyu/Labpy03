# Tugas Praktikum 3

## Latihan 1
Pada latihan 1 kita akan mencari bilangan acak yang lebih kecil dari 0.5.
### Syntaxnya:
```python
r = int(input("Masukkan Nilai N:"))

jumlah = r+1
start = 1
stop = jumlah
for i in range(start, stop):
    from random import random
    a = random()
    print("Data ke", i, "=>", a)
print("Selesai")
```

#### Penjelasan Algoritma

- Pertama kita membuat perintah untuk memasukkan nilai n.
```python
x = int(input("Masukkan Nilai N:"))
```

- Lalu kita membuat variable untuk menentukan berapa jumlah data yang akan kita cari.
```python
jumlah = x+1
start = 1
stop = jumlah
```
"start = 1" berarti data dimulai dari 1.
"jumlah = x+1 dan stop = jumlah" berarti looping akan berhenti ketika variable 'jumlah' sudah sesuai dengan nilai yang diinput pada variable 'x'.

- Lalu kita membuat syntax looping for.
```python
for i in range(start, stop):
```
Looping akan terus berjalan sampai jumlah yang telah ditentukan untuk berhenti.

- Setelah itu kita memasukkan fungsi untuk menampilkan nilai secara acak.
```python
    import random
    a = random.uniform(0, 0.5)
```

- Terakhir kita tinggal membuat syntax untuk mengeluarkan hasil dari looping tersebut.
```python
    print("Data ke", i, "=>", a)
print("Selesai")
```
'i' adalah hasil dari jumlah perulangan yang telah dilakukan. Dan 'a' akan menampilkan nilai secara acak karena fungsi random yang telah diinput.

### Screenshoot Input dan Output
![awdawdawdawda](https://user-images.githubusercontent.com/72727701/98082031-b2532880-1eaa-11eb-97a3-4e4bc2d07abb.png)

## Latihan 2
Latihan 2 akan menampilkan bilangan ***terbesar*** dari ***n*** buah data yang diinputkan.

### Syntaxnya:
```python
a = int()
b = 0

while a >= 0:
    a = int(input("Masukkan Bilangan: "))
    if a == 0:
        break
    if a > b:
        b = a
print("Bilangan terbesar adalah :", b)
print("Selesai")
```

#### Penjelasan Algoritma

- Pertama kita membuat 2 variable.
```python
a = int()
b = 0
```
Variable 'a' sebagai integer yg belum diinput nilainya, dan variable 'b' bernilai 0.

- Lalu kita membuat looping while.
```python
while a >= 0:
    a = int(input("Masukkan Bilangan: "))
```
Disini kita akan diminta untuk menginput angka pada variable 'a'. Dan apabila nilai 'a' lebih besar dari 0, maka akan terjadi perulangan.

- Membuat statement untuk berhenti dari perulangan.
```python
    if a == 0:
        break
```
Pada tahap ini apabila kita menginput nilai 0 pada variable 'a' yang diminta sebelumnya, maka kita akan berhenti dari perulangan.

- Membuat statement untuk mengambil angka terbesar.
```python
    if a > b:
        b = a
```
Disini system akan mengambil nilai 'a' terbesar untuk variable 'b'.

- Menampilkan outputnya
```python
print("Bilangan terbesar adalah :", b)
print("Selesai")
```
Disini kita akan menampilkan output bilangan terbesar dari angka - angka yang telah diinputkan.

### Screenshoot Input & Output
![Latihan 2](https://user-images.githubusercontent.com/72727701/98082633-a320aa80-1eab-11eb-8bbc-18b9f37cfde6.png)

## Program1
Pada program ini kita akan mencari keuntungan pada usaha yang telah berjalan selama 8 bulan dengan kondisi yang telah ditentukan.

### Syntaxnya
```python
modal = 100000000
laba = 0
untung = 0

for i in range(1, 9):
    if i < 3:
        laba = 0
        untung = untung + laba
    elif i < 5:
        laba = modal*1/100
        untung = untung + laba
    elif i < 8:
        laba = modal*5/100
        untung = untung + laba
    else:
        laba = modal*3/100
        untung = untung + laba
    print("Laba bulan ke", i, "sebesar:", laba)
print("Total laba adalah:", untung)
```

#### Penjelasan Algoritma

- Membuat variablenya. contoh:
```python
modal = 100000000
laba = 0
untung = 0
```
Disini variable modal yaitu 100000000 dan variable laba dan untung adalah 0.

- Lalu membuat looping for.
```python
for i in range(1, 9):
```
Disini perulangan akan dimulai dari nilai 1 dan akan berhenti pada nilai akhir, yaitu 9.

- Membuat kondisi pertama.
```python
    if i < 3:
        laba = 0
        untung = untung + laba
```
Disini apabila nilai 'i' kurang dari 3 maka labanya adalah 0. Artinya apabila belum bulan ke 3, maka labanya adalah 0. Untung digunakan untuk nanti menghitung total keuntungan yang didapat.

- Membuat kondisi kedua.
```python
    elif i < 5:
        laba = modal*1/100
        untung = untung + laba
```
Kondisi ini adalah pada bulan ke 3 - 4, maka akan mendapatkan laba sebesar 1% atau laba = modal dikali 1 dibagi 100.

- Membuat kondisi ketiga.
```python
    elif i < 8:
        laba = modal*5/100
        untung = untung + laba
```
Kondisi ini apabila belum memasuki bulan ke 8, maka akan mendapatkan laba sebesar 5%.

- Membuat kondisi terakhir.
```python
    else:
        laba = modal*3/100
        untung = untung + laba
```
Ini adalah kondisi pada bulan ke 8. Laba menurun 2%, sehingga laba bulan ke 8 menjadi sebesar 3%.

- Mencetak laba perbulan dan total laba selama 8 bulan.
```python
    print("Laba bulan ke", i, "sebesar:", laba)
```
Syntax diatas akan menampilkan hasil laba setiap bulan.

```python
print("Total laba adalah:", untung)
```
Dan ini akan menampilkan total laba selama 8 bulan.

### Screenshoot Input & Output
![Program1](https://user-images.githubusercontent.com/72727701/98082911-20e4b600-1eac-11eb-98fd-bb86b082d9df.png)
