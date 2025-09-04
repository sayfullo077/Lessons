# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar

# talabalar = ["Izzatbek", "Tohirjon", "Husanboy"]
# baholar = bahola(talabalar)
# print(baholar)


# def katta_harf(ismlar):
#     return [ism.title() for ism in ismlar]

    
# ismlar = ["izzatbek", "tohirjon", "husanboy"]
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)



# *args - (*arguments)

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(100, 200, 300, 400, 500))
    

# def summa(x, y, *sonlar):
#         return x + y + sum(sonlar)

# print(summa(2))

# **kwargs — keyword arguments (kalit so'zli argumentlar)


# def avto_info(kompaniya, model, **malumotlar):
#     """Avtomobil haqida ma'lumot qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "Malibu", rang="qora", yil=2018)
# avto2 = avto_info("Kia", "K5", rang="qizil", narh=35000)

# print(avto1)
# print()
# print(avto2)


def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {
        "kompaniya":kompaniya,
        "model": model,
        "rang": rangi,
        "karobka": karobka,
        "yil": yili,
        "narh": narhi
    }
    return avto


def avto_kirit():
    avtolar=[]
    while True:
        print("\n Quyidagi ma'lumotlarni kiriting: ", end="")
        kompaniya = input("Ishlab chiqaruvchi")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        karobka = input("Karobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narhi = input("Narhi: ")
        
        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
        javob = input("Yana avto qo'shasizmi? yes/no")
        if javob == "no":
            break
        
    return avtolar


def info_print(avto_info):
    """Avtolar haqidagi salqangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info["rang"].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['karobka']} karobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    





