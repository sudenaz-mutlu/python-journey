import os 

yapılar = {
        "Klasörlerim": {
            "dosya": "Yıllık Raporlar",
            "notlar": "Notlar",
            "belgeler": {
                "yapılacaklar": "Yapılacaklar listesi",
                "2024": {
                    "ocak": "Ocak raporu",
                    "subat": "Şubat raporu",
                    "projeler": {
                        "proje1": "Proje 1 detayları",
                        "proje2": "Proje 2 detayları",
                        }
                    }
                },
                "arsiv": {
                    "eski_notlar": "Eski notlar",
                    "yedek": "Yedek dosya"
                }
            },
            "resimler": {
                "foto1": "Foto içeriği",
                "foto2": "Başka foto",
                "foto3": {
                    "deniz": "Deniz fotoğrafı",
                    "dag": "Dağ fotoğrafı"
                }
            },
            "bos_klasor": {},
            "kodlar": {
                "script": "print('Merhaba')",
                "test": "Test kodu",
                "modeller": {
                    "model1": "Model 1",
                    "model2": "Model 2"
                }
            }
        }

#klasör oluşturma
def klasor_olustur(Klasör_yolu, klasör_içeriği):
    for key, value in klasör_içeriği.items():   #klasör içeriğindeki anahtar ve değerleri al
        yeni_yol = os.path.join(Klasör_yolu,key) #yeni değeri oluştur 

        if isinstance(value,dict): #oluşan şey dict içerirse klasör,string içerirse dosya
            if not os.path.exists(yeni_yol): #yeni klasör daha önce yoksa oluşturur
                os.makedirs(yeni_yol)        #klasör oluşturur
                print(f"{yeni_yol} klasörü oluşturuldu.")
            klasor_olustur(yeni_yol, value)
        else: #oluşacak olan şey dosya ise dosyayı oluştur
            try: 
                with open(yeni_yol, "w" , encoding="utf-8") as dosya:
                    dosya.write(value)
                print(f"{yeni_yol} dosyası oluşturuldu.")
            except Exception as e:
                print(f"{yeni_yol} dosyası {e} sebebiyle oluşturulamadı.")

ana_klasor_adı = list(yapılar.keys())[0] #klasörlerim
ana_klasor_içeriği = yapılar[ana_klasor_adı]

if not os.path.exists(ana_klasor_adı): 
    os.makedirs(ana_klasor_adı)
    print(f"{ana_klasor_adı} oluşturuldu.")

klasor_olustur(ana_klasor_adı,ana_klasor_içeriği)
"""
#geleneksel yolla arananı bulma
def arananı_bul(aranan,mevcut_yapı):
    bakılacaklar = [mevcut_yapı]
    while len(bakılacaklar) > 0:
        incelenecek_klasor = bakılacaklar.pop(0)
        for key,value in incelenecek_klasor.items():
            if key == aranan:
                if isinstance(value,dict):
                    print(f"Aranan {key} klasör içeriği: {list(value.keys())}")
                else:
                    print(f"Aranan {key} dosya içeriği: {value}")
                return value
            if isinstance(value,dict):
                bakılacaklar.append(value)
    print(f"Aradığınız {aranan} burada değil")
    return None
"""

#recursive yolla arananı bulma 
def arananı_bul(aranan,mevcut_yapı,yol=[]):
    for key,value in mevcut_yapı.items():
        mevcut_rota = yol + [key]

        if key == aranan: #klasör mü dosya mı tespit 
            if isinstance(value,dict): #bu da klasör ise
                print(f"Klasör içeriği: {list(value.keys())}") #gidilen yol liste şeklinde yazdırsın diye kullanıldı
                return value
            else:
                print(f"Dosya içeriği: {value}")
                return value
        #Recursive kısmı
        if isinstance(value,dict):
            sonuc = arananı_bul(aranan,value,mevcut_rota) #aranan dosya olana kadar devam et 
            if sonuc is not None:  #aranan dosya var mı yoksa sonuc değeri boş mu geldi?
                return sonuc
    return None

hedef = input("Aramak istediğiniz dosya/klasör adını giriniz: ").strip() #gereksiz boşluğu temizler
hedef_sonucu = arananı_bul(hedef,yapılar,yol=[])

if hedef_sonucu is None:
    print("Aranan değer Klasörlerim içerisinde değil!!")

"""
#Recursive yolla silme işlemi 1-Arananın yolunu bul 
def silineceğin_yolu(silinecek,mevcut_yapı,mevcut_yol ="Klasörlerim"): #klasörlerimde işlem yapılacak
    for key,value in mevcut_yapı.items():
        yol = os.path.join(mevcut_yol,key)
        if key == silinecek: #aradığım şeyi bulduysam
            return yol
        if isinstance(value,dict): #aradığım şeyi bulamadım elimdeki klasör içine girmelimiyim?
            sonuc = silineceğin_yolu(silinecek,value,yol)
            if sonuc is not None:
                return sonuc
    return None 

#2-recursive silme kısmı
def klasor_silme(silinecek_öge):
    if os.path.isfile(silinecek_öge): #silinecek öge dosya
        os.remove(silinecek_öge)
        print(f"{silinecek_öge} dosyası silidi")
        return
    
    for öge in os.listdir(silinecek_öge):   #silinecek dosya içeriği listelendi
        izlenen_yol = os.path.join(silinecek_öge,öge) #bulduğu dosya/klasörleri birleştirir

        if os.path.isdir(izlenen_yol): #silinecek öge klasör 
            klasor_silme(izlenen_yol)
        else: #dosya silinecekse
            os.remove(izlenen_yol)
            print(f"{izlenen_yol} dosyası silindi.")
    os.rmdir(silinecek_öge) #içi boş klasörü siliniyor
    print(f"{silinecek_öge} klasörü silindi.")

sil = input("Silmek istediğiniz dosya/klasör giriniz.").strip()
silme_islemi = silineceğin_yolu(sil,yapılar["Klasörlerim"])

if silme_islemi and os.path.exists(silme_islemi):
    klasor_silme(silme_islemi)
else:
    print("Silinecek öğe bulunamadı.")
"""