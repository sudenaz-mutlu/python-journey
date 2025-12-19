# Developer: @sudenaz-mutlu
# Proje: Labirentten Çıkış ve Bilgi Yarışması

import random
import time

# Labirent yapısı
labirent = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],  
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],  
    ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '^'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

kelime_havuzu = {
    "AGRI": "Türkiye'nin en yüksek dağı",
    "ANKARA": "Türkiye'nin başkenti",
    "MOZART": "Küçük Bir Gece Müziği'ni besteleyen",
    "MARS": "Kızıl gezegen olarak bilinen",
    "JUPITER": "Güneş sisteminin en büyük gezegeni",
    "NIL": "Dünyanın en uzun nehri",
    "EVEREST": "Dünyanın en yüksek dağı",
    "FRANSA": "Eyfel Kulesi hangi ülkede",
    "EINSTEIN": "Görelilik teorisini bulan bilim insanı",
    "LONDON": "Big Ben hangi şehirde"
}
def labirent_yazdir(): 
    for satir in labirent:
        print(" ".join(satir))

# Boş hücre
bos_hucre = []
for i in range(len(labirent)):
    for j in range(len(labirent[i])):
        if labirent[i][j] == " ":
            bos_hucre.append((i,j))

# Oyuncuyu yerleştirme 
oyuncu_x, oyuncu_y = random.choice(bos_hucre)          
labirent[oyuncu_x][oyuncu_y] = "."

hareketler = {"W": (-1, 0), "S": (1, 0), "A": (0, -1), "D": (0, 1)}

print("Labirentte '.' sizsiniz. '^' kapısına ulaşın!")

while True:
    labirent_yazdir()
    hareket = input("Hareket (WASD): ").upper()

    if hareket not in hareketler:
        print("Geçersiz tuş! WASD kullanın.")
        continue

    dx, dy = hareketler[hareket]
    yeni_x, yeni_y = oyuncu_x + dx, oyuncu_y + dy

    # Duvar kontrolü
    if labirent[yeni_x][yeni_y] == "#":
        print("Duvara çarptın.")
        continue
    
    # Çıkış kontrolü
    if labirent[yeni_x][yeni_y] == "^":
        print("\n--- TEBRİKLER ÇIKIŞA GELDİN! SON ADIM. ---")
        secilen_kelime = random.choice(list(kelime_havuzu.keys()))
        print(f"SORU: {kelime_havuzu[secilen_kelime]}")
        
        basla = time.time()
        cevap = input("Cevabınız: ").strip().upper()
        bitis = time.time()

        if bitis - basla > 60:
            print("Süre doldu!")
        elif cevap == secilen_kelime:
            print("Tebrikler! Kazandınız.")
        else:
            print(f"Yanlış! Cevap: {secilen_kelime}")
        break

    # Oyuncu hareketi
    labirent[oyuncu_x][oyuncu_y] = " "
    oyuncu_x, oyuncu_y = yeni_x, yeni_y
    labirent[oyuncu_x][oyuncu_y] = "."