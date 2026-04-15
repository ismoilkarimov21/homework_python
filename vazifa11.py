# with open('pi_million_digits.txt', 'r') as fayl:
#     pi = fayl.read()
#     if "28122007" in pi:
#         print("Ushbu raqamlar orasida tug'ilgan kuningiz uchraydi.")
#     else:
#         print("Afsuski tu'gilgan sanangiz topilmadi🥲")

# with open('pi_million_digits.txt', 'r') as fayl:
#     pi_matn = fayl.read()
# pi_float = float(pi_matn[:50])
# print(pi_float)

class User:
    def __init__(self,ism,familiya,yoshi):
        self.ism = ism
        self.familiya = familiya
        self.yoshi = yoshi

    def get_name(self):
        return self.ism
    def get_familiya(self):
        return self.familiya
    def get_yoshi(self):
        return self.yoshi
    def get_info(self):
        return f"Ismi: {self.ism}. Familiyasi: {self.familiya}. Yoshi: {self.yoshi}. "
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yoshi = int(input("Yoshingizni kiriting: "))

user1 = User(ism,familiya,yoshi)
print(user1.get_info())

with open("users.txt", "a") as fayl:
    fayl.write(user1.get_info() + "\n")

print("Ma'lumot faylga yozildi.")