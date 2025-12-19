# Developer: @sudenaz-mutlu
# Proje: Adam Asmaca 
# Açıklama: 4 zorluk seviye seçeneği olan kelime tahmin oyunu

import random

print("Adam Asmaca Oyununa Hoşgeldiniz!")
print("1-kolay\n2-orta\n3-zor\n4-çok zor")
game_difficulty_level = int(input("Oyunun zorluk derecesini rakam olarak seçiniz: "))
right_to_estimate = {"1": 3,
                     "2": 3,
                     "3": 6,
                     "4": 6}

easy_level = [
"ışık","örtü","büyü","çetin","gizem","şüphe","hipnoz","zıtlık","pusula","karmaşa",
"labirent","mücadele","serüven","özgür","baskı","rüya","kıyam","tutku","yargı","şans",
"şafak","hırsız","yankı","temsil","kavram","üslup","çözüm","sancak","özlem","saygı",
"beyin","kutsal","sırlar","vahşi","yakın","düşün","dönüş","zaman","düşes","mantık",
"saydam","duygu","şekil","özdeş","şehvet","güven","ihtişam","fısıltı","bilinç","merkez",
"tören","mabet","arzu","özgül","duruş","korku","soylu","doğum","sonsuz","bellek",
"hisar","puslu","cevher","imkan","serin","sükun","ürper","başat","tasar","sarsı",
"merak","yankı","irade","özveri","mutlak","kuşku","yordam","bağlam","anımsı","sürem",
"sürgü","yarış","bilgi","teklik","sentez","yörün","kısmet","özdeş","betim","belge",
"kitap","sanat","insan","bütün","doğal","varlık","yargıç","tutarl"
]
medium_level =[
"gizlenmek","başlangıç","karşıtlık","göçebelik","müteahhit","sorgulamak","bilinçaltı","içselleşme",
"parçalanma","özgürleşme","karmaşıklık","muhasebeci","dönüşümler","etkileşim","özdeşleşme","yabancılaşma",
"çelişiklik","uyumsuzluk","kararlılık","kapsayıcılık","uygarlıklar","düşünürlük","imkansızlık","belirsizlik",
"bütünleşme","hassasiyet","gözetlemek","değerlilik","esneklikler","otoriterlik","yansımasız","gelişimsiz",
"hakikatler","bilinemezci","sorgusuzluk","yetersizlik","bağımsızlık","açıklanmak","kararlısız","karşılaşma",
"farkındalık","bütünlenme","semboliklik","dönüştürme","kendilikler","birleşimsel","zenginleşme","anlamlılık",
"otoritesiz","düşüncesiz","çözümlemek","yaratıcılık","tekrarlama","bilinmezlik","önsezicilik","ilkesizlik",
"umutlanmak","çerçevelem","sarsılmaz","ölçülebilir","paylaşımcı","soyutlamak","bağlantılı","özümseme",
"yansıtılmak","belirlenme","çözümsüzlük","betimlemek","özdeşleşim","araştırıcı","yorumlamak","sezgisellik",
"kendiliğinden","öğreticilik","sorgulayıcı","yansıtmacı","dönüştürücü","başkalaşım","tasarımlık","gerçeküstü",
"duyumsamak","karmaşasız","alışkanlık","kaygısızca","yükseltili","bireysellik","çağrışımsal","deneyimsel",
"anlamlandır","ölümsüzlük","duyarlılık","simgesellik","belirsizce","özgünleşme","ifadelilik","yansımasız"
]
hard_level= [
"değerlendirme","anlamlandırma","karşılaştırma","özdeşleştirmek","sürdürülebilir","çözümleyicilik","uzlaştırıcılık",
"sorumlulaştırma","muhasebeleştirme","geliştirilebilir","yenidenyapılandırma","karakteristiklik","psikolojiklik",
"sorgulayabilir","düşünselcilik","kararsızlaşmak","bilinçselleşme","bağımsızlaştırma","özümseyicilik",
"kuramsallaştırma","karmaşıklaşmak","mantıksallaştırma","deneyimleyicilik","özdeşleştirici","algılayabilirlik",
"farkındalaştırma","betimleyicilik","eleştirellik","yorumlayıcılık","çözümleyebilmek","bağlamsallaşmak",
"bireyselleşmiş","dönüştürülebilir","anlamlandırıcılık","düşünselleşmek","ifadelendirici","belirsizleştirme",
"psikanalitiklik","kavramsallaşmak","özgürleştirici","parçalayabilirlik","yansıtıcılık","ilişkilendirmek",
"karakterizasyon","kapsamlandırmak","genelleştirmek","felsefileştirme","çelişkisizlik","deneyimleştirici",
"yorumlanabilir","duygusallaşmak","ahlaksallaştırma","önemsizleştirme","simgeselleştirme","özdeşlikçilik",
"doğallaştırıcı","sistematikleşme","tanımlanabilir","düşüncelileşme","belirleyicilik","bütünselleştirme",
"tutarlılıksızlık","öğretilebilmek","yargılayıcılık","güçlendirilmiş","mantıksızlaştırma","yansıtılabilirlik",
"bireyleşebilmek","tasarımsallaştırma","özgünleştirici","sorunsuzlaştırma","deneyselleştirme","gerçekleştirmek",
"yansımaçözümleme","özdeşleşebilir","karşılaştırıcılık","betimleyebilmek","bağdaştırıcılık","mantıklaştırıcı",
"evrenselleşmek","disiplinlerarası","tanımlayıcılık","yenidenüretimcilik","içselleştirebilmek","özgürleştiricilik",
"bütüncülleşmek","ayrıntılandırma","soyutlayıcılık","sembolleştirme","kapsamlılaştırma","rasyonelleştirme",
"şekillendirilmek","yorumlanabilirlik","farklılaştırıcılık","özdeşselleşme","dengeleyicilik","uyumlaştırıcılık"
]
extra_hard_level = [
"ayakları yere basmak","gözden düşmek","tepesi atmak","ağzı açık kalmak","dilinin altında bakla kalmamak",
"kulak asmamak","etekleri zil çalmak","yüreği ağzına gelmek","gözünü budaktan sakınmamak","ağzından bal damlamak",
"ayağına taş değmesin","taş üstünde taş bırakmamak","göz boyamak","ipleri eline almak","kulağını tersten göstermek",
"yağmurdan kaçarken doluya tutulmak","devede kulak kalmak","başı göğe ermek","elini taşın altına koymak","burnundan solumak",
"adım adım ilerlemek","kulağı delik olmak","kafası karışmak","kılı kırk yarmak","canı burnunda olmak","kalem oynatmak",
"dil dökmek","karnından konuşmak","sudan sebepler","taş kesilmek","gözünü dört açmak","etekleri tutuşmak","yol yordam bilmek",
"başına çorap örmek","kol kanat germek","kalbi pır pır etmek","eli ayağına dolaşmak","yüreği hop etmek","dilinde tüy bitmek",
"boş laf etmek","ağzı kulaklarına varmak","gözünü karartmak","gözü kara olmak","kafası atmak","etekleri zil çalmak",
"aklı başına gelmek","başı dertte olmak","gözü dönmek","dili tutulmak","ayağına dolanmak","göz göre göre","kanat germek",
"karın ağrısı çekmek","çizgiyi aşmak","ipleri koparmak","sözünü esirgememek","suya sabuna dokunmamak","taş gibi olmak",
"bağrı yanık olmak","el ayağa düşmek","kuyruğu dik tutmak","yüzü gülmek","yüreği dağlanmak","kabına sığmamak","akıl sır ermemek",
"dili damağı kurumak","başını derde sokmak","sudan çıkmış balığa dönmek","gözü kulağı açık olmak","göz göze gelmek",
"ayağını denk almak","kulağına küpe yapmak","kafasına dank etmek","baş göz etmek","kafayı yemek","boşboğazlık etmek",
"gözleri fal taşı gibi açılmak","ipi koparmak","taş kesilmek","ağzı var dili yok","burnu büyük olmak","gönül koymak",
"ayak diremek","soğukkanlı olmak","dilinin kemiği olmamak","kafası çalışmak","can atmak","ağzı kulaklarına varmak",
"çileden çıkmak","dilini yutmak","gözleri parlamak","ayağı kaymak","kulağını çınlatmak","yolunu gözlemek","başını alıp gitmek",
"elini eteğini çekmek","gözünü alamamak","başına iş açmak","etekleri zil çalmak","burnu havada olmak","taş kesilmek"
]

