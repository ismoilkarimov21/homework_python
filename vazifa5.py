# SVETAFOR

# ranglari = {'qizil', 'sariq', 'yashil'}
# ishora = True
# n=1
# while ishora:
#     rang = input("Svetafor qaysi rangda ? ")
#     if rang in ranglari:
#         print("Rahmat, to'g'ri keladi.")
#         ishora = False
#     if rang not in ranglari:
#         print("Kechirasiz, bu rang to'g'ri kelmaydi. Qayta urinib ko'ring ")
#         n+=1
#         ishora = True

# TASODIFIY SON
#
# import random
# tasodifiy_son = random.randint(1,10)
# ishora = True
# while ishora:
#     son = int(input("Marhamat topishga urinib ko'ring: "))
#     if son == tasodifiy_son:
#         ishora = False
#         print("Tabriklaymiz siz tasodifiy sonni topdingiz !😎")
#     else:
#         ishora = True
#         print("Noto'g'ri, qayta urinib ko'ring😊")

# DO'STLAR RO'YHATINI YARATISH

# dostlar = []
# print("Do'stlarim ro'yhati.")
# n=1
# while True:
#     dost = f"Do'stingizni ismini kiriting: "
#     ism = input(dost)
#     dostlar.append(ism)
#     natija = input("Yana do'stlaringiz bormi ? (ha/yo'q)")
#     if natija == "ha":
#         continue
#     else:
#         break

# VALYUTA AYIRBOSHLASH KURSI

# kurs = 12600
# ishora = True
# print("Valytua ayirboshlash dasturiga xush kelibsiz!")
# while ishora:
#     qiymat = input("\nSo'm miqdorini kiriting: ").lower()
#     if qiymat == 'stop':
#         ishora = False
#         print("Dastur ishlashi to'xtatildi!")
#     else:
#         som = float(qiymat)
#         dollar = som/kurs
#         print(f"{som:,} so'm = {dollar:.2f} USD")