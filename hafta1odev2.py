import math
kenar1 = float(input("1. kenarı giriniz: "))
kenar2 = float(input("2. kenarı giriniz: "))

diktörtgenalani= kenar1*kenar2

print(diktörtgenalani)


#################################################################################################


yaricap = float(input("yari çap giriniz: "))
yukseklik = float(input("yüksekliği giriniz: "))

silindirinalani = (2*math.pi*(yaricap**2)+(2*math.pi*yukseklik*yaricap))

print(silindirinalani)
