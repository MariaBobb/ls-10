import datetime

#t = datetime.datetime.now() #текущее время
#print("Текущее время:", t)

#d = datetime.date.today()  #текуща дата

#print("Сегодня: ", d)

# красивый вывод даты
#date = d.strftime("%d %B %Y")

#print("Форматированная дата: ", date)

#date = d.strftime("%d.%m.%Y")
#print("Форматированная дата: ", date)

#d = datetime.date.today() #текуща дата
# ru = ""
# m = d.month #храним номер месяца
# print(f"Сегодня: {m}")
# if m == 1:
#     ru = "января"
# elif m == 2:
#     ru = "февраля"
# elif m == 3:
#     ru = "марта"
# elif m == 4:
#     ru = "апреля"
# elif m == 5:
#     ru = "мая"
# elif m == 6:
#     ru = "июня"
# elif m == 7:
#     ru = "июля"
# elif m == 8:
#     ru = "августа"
# elif m == 9:
#     ru = "сентября"
# elif m == 10:
#     ru = "октября"
# elif m == 11:
#     ru = "ноября"
# elif m == 12:
#     ru = "декабря"
#print(f"Сегодня {d.day} {ru} {d.year} года.")

import datetime

t = datetime.date.today()
ru = ""
m = t.month
s = ["января","февраля","марта","апреля","мая","июня","июля","августа","снтября","октября","ноября","декабря"]
month_ru = s[m-1]

print(f"Сегодня {t.day} {month_ru} {t.year} года.")