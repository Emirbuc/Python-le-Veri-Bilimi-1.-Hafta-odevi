# Python-le-Veri-Bilimi-1.-Hafta-odevi
# Kullanıcıdan iki sayı alıp, aşağıdaki işlemleri yaparak ekrana yazdıran bir Python programı yazın: 
# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin:"))
sayi2 = float(input("İkinci sayıyı girin:"))
# İşlemleri gerçekleştirme
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 
mod = sayi1 % sayi2
us= sayi1 ** sayi2

# Sonuçları ekrana yazdırma
print("Toplam: ", toplam)   
print("Çıkarma:", fark)     
print("Çarpma:", carpim)
print("Bölme:", bolum)
print("Mod alma:",mod)
print("Üs alma:",us)
