# from datetime import datetime, timedelta
#
# bugun = datetime.today()
# for i in range(10):
#     sana = bugun + timedelta(weeks=2*i)
#     print(sana.strftime("%d/%m/%Y"))
import re

# import datetime as dt
# bugun = dt.date.today()
# qurbon = dt.date(2026, 5, 27)
# farq = qurbon - bugun
# print(f"Qurbon hayitigacha {farq.days} kun qoldi")


# import datetime as dt
# bugun = dt.date.today()
# tkunim = dt.date(2007, 12, 28)
# farq = bugun - tkunim
#
# yil = farq.days
# oy = (farq.days %365)
# kun = (farq.days % 365)
# print(f"Tug'ilgan kunimdan {yil}, {kun} kun, {oy} oy o'tdi")


# import re
#
# andoza = r'^998(33|88|90|91|93|94|95|97|98|99|71|77|50|20)\d{7}$'
# msg = ("Telefon raqamingizni kiriting: ")
#
# while True:
#     telraqam = input(msg)
#     if re.match(andoza, telraqam):
#         print("Telefon raqam mos keldi")
#         break
#     else:
#         print("Telefon raqam mos kelmadi")


matn = """Internet olami juda keng bo‘lib, unda har qanday ma’lumotni topish mumkin. Masalan, bilim olish uchun wikipedia.org saytidan foydalanish juda qulay va foydalidir. Shuningdek, dasturlashni o‘rganishda w3schools.com sahifasi eng yaxshi manbalardan biri hisoblanadi. Agar sizga turli mavzularda video darsliklar kerak bo‘lsa, youtube.com platformasi aynan siz uchun. Kundalik yangiliklar va ijtimoiy muloqot uchun esa kun.uz kabi nashrlarni muntazam kuzatib borish mumkin."""

andoza =  r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b'
webadres = re.findall(andoza, matn)
print(webadres)