class User:
    def __init__(self,ism, username, familiya, email):
        self.ism = ism
        self.username = username
        self.familiya = familiya
        self.email = email
    def get_name(self):
        return self.ism
    def get_username(self):
        return self.username
    def get_familiya(self):
        return self.familiya
    def get_email(self):
        return self.email
    def tanishtir(self):
        print(f"Ismim {self.ism}, usernamim {self.username}, familiyam {self.familiya}, emailim {self.email}")

foydalanuvchi = User("Tohir", "Tohir07", "Shonazarov", "tohir81@gmail.com")
foydalanuvchi2 = User("Jasur", "Jasur08", "Otaboyev", "jasurbek087@gmail.com")
foydalanuvchi3 = User("Elbek", "Elton08", "Qadamboyev", "elton003@gmail.com")
foydalanuvchi4 = User("Sherali", "Sherbektrk", "Shonazarov", "sherbekkrash@gmail.com")
print(f"{foydalanuvchi.ism} {foydalanuvchi.username} {foydalanuvchi.familiya} {foydalanuvchi.email}")

print(f"Foydalanuvchi ismi: {foydalanuvchi.get_name()}, usernamesi: {foydalanuvchi.get_username()}, " \
      f"familiyasi: {foydalanuvchi.get_familiya()}, emaili: {foydalanuvchi.get_email()}")

print(foydalanuvchi4.tanishtir())