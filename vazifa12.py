import json
#
# data = {
#     "Model": "Malibu",
#     "Rang": "Qora",
#     "Yil": 2020,
#     "Narh": 40000
# }
#
# data_json = json.dumps(data)
# print(data_json)
#
#
# talaba_json = """{"ism":"Hasan", "familiya": "Husanov", "tyil": "2000"}"""
#
# talaba = json.loads(talaba_json)
# print(talaba["ism"], talaba["familiya"])
#
# with open('data.json', 'w') as file:
#     json.dump(data, file)
# print(data)
#
# with open('talaba.json', 'w') as f:
#     json.dump(talaba, f)
# print(talaba)

# ISHLAMADI
# with open('students.json', 'r') as f:
#     students = json.load(f)
#
# for talaba in students:
#     print(f"{talaba["ism"]} {talaba["familiya"]}, {talaba["kurs"]}-kurs, {talaba["fakultet"]} fakultet talabasi")

info_json = {"batchcomplete":"","query":{"pages":{"13801":{"pageid":13801,"ns":0,"title":"Python","extract":"Python ([\u02c8p\u028c\u026a\u03b8 (\u0259)n] \u2014 payton, piton) \u2014 turli sohalar uchun yuqori darajadagi umumiy maqsadli dasturlash tili. Uning dizayn falsafasi muhim chekinishdan foydalangan holda kodning o\u02bbqilishiga urg\u02bbu beradi. Uning til konstruksiyalari va obyektga yo\u02bbnaltirilgan yondashuvi dasturchilarga kichik va yirik loyihalar uchun aniq, mantiqiy kod yozishda yordam berishga qaratilgan. Shuningdek Python sun\u02bciy intellekt hamda ma\u02bclumotlar muhandisiligi sohalarining tili hisoblanadi.\nPython deyarli barcha platformalarda ishlay oladi, xususan Windows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar shular jumlasidandir. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud bo\u02bblib, uning nomi \u2014 IronPython dasturlash muhitidir.\nGuido van Rossum 1980-yillarning oxirida ABC dasturlash tilining davomchisi sifatida Python ustida ishlay boshladi va birinchi marta 1991-yilda Python 0.9.0 versiyasini ommaga e\u02bclon qildi.\nPython dasturlash tiliga bo\u02bblgan talab yildan yilga oshib bormoqda. CodingDojo portalining tadqiqotlariga ko\u02bbra, 2020\u20142021-yillarda aynan Python tilida dasturlovchi mutaxassislarga eng ko\u02bbp talab bo\u02bblgan."}}}}
page = info_json["query"]["pages"]["13801"]
print(page["title"])
print(page["extract"])
