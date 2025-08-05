sonlar = list(range(0,10)) # 
print(sonlar)

juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

ismlar = ["Ali", "Vali", "Zokir", "Toshmat", "Xolmat"]
sonlar = list(range(1, 6))

print(sonlar[0], ismlar[0])
print(sonlar[1], ismlar[1])
print(sonlar[2], ismlar[2])
print(sonlar[3], ismlar[3])
print(sonlar[4], ismlar[4])

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)


cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars) 