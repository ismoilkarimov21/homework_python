class Shaxs:
    def __init__(self, ism, familiya, passport):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport

    def get_info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Passport: {self.passport}"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def get_info(self):
        return f"Fan nomi: {self.nomi}"


class Talaba(Shaxs):
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, kurs, stipendiya=0):
        super().__init__(ism, familiya, passport)
        self.kurs = kurs
        self.__stipendiya = stipendiya
        self.fanlar = []
        Talaba.__talabalar_soni +=1

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def get_stipendiya(self):
        return self.__stipendiya

    def add_stipendiya(self,summa):
        if summa >=0:
            self.__stipendiya += summa
        else:
            print("Stipendiyani kamaytirib bo'lmaydi!!!")

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_fanlar(self):
        if self.fanlar:
            return [fan.nomi for fan in self.fanlar]
        return []

    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni

    def get_info(self):
        return f"Talaba: {self.ism} {self.familiya}, passport: {self.passport}, kurs: {self.kurs}, fanlar soni: {len(self.fanlar)}"


class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, mutaxassislik, ish_staji):
        super().__init__(ism, familiya, passport)
        self.mutaxassislik = mutaxassislik
        self.ish_staji = ish_staji

    def dars_berish(self):
        return f"{self.ism} {self.familiya} dars bermoqda"

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, mutaxassislik: {self.mutaxassislik}, ish staji: {self.ish_staji} yil"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, username, email):
        super().__init__(ism, familiya, passport)
        self.username = username
        self.email = email

    def login(self):
        return f"{self.username} tizimga kirdi"

    def get_info(self):
        return f"Foydalanuvchi: {self.ism} {self.familiya}, username: {self.username}, email: {self.email}"


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, username, email):
        super().__init__(ism, familiya, passport, username, email)

    def ban_user(self):
        return "Foydalanuvchi bloklandi"

    def get_info(self):
        return f"Admin: {self.ism} {self.familiya}, username: {self.username}, email: {self.email}"


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, dokon_nomi, tajriba):
        super().__init__(ism, familiya, passport)
        self.dokon_nomi = dokon_nomi
        self.tajriba = tajriba

    def sotish(self):
        return f"{self.ism} mahsulot sotmoqda"

    def get_info(self):
        return f"Sotuvchi: {self.ism} {self.familiya}, do'kon: {self.dokon_nomi}, tajriba: {self.tajriba} yil"


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, manzil, telefon):
        super().__init__(ism, familiya, passport)
        self.manzil = manzil
        self.telefon = telefon

    def xarid_qilish(self):
        return f"{self.ism} xarid qilmoqda"

    def get_info(self):
        return f"Mijoz: {self.ism} {self.familiya}, manzil: {self.manzil}, telefon: {self.telefon}"


fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Informatika")

talaba1 = Talaba("Ismoil", "Karimov", "AB1234567", 1, 570000)
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
print(Talaba.get_talabalar_soni())
print(talaba1.get_info())
talaba1.add_stipendiya(120000)
print(f"Talabaning stipendiyasi: {talaba1.get_stipendiya()}")
print("Talabaning fanlari:", talaba1.get_fanlar())

talaba1.remove_fan(fan1)
print("Fan o'chirilgandan keyin:", talaba1.get_fanlar())
print(talaba1.remove_fan(fan3))

print()

professor1 = Professor("Ali", "Valiyev", "CD7654321", "Matematika", 15)
print(professor1.get_info())
print(professor1.dars_berish())

print()

foydalanuvchi1 = Foydalanuvchi("Hasan", "Aliyev", "EF1112223", "hasan01", "hasan@gmail.com")
print(foydalanuvchi1.get_info())
print(foydalanuvchi1.login())

print()

admin1 = Admin("Admin", "Boss", "GH3334445", "admin01", "admin@gmail.com")
print(admin1.get_info())
print(admin1.login())
print(admin1.ban_user())

print()

sotuvchi1 = Sotuvchi("Sardor", "Tursunov", "IJ5556667", "Techno Shop", 4)
print(sotuvchi1.get_info())
print(sotuvchi1.sotish())

print()

mijoz1 = Mijoz("Madina", "Qodirova", "KL7778889", "Toshkent", "+998901234567")
print(mijoz1.get_info())
print(mijoz1.xarid_qilish())