# ism = about_me['firstname']
# familya = about_me['lastname']
# yosh = about_me['age']
# yili = about_me['year']
# ish = about_me['jobs']
# joylashuv = about_me['address']

# print(f"Mening ismim {ism} familyam {familya}, {yili}-yilda tug'ilganman, yoshim {yosh}da, {joylashuv}da {ish} bo'lib ishlayman.")
# print(about_me.items())

# for k, q in about_me.items():
#     print(f"Kalit: {k}")
#     print(f"Qiymat: {q}")

# about_me = {'firstname': 'Sayfulloh', 'lastname': 'Mamatqulov', 'age': 28, 'year': 1997, 'jobs': 'Developer', 'address': 'Fergana'}

# print(about_me.keys())



bozorlik = ["banan", "non", "qaymoq", "sut", "tarvuz", "tuxum", "guruch", "go'sht"]
mahsulotlar = {"non": 5000, "qaymoq": 50000, "tuxum": 2000, "guruch": 50000, "go'sht": 100000, "sut": 5000, "tarvuz": 3000}

# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} narxi {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print(mahsulotlar.keys())
# print(mahsulotlar.values())

# for narx in mahsulotlar.values():
#     print(f"Mahsulot narxlari: {narx}")
    
davlatlar = {"O'zbekiston": "Toshkent", "Rossiya": "Moskva", "AQSH": "Vashington", "Turkiya": "Anqara", "Qozog'iston": "Nursulton"}
for davlat, poytaxt in davlatlar.items():
    print(f"{davlat} davlatining poytaxti {poytaxt} shahri")