# Proje: Taş-Kağıt-Makas Oyunu
# Developer: @sudenaz-mutlu
# Açıklama: Python öğrenme sürecimde geliştirdiğim basit bir oyun.

import random
choices =[ "taş", "kağıt", "makas"]
tur_sayısı = int(input("Kaç tur oynamak istersiniz?"))
#puanlar
player_score = 0
computer_score = 0
round_number = 1

while round_number <= tur_sayısı:
   print(round_number, ".tur")
   print("Seçenekler:", choices)
   computer = random.choice(choices)
   player = input("senin seçimin:").lower()
   print("Bilgisayarın seçimi:", computer)

   if player == computer:
      print("berabere")
   elif(player == "taş" and (computer == "makas")) or \
    (player == "kağıt" and (computer == "taş")) or \
    (player == "makas" and (computer == "kağıt")):
    print("Kazandınız!")
    player_score += 1
   else:
      print("Kaybettiniz!")
      computer_score += 1
   round_number += 1

print("OYUN BİTTİ")
print("Senin skorun:", player_score)
print("Bilgisayarın skoru:", computer_score)
if player_score > computer_score:
   print("Tebrikler, oyunu kazandınız!")
elif player_score < computer_score:
    print("Oyunu kaybettiniz.")
else:
    print("Oyun berabere bitti.")


