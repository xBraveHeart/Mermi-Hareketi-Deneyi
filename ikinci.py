#control flow
#akışı kontrol et!

#a=3
#b=5

a , b = 3 , 5

#code block

#mesela c dillerind kod blockları {}
#if a>b {print...}
a , b= b, a
a=b 
if a>b :
    print("a b'den büyük") #15_16_17 okumaz istenilen şartı sağlamadı
    print("a:" , a , "b:" , b)
#else :
#    print("a b'den büyük değil...")
elif a<b :    
   print("a b'den küçük")
#elif a==b : #== diye kullanılır çünkü atama operatörüdür sağdaki değişkeni soldakine atar
   print("a b'ye eşit")
else :
    print("a b'ye eşit")

#block nesnesi başladı ise kesinikle altına girinti bekler.
if 4<1 :
    pass

if 4>1 :
    print("bu doğru bir durum")
#girinti 4 tane boşluk olucak #ya da 1 kere tab a bas

değişken_adı=5
#int - integer - tam sayı tipli bir değişken!
print(type(değişken_adı))

kesir=3/7
#float - kesir tipli değişken
#ondalık olarak(.) işareti kullanılır!
print(type(kesir) , kesir)

metin="metin tipinde"
#str - metin tipinde değişken.
print(type(metin))


x="5" #str
y=5 #int
z=5.0 #float

print(x==y)
#x==y ? print(type(x)==type(y))
#y==z ? eşit

t = False
t = True
#bool - Boolean / Doğru - Yanlış tipli değişken
#Doğru True
#Yanlış False
print(type(t))

#Doğru - Yanlış tipli değişkenin ilk harfi büyük yazılır
#True=5 anahtar kelime olduğu için değişken olamaz.
#true=5 değişken olabilir.

a=16 #tam sayı olmalı
b=" bursaspor\n " #n koyarsak alt alta yazar ;n olmazsa satıra koyar
print(a*b)

a= " merhaba"
b= " dünya "
c=a+b
print(c)

a=5
b=" dünya "
c=a*b
print(c)

a=5
b="dünya"
c=str(a)+ b
print(c)

z="55.2"
x="23"
print(int(x)+float(z))

t= "False" 
print(bool(t))
#True çıktı çünkü bir değer gözüküyor.

t=0
print(t==False)
t=12
print(t==True)

import random

rasgele= random.randrange(1,10)

kul_veri = input("1 ve 10 arası rasgele sayı giriniz:")
if kul_veri ==str(rasgele) :
        print("Helal olsun dayıoğlu")
else:
        print("Bilgisayarın tuttuğu sayı:", rasgele)
        print("Sizin girdiğiniz sayı:" , kul_veri)
        print("Bidahakine dene dayıoğlu.")


#iç içe if durumları
a , b , c =1 , 2 , 3

if 3 > 1:
    print("3 bir rakamından büyük")
    if 3<2:
        print("2 rakamından da büyük")
        if 3 == 3 :
            print("bu değerler birbirine eşit")
        else :
            print("eşit değil")
            print("Bu kimin altında?")    
        print("Bu kimin altında?")    
else:
    print(" 3 rakamından büyük değil")



#birden fazla şart bulunan durumlar

if 3>2 and 2>1 :
    print("iki şart da doğru")
if 3>=2 and 3<=4 and 3<4 and 3 != 4 :
    print("Tüm şartlar doğru")

print( True and True)
print(1 and 1)
print(False and False)
print(0 and 0)
print(True and False)
print(1 and 0)
print(False and True)
print(0 and 1)


print(True or True)
print(False or True)
print(False or False)


import math

vize= int(input("Vize sonucunu giriniz:"))
if vize > 50:
    final_için_gerekli_not=(50- 0.4* vize)/0.6
    print("Final için almanız gereken not: " , math.ceil(final_için_gerekli_not))
else:
    print("Final için almanız gereken not : 50")

