# проект бронирования мест
#список мест будет в виде списка кортежей

#[["Б1","свободно"],["Б2","свободно"]]

def book_seat(seats):
    s  = input("Введите место для бронирования (от Б1 до Б9): ")
    if seats[s] == "свободно":
        seats[s] = "забронировано"
        print(f'место {s} успешно забронировано')
    else:
        print(f'место {s} забронировано или не существует.')

seats = {f"Б{i}":"свободно" for i in range(1,10)}
print(seats)        
while True:
    book_seat(seats)
    booking = input("Хотите забронировать еще одно место? (да/нет): ")
    if booking.lower() != "да":
        break

print("Итоговое состояние бронирования местю")
for seat in seats:
    print(f"{seat[0]} : {seat[1]}")