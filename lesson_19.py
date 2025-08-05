# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")


# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }

# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")


# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
 
phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)
