# lugat = {
#     "if":"agar",
#     "you":"siz",
#     "we":"biz",
#     "they":"ular",
#     "plular":"ko'plik",
#     "people":"odamlar",
#     "humanity":"odamiylik",
#     "for":"sikl",
#     "set":"to'plam",
#     "this":"kalit so'z"
# }
# for narsa,buyum in sorted(lugat.items()):
#     print(f"{narsa} - {buyum} ")

# countries = {
#     "italy":"rome",
#     "aqsh":"washington",
#     "uk":"london",
#     "qozog'iston":"ostona",
#     "Rossiya":"Moskva",
#     "O'zbekiston":"Toshkent",
#     "Xitoy":"Pekin",
#     "kanada":"Ottava"
# }
# print("Dunyo davlatlari: ")
# for country in sorted(countries.keys()):
#     print(f"{country.title()}")
#
# print("Davlatlarning poytaxtlari: ")
# for poytaxt in sorted(countries.values()):
#     print(f"{poytaxt.title()}")

# davlat = input("Qaysi davlatni poytaxtini bilmoqchisiz ?>> ")
# if  davlat in countries:
#     poytaxt = countries[davlat]
#     print(f"{davlat.title()}ning poytaxti {poytaxt.title()}")
# else:
#     print("Kechirasiz, bizda bunday ma'lumot yo'q")

menu = {
    "osh":35000,
    "barak":20000,
    "baliq":80000,
    "manti":40000,
    "lag'mon":15000,
    "shashlik":25000,
    "somsa":13000,
    "steyk":200000,
    "non":5000,
    "grechka":30000
}

print("3 ta taom buyurtma qiling:  ")
buyurtma = []
for i in range(3):
    taom = input(f"{i+1}-taom: ").lower()
    buyurtma.append(taom)
for buyurtmalar in buyurtma:
    if buyurtmalar in menu:
        print(f"{buyurtmalar.title()} {menu[buyurtmalar]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtmalar} yo'q")

