# import random
# name = ["Маша","Петя","Галя","Таня","Юля","Варвара","Александр","Иван"]
# age = random.randint(5,25)
# rnd_name = random.randint(0,8)
# job = ["врач","стоматолог","таксист","курьер","мастер","школьник","директор"]
# rnd_job = random.randint(0,7)
# print(f"Меня зовут {name[rnd_name]}. Мне {age} лет. Я {job[rnd_job]}")

#ввод с клавиатуры

import random
name = []
job = []
names = int(input("Сколько имен введете? "))
jobs = int(input("Сколько профессий введете? "))
for i in range(names):
    name.append(input("Введите имя: "))
for i in range(jobs):
    job.append(input("Введите профессию: "))
print(name)
print(job)