# def kvadrat_fuksiya():
#     son = int(input("Istalgan son kiriting: "))
#     natija = f"{son}ning kvadrati: {son ** 2}"
#     return natija

# print(kvadrat_fuksiya())
    

# def full_name_func(first_name, last_name, name=''):
#     if name:
#         full_name = f"{first_name} {name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# student1 = full_name_func("Muhammadyusuf", "Abdusattorov")
# student2 = full_name_func("Husanboy", "Shermuhammedov")
# student3 = full_name_func("Toxirbek", "Rustamov")
# student4 = full_name_func("Izzatbek", "Azamov")
# student5 = full_name_func("Palonchi", "Pistonchiyev", "Xojayevich")
# print(student1)
# print(student5)

# print(f"Darsga kech qolgan talabalar: {student2}.\nVaqtida kelgan talabalar: {student1}, {student3}, {student4}")


# def avto_info(kompaniya, model, rangi, karobka, yili, narx=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'karobka': karobka,
#         'yili': yili,
#         'narx': narx
#     }
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2020)
# avto2 = avto_info('GM', 'Lacetti', 'oq', 'mexanik', 2018, 12000)

# print("Online savdoda mavjud avtomobillar: ")
# for avto in [avto1, avto2]:
#     if avto['narx']:
#         print(f"{avto['yili']} {avto['kompaniya']} {avto['model']}, Rangi: {avto['rangi']}, Karobka: {avto['karobka']}, Narxi: {avto['narx']}$")
#     else:
#         print(f"{avto['yili']} {avto['kompaniya']} {avto['model']}, Rangi: {avto['rangi']}, Karobka: {avto['karobka']}")



def oraliq(min, max, qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    
    return sonlar

print(oraliq(1, 51, 2))
print(oraliq(10, 21, 3))





