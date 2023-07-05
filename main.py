modern_sozluk = {"if":"eğer","else":"değilse","==":"eşitse"}
soru = input("kelime giriniz")
if soru in modern_sozluk.keys():
    print(modern_sozluk[soru])
else:
    print("kelime bulunamadı")
