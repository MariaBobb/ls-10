# создать список из 20 случайных чисел
import random
random.seed(123)


lst = []

while len(lst)<20:
    x = random.randint(-100, 100)
    lst.append(x)
print(*lst)
    
#lst = [random.randint(-100,100) for _ in range(20)]
#print(*lst)

#random.seed()  #условно рандомная послеовательность

#посчитать сумму чисел
#s,i = 0,0
#while i<len(lst):
#    s+=lst[i]
#    i+=1    
#print("Сумма чисел равно: ",s)

#сумма четных чисел
#первый способ
#s,i =0,0
#while  i < len(lst):
#    s+=lst[i] if lst[i]%2 ==0 else 0
#    print(i,lst[i],s)
#    i+=1
#print("Сумма четных чисел равна: ", s)
#второй способ
#s,i =0,-1

#while  i < len(lst)-1:
#    i+= 1
#    if lst[i]%2 !=0:
#        continue
#    s+= lst[i]
#    print(i,lst[i],s)
    
#print("Сумма четных чисел равна: ", s)

# сумма чисел заканчивающихся на 3

s,i =0,-1

while  i < len(lst):
    
    if abs(lst[i])%10 ==3:  #abs чтобы отрицательные числа давали верное окончание! особенность питона. берем по модулю
        s+= lst[i]
    i+= 1
    
print("Сумма четных чисел равна: ", s)

# нацти максимальное число в списке

m,i = lst[0],0

while i < len(lst):
    if lst[i] > m:
        m = lst[i]
        
    i+=1
print("Максимальный элемент в списке: ", m, max(lst))

#минимальное значение в списке
m,i = lst[0],0

while i < len(lst):
    if lst[i]<m:
        m = lst[i]
    i+=1
print("Минимальное значение в писке: ", m,min(lst))
  