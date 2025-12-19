# Proje: Banka Hesap Yönetimi (ATM Simülasyonu)
# Developer: @sudenaz-mutlu
# Açıklama: Sözlük yapısı kullanarak bakiye ve ek hesap kontrolü yapan bir sistem.

ardaHesap = {
    "ad" : "Arda Ersoy",
    "hesapno" : "6439030",
    "bakiye": 7650,
    "ekhesap": 3000
}
edaHesap = {
    "ad" : "eda güler",
    "hesapno" : "8938756",
    "bakiye": 9343,
    "ekhesap": 7500
}

def para_cek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap["bakiye"] >= miktar:
            print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]
        if toplam >= miktar:
            ekhesapkullanımı = input("Ek hesap kullanılsın mı? (e/h)")
            if ekhesapkullanımı == "e":
                ekhesapkullanılacakmiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ekhesapkullanılacakmiktar
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz.")
def bakiye_sorgula(hesap):
    print(f"Merhaba {hesap['ad']}")
    print(f"Hesap bakiyeniz: {hesap['bakiye']}")
    print(f"Ek hesap bakiyeniz: {hesap['ekhesap']}")
para_cek(edaHesap, 10000)
bakiye_sorgula(edaHesap)
para_cek(edaHesap, 5000)
bakiye_sorgula(edaHesap)