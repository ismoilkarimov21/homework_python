# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh<=4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# elif yosh < 65:
#     price = 10000
# elif yosh >= 65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")
#
# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print(f'Bugun dam olish kuni.')
# else:
#     print(f'Bugun ish kuni')
#
# kun = input("Bugun nima kuni?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani kettik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")


# narx = 15000
# choy = True
# salat = False
#
# if choy and salat :
#     narx = narx + 10000
# elif choy or salat :
#     narx = narx + 5000
#
#     print(f"Jami {narx} so'm")
#
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh','somsa','manti','shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menuda {taom} bor')
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ['osh','somsa','manti','shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh")


