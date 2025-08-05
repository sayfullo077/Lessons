toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz

# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)


#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"