# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")  

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")


cars=[]

for n in range(10):
    new_car = {
        'model': 'Malibu',
        'rang': None,
        'yil': 2020,
        'narh': None,
        'km': 0,
        'korobka': 'avto'
    }
    cars.append(new_car)
     
for car in cars[:3]:
    car['rang'] = 'qizil'
    car['narh'] = 15000
       
for car in cars[3:6]:
    car['rang'] = 'oq'
    car['narh'] = 20000
    
for car in cars[6:]:
    car['rang'] = 'qora'
    car['narh'] = 25000
    
# print(cars)

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#'],
    'sardor':['java','go'],
    }

print(dasturchilar.keys())
print(dasturchilar.values())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')

        



