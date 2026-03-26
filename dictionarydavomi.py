# talaba_0 = {
#     'ism': 'ismoil',
#     'familiya': 'karimov',
#     'yosh':'19',
#     'fakultet':'kompyuter injiniring',
#     'kurs':1
# }
#
# #print(talaba_0)
# #print(talaba_0.items())
#
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")
from dictionary import telefonlar

# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olimcola': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'jamol':'nokia 3311',
#     'jasur': 'iphone x',
#     'bobur':'iphone x'
# }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
#
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':30000,
#     'anjir':25000,
#     'shaftoli':40000,
#}

# print(mahsulotlar.keys())
# print(f"Do'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling!")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
#
# print(telefonlar.values())
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

print("banana" in thisset)

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya", "cherry"}

thisset.update(tropical)

print(thisset)

thisset.remove("banana")
print(thisset)