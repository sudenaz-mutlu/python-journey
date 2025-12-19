# Not: Bu benim Python öğrenmeye başladığım ilk ayda yazdığım projemdir. 
# Gelişimimi takip etmek için paylaşıyorum.
#rastgele parola oluştur 5 haneli harf özel karakter ve rakam içeren  sonra kullanıcıya verdiğin parola girdir bunu hafızaya atıp dosyaya kaydet ve kullanıcıdan parolasını iste 3 yanlış hakkı var sonra tamamen kapanır.
import random
parola_karakterlerk = "abcdefghijklmnopqrstuvwxyz"
parola_karakterlerB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
parola_karakterlerR = "0123456789"
parola_karakterleriO = ".,;:!?/+-*%&()[]{}<>#@"
p1 = random.choice(parola_karakterlerk)
p2 = random.choice(parola_karakterlerB)
p3 = random.choice(parola_karakterlerR)
p4 = random.choice(parola_karakterleriO)
p5 = random.choice(parola_karakterlerk + parola_karakterlerB + parola_karakterlerR + parola_karakterleriO)
parola = sorted(p1,p2,p3,p4,p5)
parola = "".join(parola)

kullanıcı_isim = input("kullanıcı ad ve soyadınızı giriniz: ")
cinsiyet = input("Cinsiyetinizi giriniz (E/K): ")

if cinsiyet == "E":
    print(f"{kullanıcı_isim} Bey, parolanız: ",parola)
elif cinsiyet == "e":
    print(f"{kullanıcı_isim} Bey, parolanız: ",parola)
elif cinsiyet == "K":
    print(f"{kullanıcı_isim} Hanım, parolanız: ",parola)
elif cinsiyet == "k":
    print(f"{kullanıcı_isim} Hanım, parolanız: ",parola)
else:
    print("Cinsiyet bilgisi yanlış girildi.")

with open("parolalar.txt","a",encoding="utf_8") as file:
    file.write(kullanıcı_isim + "\n" + parola + "\n")

hak = 3
while hak > 0:
    giris_denemesi = input("Lütfen giriş yapmak için parolanızı yazın.")
    
    if giris_denemesi == parola:
        print("Başarılı! Sisteme giriş yapıldı.")
        break
    else:
        hak = hak - 1
        if hak > 0:
            print("Hatalı parola, lütfen tekrar deneyin.")
        else:
            print("3 kez hatalı giriş yaptınız. Sistem güvenlik nedeniyle kapatıldı.")