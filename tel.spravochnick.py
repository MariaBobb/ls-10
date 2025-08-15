contacts = { }

def input_contacts():
    name = input("Введите имя: ")
    phone = input("Введите десятизначный номер телефона, начиная с 9 : ")
    if len(phone) == 10 and phone.isdigit() and phone.startswith("9"):
        contacts[name] = phone
        print("Контакт успешно добавлен!")
        print(contacts)
    else:
        print("Неверно введен номер телефона")
def find_contact():
    name = input("Введите имя для поиска: ")
    print(contacts.get(name,"Контак не найден!"))
    # if name in contacts:
    #     print(contacts[name])
    # else:
    #     print("контакт не найден!")

def delete_name():
    name = input("Введите имя для удаления: ")
    try:
        del contacts[name]
        print(contacts)
        print("Контакт успешно удален!")
    except KeyError:
        print("Контакт не найден!")
    
while True:
    action = int(input("Выберете действие: добавить(1), найти (2), удалить (3), выйти (4)"))
    if action == 1:
        input_contacts()
    elif action == 2:
        find_contact()
    elif action == 3:
        delete_name()
    elif action == 4:
        break
    else:
        print("Неверный ввод. Выберете 1,2,3 или 4. ")