#def my_sum(a,b,*c):
#    print(a,b,c)
#    #return a+b

#my_sum(1,2,3,4,5)

#print(y)


#def my_sum(*a):
#    s = 0
#    for x in a:
#        s+=x 
#    return s
#r = my_sum(1,2,3,4,5)
#print(r)

#def avg(*a,точность =4):
#    x = sum(a)/len(a)
#    return round(x,точность)

#r = avg(1,2,3,4,3)
#print(r)


#определить является ли слово полиндромом с помощью функции

#def get_palindrome(word):
#    word =word.lower()
#    print("Yes" if word ==word[::-1] else "NO")
    
#get_palindrome("Анна")
#get_palindrome("шалаШ")
#get_palindrome("принт")

#объявить функцию для проверки числа на четность

#def is_odd(x):
#    return x%2 !=0
#print(is_odd(3))


# чтобы вывел 11,15,3
#st = [8,11,15,3,2,10]

#st = [ x for x in st if is_odd(x) ]
#print(st)

#проверить может ли получиться треугольник

#def is_triangle(a,b,c):
#    return a+b>c and a+c>b and b+c>a
#print(is_triangle(3,4,5))
#print(is_triangle(3,4,8))

# принимает строки и заключает в указанный тег

#def get_html(s,tag = 'h1'):
#    return f'<{tag}>{s}</{tag}>'
    
    
#html = get_html("Hello Python")
#print(html)    

#html = get_html("Hello Python", tag ="div")
#print(html)

#def get_rect_value(a,b,type =0):
#    return 2*(a+b) if type == 0 else a*b

#res1 = get_rect_value(5,2)
#res2 = get_rect_value(5,2, type ='1')
#print(res1,res2)        

#5! = 1*2*3*4*5 =120

#F(n) =F(n-1)*n  рекруция

def F(n):
    if n==1: return 1
    return F(n-1)*n
res = F(5)
print(res)

# 1,1 2,3,5,8,12 -фибоначи
#F(1) +1, F(2) = 1
# F(n)= F(n-1) +F(n-2)

def fib(n):   
    if n==1 or n==2: return 1
    return fib(n-1) +fib(n-2)
print(fib(8))

#lambda

#анонимная функция

def y(x): return  x **2

y= lambda x: x **2
z = y(5)
print(z)


x = [1,2,3,4,5]
y1 = map(y,x)
print(*y1)


cities = ["Москва", "Париж","лондон","Челябинск","Питер","Ростов-на-Дону", "Нижний Новгород"]
# по алфавиту
cities.sort()
print(*cities, sep="\n")
# по доине
cities.sort(key=len)
print(*cities, sep ="\n")

# по последней букве  и первой букве

cities.sort(key=lambda x:(x[-1], x[0]))
print(*cities, sep ='\n')

import time
start = time.perf_counter()
[x ** 2 for x in range (10**7)]
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")
