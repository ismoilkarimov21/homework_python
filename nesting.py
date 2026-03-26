# car0 = {
#     'model':'Lacetti',
#     'rang':'oq',
#     'yil':2018,
#     'narx':13000,
#     'probeg':50000,
#     'korobka':'avtomat'
# }
# car1 = {
#     'model':'nexia 3',
#     'rang':'qora',
#     'yil':2015,
#     'narx':9000,
#     'probeg':89000,
#     'korobka':'mexanika'
# }
# car2 = {
#     'model':'Gentra',
#     'rang':'qora',
#     'yil':2019,
#     'narx':15000,
#     'probeg':10000,
#     'korobka':'avtomat'
# }
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang']} rang,"
#           f"{car['yil']} yil, {car['narx']}$")
#
#
# print(f"{cars[0]}")
# print(car0['model'])
# print(f"{cars[2]['rang'].title()}"
#       f"{cars[2]['model']}")


# malibus =[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':10,
#         'korobka':'avto'
#     }
#     malibus.append(new_car)
#
# print(malibus)
#
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
#
# print(malibus)
#
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
#
# print(malibus)
#
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka']='mexanika'
#
# print(malibus)
#
# for malibu in malibus:
#     if malibu ['korobka'] =='avto':
#         malibu['narx']=40000
#     else:
#         malibu['narx'] = 35000
# print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php', 'sql'],
#     'husan':['python','php'],
#     'maryam':['css','c#']
# }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html','css','js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
        }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
