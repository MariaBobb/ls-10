from random import * 

print(randint(1,100)) # рандомное число
print(random()) # вещественное
print(randrange(0,100,10)) #10 это шаг

print(choice("питон")) #  рандомная буква из слова

#print(shuffle("питон"))

#RANDOM + циклы
import time

i = 0
while (i := i + 1) <= 10:  #проверка на истину, все что отлично от 0, кроме false, пустоц строки, none
    print(f"работаю... {i}")
    time.sleep(0.1)
    if i == 5:
        break
    else:
        print("все ок")
    print("the end")
    
    
    
    # ALT + SHIFT + F