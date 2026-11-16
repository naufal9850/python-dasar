#membuat modue dalam package 
# operasi.py
def kurang(a, b):
    return a - b

# geometri.py
def luas_persegi(sisi):
    return sisi * sisi

#menggunakan package
from my_package import operasi, geometri

print(operasi.kurang(10, 4))       # Output: 6
print(geometri.luas_persegi(5))    # Output: 25


#import package dengn fungsi tertentu
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))          # Output: 13
print(luas_persegi(8))        # Output: 64


#package di standary library Python
import os
print(os.getcwd())   # Menampilkan direktori kerja saat ini
import datetime
print(datetime.date.today())  # Menampilkan tanggal hari ini
