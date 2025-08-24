# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting\n", end="")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka turi: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no):")
#     if javob.lower() != 'yes':
#         break
    
# print("\nRo'yxatdagi avtomobillar:")
# for a in avtolar:
#     print(f"{a['yil']} {a['kompaniya']} {a['model']}, Rangi: {a['rang']}, Karobka: {a['korobka']}, Narxi: {a['narh']}$")
    
    
"""
Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
"""

# def user_info(ismi, familiyasi, t_yil, t_joy, email=None, telefon=None):
#     user = {'ismi':ismi,
#             'familiyasi':familiyasi,
#             't_yil':t_yil,
#             't_joy':t_joy,
#             'email':email,
#             'telefon':telefon}
#     return user


# print("Foydalanuvchi ro'yxatini shakllantiramiz.")
# users = []

# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting\n", end="")
#     ismi=input("Foydalanuvchi ismi: ")
#     familiyasi=input("Foydalanuvchi familyasi: ")
#     t_yil=input("Tug'ilgan yili: ")
#     t_joy=input("Tug'ilgan joyi: ")
#     email=input("Foydalanuvchi emaili: ")
#     telefon=input("Foydalanuvchi telefon raqami: ")
    
#     users.append(user_info(ismi, familiyasi, t_yil, t_joy, email, telefon))
#     javob = input("Yana foydalanuvchi qo'shasizmi? (yes/no):")
#     if javob.lower() != 'yes':
#         break
    
# print("\nRo'yxatdagi Foydalanuvchilar:")
# for a in users:
#     print(f"Foydalanuvchi ismi {a['ismi']}\nFoydalanuvchi familiyasi {a['familiyasi']}\nFoydalanuvchi tug'ilgan yili {a['t_yil']},\nFoydalanuvchi tug'ilgan joyi {a['t_joy']},\nFoydalanuvchi pochtasi {a['email']},\nFoydalanuvchi telefon raqami {a['telefon']}$")
    