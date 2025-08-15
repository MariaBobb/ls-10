# Структуры даннх
# список list[], кортеж (), множество {}
# марк луц по пайтону

# СПИСОК
import turtle as t
x = []
y = list()

# может хранить что угодно
#x= (1, 3.14, True, "hello", [1,2,3], t)
#print(x[0])
#print(x[-1][1])

shoplist = ["яюлоки","манго",'морковь',"бананы"]
print("я должен сделать", len(shoplist),"покупки.")

print("Покупки:", end ="")

for item in shoplist:
    print(item)
print()
print(*shoplist)
print("\n Теперь я должен купить рис")

shoplist.append("рис") #добавить в список

print(shoplist)
shoplist.sort()
print("отсортировть список:", *shoplist)
print("напечатать первое", shoplist[0])

del shoplist[0] #удалить первое в списке
print("Теперь мой список такой:", shoplist)

print("манго" in shoplist)

print(shoplist.count("манго"))
print(shoplist.index("манго"))

shoplist.remove("манго")
print(shoplist)

#пока есть удаляй

while "манго" in shoplist:
    shoplist.remove("манго")
print(shoplist)

shoplist.pop() # удвляет последний элемент, можно указать индекс

while shoplist:
    x = shoplist.pop()
    print(x)
print(shoplist)

#либо

shoplist.clear()

print(id(shoplist))



#кортеж

x = tuple("корртеж")
y = list("кортеж")

print(x.__sizeof__())
print(y.__sizeof__())








