def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        else:
            print("Это не целое число!")

# add = lambda x,y: x+y
# subtruck = lambda x,y: x-y
# multiply = lambda x,y: x*y
# divide = lambda x,y: "Ошибка. Деление на ноль" if y==0 else x/y
def add(x,y):
    return x + y
def subtruck(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    # if y==0:
    #     return "Ошибка деление на ноль"
    # else:
    #     return x/y
    try:
        return x / y
    except ZeroDivisionError:
        return "Ошибка. Деление на ноль"
    except TypeError:
        return "Ошибка типа данных."
    
print("Выберите операцию: ")
print("1.сложение")
print('2.вычитание')
print('3.умножение')
print('4.деление')

valid_choices = ["1","2","3","4"]
choice = None

while choice not in valid_choices:
    choice = input("введит номер операции (1,2,3,4):")
    if choice not in valid_choices:
        print("Вы ввели не 1,не 2,не3 и не 4")

num1 =  get_number("Введите 1 число: ")
num2 =  get_number("Введите 2 число: ")

if choice == "1":
    print(f"Результат: {num1} + {num2} = {add(num1,num2)}")
elif choice == "2":
    print(f"Результат: {num1} - {num2} = {subtruck(num1,num2)}")
elif choice == "3":
    print(f"Результат: {num1} * {num2} = {multiply(num1,num2)}")
elif choice == "4":
    res = divide(num1,num2)
    if isinstance(res,str):
        print(res)
    else:
        print(f"Результат: {num1} / {num2} = {res:.2f}")
