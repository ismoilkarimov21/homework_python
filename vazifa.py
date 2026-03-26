# pochtalar = ["user1@gmail.com","user2yahoo.com","user3@outlook.com"]
# for pochta in pochtalar:
#     if "@" in pochta:
#         print(f"Togri {pochta}.")
#
#     else:
#         print(f"noto'g'ri {pochta}.")
#
# parollar = ["password123","Qwerty","admin","StrongPass1!"]
# for parol in parollar:
#     if len(parollar)<=8:
#         print("Login 8 harfdan iborat bo'lishi shart!")
#     elif parollar.isalnum() and parollar.isalpha():
#         print('Kuchsiz parol')
#     else:
#         print("Kuchli parol")
#
#
# weather_weekly = [20,29,22,19,24,25,23,21]
# sum_weekly = sum(weather_weekly)/len(weather_weekly)
# for havo in weather_weekly:
#     if havo >sum_weekly:
#         print("Iliq kun")
#     else:
#         print("Salqin kun")

#
# taomlar = ['Osh', 'Barak', 'Somsa', 'Manti', 'Shashlik']
# buyurtmalar = ["Osh", "Gumma", "Barak", "Baliq", "Lavash"]
# if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in taomlar:
#            print(" Buyurtmangiz qabul qilindi.")
#        else:
#            print("Kechirasiz menyuda bunday taom yo'q")
# else:
#     print("Zakaz qilmadingiz!")
#
# yosh = [15, 21, 24, 30, 16]
# for yoshi in yosh:
#     if yoshi < 18:
#         print(f"Yoshi {yoshi}: Yosh chegarasiga yetmagan")
#     else:
#         print('Xush kelibsiz')
#
#
# xabarlar = ['Yangi xabar', 'Batareya past', 'Yangilanish mavjud']
# for xabar in xabarlar:
#     if "Batareya past" in xabar:
#         print("Telefoningizni zaryadlang!")

fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []
for fayl in fayllar:
    if ".jpg" in fayl:
        rasmlar.append(fayl)
    else:
        musiqalar.append(fayl)
        print("Rasmlar: ")
        print("Musiqalar: ")
