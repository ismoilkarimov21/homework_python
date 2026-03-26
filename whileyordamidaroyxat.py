# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shishni istaysizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Do'stlaringiz ro'yhati: ")
# for ism in ismlar:
#     print(ism.title())
#
#

# print("Do'stlaringizni yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "no":
#         ishora = False
#
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['jonibek', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(talabalar)

