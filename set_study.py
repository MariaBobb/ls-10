# множество - изменяемое
# только уникальные значения

mn = set()

mn = {1,2,1,2,4,3,2,3}
print(mn)

mn.add(101) # добавление, рандомное - отсуствует индексация

print(mn)

mn.update([6,7,8,9,10,"hello"])
print(mn)


# МОЖЕТ ХРАНИТЬ НЕИЗМЕНЯЕМЫЕ ДАННЫЕ -(ВСЕ КРОМЕ СПИСКА И МНОЖЕСТВА)
#НЕТ ИНДЕКСОВ
# НЕУПОРЯДОЧНАЯ СТРУКТУРА


mn.remove("hello")
print(mn)

mn.discard("hello")
print(mn)

mn.pop()
print(mn)

mn.clear()
print(mn)