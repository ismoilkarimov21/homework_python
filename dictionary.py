from os import kill

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0)
# print(len(car_0))
# print(car_0['model'])
# print(car_0['rang'])
#
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# talaba_0['kurs']=4
# talaba_0['fakultet']= 'ki'
# print(talaba_0)
# print(f"{talaba_0['ism'].title()}, \
# {talaba_0['yosh']} yoshda, \
# {talaba_0['t_yil']}-yilda tug'ilgan")
#
# talaba_1 = {}
# talaba_1['ism'] = 'ismoil karimov'
# talaba_1['kurs'] = 1
# talaba_1['yosh']= 19
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
# talaba_1['kurs']= 4  # 4- kursga o'zgartirmiz
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_0 = {'ism':'Jonibek O\'ralov', 'yosh':20, 'yil':2001}
print(talaba_0)
del talaba_0['yosh']
print(talaba_0)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'note 12',
    'orif':'nokia 3310'
}

phone = telefonlar['ali']
print(f"Alining telefoni {phone}")

phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(f"Hasanning telefoni {phone}")