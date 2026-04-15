# class Avto:
#
#     def __init__(self,model,rang,korobka,narh,yili):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.yili = yili
#         self.probeg = 135000
#
#     def get_info(self):
#             return f"Modeli {self.model} rangi {self.rang} korobkasi {self.korobka} narhi {self.narh}" \
#             f" yili {self.yili} probegi {self.probeg}"
#
#     def get_model(self):
#         return self.model
#     def get_rang(self):
#         return self.rang
#     def get_korobka(self):
#         return self.korobka
#     def get_narh(self):
#         return self.narh
#     def get_yili(self):
#         return self.yili
#     def get_probeg(self):
#         return self.probeg
#     def set_probeg(self,probeg):
#         self.probeg = probeg
#     def update_probeg(self):
#         self.probeg +=1
#
# avto1 = Avto("KIA", "Qora", "avtomat", 22500, 2024)
# print(avto1.get_info())
# avto1.set_probeg(100000)
# print(avto1.probeg)



class Avtosalon:

    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.newautos = []

    def get_info(self):
        return f"Avtosalon nomi: {self.nomi}, manzili: {self.manzili}, sotuvdagi avtomobillar soni: {len(self.newautos)}"

    def get_name(self):
        return self.nomi

    def get_manzili(self):
        return self.manzili

    def get_avtosoni(self):
        return len(self.newautos)

    def add_newauto(self, newauto):
        self.newautos.append(newauto)

    def show_autos(self):
        return self.newautos

avtosalon1 = Avtosalon("Yunusobod", "Toshkent shahri")

avtosalon1.add_newauto("Malibu")
avtosalon1.add_newauto("Cobalt")
avtosalon1.add_newauto("Gentra")

print(avtosalon1.get_info())
print(f"Avtosalon: {avtosalon1.get_name()}. Avtolar: {avtosalon1.show_autos()}. Avtolar soni: {avtosalon1.get_avtosoni()}")