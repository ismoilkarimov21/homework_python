# def user_info(ism, familiya, t_yil, t_joy, yosh, e_manzil=None, tel_raqam=None,):
#     user = {
#         'ism': ism,
#         'familiya':familiya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'e_manzil':e_manzil,
#         'tel_raqam':tel_raqam,
#         'yosh':yosh
#     }
#     return user
# print("Foydalanuvchi haqida ma'lumot beramiz")
# malumot = []
# while True:
#     print("So'rovnomani to'ldiring")
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_yil = input("Tug'ilgan yilingizni kiriting: ")
#     t_joy = input("Tug'ilgan joyingizni kiriting: ")
#     e_manzil = input("Emailingizni kiriting: ")
#     tel_raqam = int(input("Telefon raqamingizni kiriting: "))
#     yosh = int(input("Yoshingizni kiriting: "))
#     malumot.append(user_info(ism, familiya, t_yil,t_joy,e_manzil,tel_raqam,yosh))
#
#     javob = input("Yana user qo'shasizmi? (ha/yo'q)")
#     if javob == "ha":
#         continue
#     else:
#         break
# print(malumot)



# def mijoz_info(ism, familiya, t_yil, t_joy, email=None, tel=None):
#     mijoz = {
#         'ism':ism,
#         'familiya':familiya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'email':email,
#         'tel':tel
#     }
#     return mijoz
# print("Mijoz haqida malumot")
# mijozlar = []
# while True:
#     print("Mijoz malumotlarini kiriting: ")
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     t_joy = input("Manzilingizni kiriting: ")
#     email = input("Email kiriting: ")
#     tel = input("Tel raqam kiriting: ")
#     mijozlar.append(mijoz_info(ism, familiya, t_yil, t_joy, email, tel))
#     javob = input("Yana mijoz qo'shasizmi ? (ha/yo'q)")
#
#     if javob.lower() !='ha':
#         break
# for m in mijozlar:
#     print(f"{m['ism']} {m['familiya']}, {m['t_yil']} yil, {m['t_joy']} da yashaydi ")

# def kattasini_top(a, b, c):
#     return max(a, b, c)
# print(f"Ushbu sonlardan kattasi: {kattasini_top(12, 367, 10000)}")

# def aylana_info(radius, pi= 3.14159):
#     aylana = {
#         'radius': radius,
#         'diametr': 2 * radius,
#         'perimetr': 2 * pi * radius,
#         'yuza': pi * (radius ** 2)
#     }
#     return aylana
# print( aylana_info(5))

def tub_sonlar_top(min,max):
    tub_sonlar = []
    for n in range(min, max+1):
        if n<2: continue
        tub = True
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                tub = False
                break
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar
print(tub_sonlar_top(1,100))