#ekrana yazdırılacak çizim seçenekleri:Kolay/Orta versiyonu (4 aşama)
stages1 = [
r"""
  +---+
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
=========
"""
]
# Zor/Çok zor versiyonu (7 aşama)
stages2 = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
game_input = input("Oyunun zorluk derecesini rakam olarak seçiniz: ")
if game_input not in ["1", "2", "3", "4"]:
    print("Geçersiz seçim! Kolay seviye seçildi.")
    game_input = "1"

game_difficulty_level = int(game_input)

right_to_estimate = {"1": 3, "2": 3, "3": 6, "4": 6}

word_list = []
if game_difficulty_level == 1:
    word_list = easy_level
    stages = stages1
elif game_difficulty_level == 2:
    word_list = medium_level
    stages = stages1
elif game_difficulty_level == 3:
    word_list = hard_level
    stages = stages2
elif game_difficulty_level == 4:
    word_list = extra_hard_level
    stages = stages2

word = random.choice(word_list).lower()
hidden_word = [" " if harf == " " else "_" for harf in word]
max_wrong = right_to_estimate[str(game_difficulty_level)]
wrong_count = 0
guessed_letters = []

while wrong_count < max_wrong and "_" in hidden_word:
    print(stages[wrong_count]) 
    print("\nKelime: " + " ".join(hidden_word))
    print(f"Kalan Hak: {max_wrong - wrong_count}")
    
    user_estimate = input("Bir harf tahmin ediniz: ").lower()
    
    # Geçersiz giriş kontrolü
    if len(user_estimate) != 1 or not user_estimate.isalpha() and user_estimate != " ":
        print("Lütfen sadece tek bir harf girin!")
        continue

    if user_estimate in guessed_letters:
        print("Bu harfi zaten söylediniz!")
        continue
    
    guessed_letters.append(user_estimate)

    # Tahmin kontrol 
    if user_estimate in word:
        print("Doğru tahmin!")
        for index, letter in enumerate(word):
            if letter == user_estimate:
                hidden_word[index] = user_estimate
    else:
        wrong_count += 1
        print("Yanlış tahmin!")

if "_" not in hidden_word:
    print("\n" + " ".join(hidden_word))
    print("TEBRİKLER! Kazandınız.")
    score = 100 - (wrong_count * (100 // max_wrong))
    print(f"Puanınız: {score}")
else:
    print(stages[wrong_count])
    print(f"Kaybettiniz! Doğru kelime: {word}")