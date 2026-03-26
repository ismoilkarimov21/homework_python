# otam = {}
# otam ['ism'] = 'Sharifboy ismoilov'
# otam ['tug\'ilgan yili'] = 1966
# otam ['shahri'] = 'Xiva'
# print(f"Otamning ismi {otam['ism'].title()}, {otam['tug\'ilgan yili']}-yilda  {otam['shahri']} tumanida tug'ilgan")

# taomlar = {
#     'onam': 'osh',
#     'otam': 'barak',
#     'men': 'manti'
#      'opam':'baliq'
#       'ukam':'shashlik'
# }
# sevimli = taomlar['onam']
# print(f"Onamning sevimli taomi {sevimli}")
#
# sevimli = taomlar['otam']
# print(f"Otamning sevimli taomi {sevimli}")
#
# sevimli = taomlar['men']
# print(f"Mening sevimli taomim {sevimli}")

# atama = {'float':'haqiqiyonlar', 'if':'agar','else':'yoki','integer':'butunsonlar', 'string':'matn','insert':"qo'shish",'del':"o'chirish",
#           'remove':'olish','sort':'saralash','list':'royhat'}
# print(atama)

lugat = {
    'name':'ism',
    'book':'kitob',
    'cution':'yostiq',
    'prepare':'tayyorlanmoq'
}
tarjima = input("So'z kiriting>>>")
tarjima = lugat.get(tarjima, "Bunday so'z mavjud emas")
print(tarjima)
# lugat = {'name':'ism', 'book':'kitob', 'cution':'yostiq', 'prepare':'tayyorlanmoq'}
# tarjima = input("Kalit so'zni kiriting>>>")
# if tarjima in lugat:
#     print(f"Bu so'zning tarjimasi: {lugat[tarjima]}")
# else:
#     print('Bunday so\'z mavjud emas!'  )

