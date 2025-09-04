import math
import lesson_27


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(100, 200, 300, 400, 500))


# def kopaytma(*sonlar):
#     """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija

# print(kopaytma(100, 200, 300, 400, 500))


# def kopaytma(*sonlar):
#     """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
#     return math.prod(sonlar)


# print(kopaytma(100, 200, 300, 400, 500))


# def student_info(first_name, last_name, **information):
#     information['first_name'] = first_name
#     information['last_name'] = last_name
#     return information


# student = student_info("John", "Doe", age=21, city="New York", job="Computer Science")
# print(student)


avto1 = lesson_27.avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 10000)
avto2 = lesson_27.avto_info("Tesla", "CyberTruck", "Qora", "avtomat", 2024, 50000)
lesson_27.info_print(avto1)
lesson_27.info_print(avto2)
