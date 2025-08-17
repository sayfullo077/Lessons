# def ozim_haqimda(ism, yosh, t_yil, joylashuv):
#     """Salom beruvchi funksiya
#     """
#     print(f"Assalomu alaykum, hurmatli {ism.title()}, siz {t_yil}-da {joylashuv.title()}da tug'ilgansiz. Yoshingiz {yosh}da.")

# ozim_haqimda("sayfulloh", 28, 1997, "oltiariq")
# ozim_haqimda("muhammadyusuf", 14, 2011, "oltiariq")


# def yosh_hisobla(ism, yil):
#     print(f"Assalomu alaykum, hurmatli {ism.title()}, siz {2025-yil} yoshdasiz.")
    
# yosh_hisobla(yil=1997, ism="sayfulloh")



# def kattasi():
#     son1 = int(input("Istalgan son kiriting 1: "))
#     son2 = int(input("Istalgan son kiriting 2: "))
    
#     if son1 > son2:
#         print(f"{son1} soni katta son.")
        
#     elif son1 == son2:
#         print("Bu sonlar o'zaro teng.")
        
#     else:
#         print(f"{son2} soni katta son.")
    
# kattasi()


# Foydalanuvchidan x va y sonlarini olib, x sonini y darajasini konsolga chiqaruvchi funksiya yozing.


def daraja():
    """x sonini y darajasini hisoblaydigan funksiya"""
    x = int(input("X sonini kiriting: "))
    y = int(input("Y darajasini kiriting: "))
    return x ** y

print(daraja())

