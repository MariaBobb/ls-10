
import time

i = 0
while (i := i + 1) <= 10:  #проверка на истину, все что отлично от 0, кроме false, пустоц строки, none
    print(f"работаю... {i}")
    time.sleep(0.1)
    
else:
    print("все ок")
    print("the end")
    
