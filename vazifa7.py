# def sonlar_kopaytmasi(*args):
#     """Sonlar ko'paytmasini hisoblovchi dastur"""
#     p = 1
#     for x in args:
#         p *= x
#     return p
# print(sonlar_kopaytmasi(5,7))



# def talabalar(ism,familiya,**malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar
# talaba = talabalar("Tohir", "Shonazarov", rangi = 'qora', yil=2015)
# print(talaba)



# def jami_narx(*args, **kwargs):
#     jami = sum(args)
#     if 'discount' in kwargs:
#         discount = kwargs['discount']
#         jami = jami - (jami*discount/100)
#
#     return jami
# print(jami_narx(100000, 300000, 80000, discount=20))



# def join_words(*args, **kwargs):
#     sep = kwargs.get('sep', ' ')
#     return sep.join(args)
#
# print(join_words("Men", "Ismoil", "Karimov"))



def  add_words(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    return sep.join(args)
print(add_words("Mening", "do'stim", "Tohir", sep="-"))