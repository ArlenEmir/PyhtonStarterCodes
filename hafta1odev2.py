def Toplama(n):
    toplam = 0
    for rakam in str(n):
        toplam += int(rakam)
    return toplam

sayi1 = int(input('4 Basamaklı Sayıyı Giriniz : '))
n = sayi1
print(Toplama(n))


Kenar1 = int(input('1. Kenar Uzunluğunu Giriniz : '))
Kenar2 = int(input('2. Kenar Uzunluğunu Giriniz : '))

def DikdörtgenAlanHesaplamaDefi():
    return  Kenar1*Kenar2
Alan = Kenar1*Kenar2
print("Dikdörtgenin alanı: ",Alan)

import math

SilindirinYüksekligi = int(input('Silindirin Yüksekliğini Giriniz: '))
SilindirinYariCapi = int(input('Silindirin Yari Capini Giriniz: '))
def SilindirinHacminiHesaplayanDef():
    return (2*math.pi)*(SilindirinYariCapi^2)+2*(math.pi*SilindirinYariCapi)*SilindirinYüksekligi