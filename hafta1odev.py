import math
sayıödev = float(input("Sayiyi Giriniz : "))

sayıa=(math.floor(sayıödev%10))
sayıb=(math.floor((sayıödev%100)/10))
sayıc=(math.floor((sayıödev%1000)/100))
sayıd=(math.floor(sayıödev/1000))

print(sayıd+sayıc+sayıb+sayıa)