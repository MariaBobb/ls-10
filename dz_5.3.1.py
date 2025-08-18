# проект бронирования мест

from tkinter import*
from tkinter import messagebox as mb


def book_seat(event=None):
    s  = seat_entry.get().upper()
    try:
        if seats[s] == "свободно":
            seats[s] = "забронировано"
            update_canvas() 
            mb.showinfo("Успех", f'место {s} успешно забронировано')
        else:
            mb.showinfo("Ошибка",f'место {s} забронировано или не существует.')
    except KeyError:
        mb.showinfo("Ошибка",f"Место {s} не существует!")


def update_canvas():
    canvas.delete("all")
    for i, (seat,status) in enumerate(seats.items()):
        x = i*40 +20
        y = 20
        color ='green' if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x + 15, y + 15, text=seat) 
        
           
def book_cancel(event=None):
    s  = seat_cansel.get().upper()
    try:
        if seats[s] == "забронировано":
            seats[s] = "свободно"
            update_canvas() 
            mb.showinfo("Успех", f'Бронь места {s} успешно отменена')
        else:
            mb.showinfo("Ошибка",f'место {s} не забронировано или не существует.')
    except KeyError:
        mb.showinfo("Ошибка",f"Место {s} не существует!")
    
    
window = Tk()
window.title("Бронирование мест")
window.geometry("400x280")
    
canvas = Canvas(width=400,height=80)
canvas.pack(pady=10)

seats = {f"Б{i}":"свободно" for i in range(1,10)}
update_canvas() 


frame_top= Frame(window)
frame_top.place(x=10, y=70)


canvas1 = Canvas(frame_top, width=30, height=30, bg='white')
canvas1.pack(side=LEFT,padx=10, pady=5)
canvas1.create_rectangle(0, 0, 29, 29, fill='green', outline='black')

label = Label(frame_top, text="Свободно", fg="black",font=("Arial", 10))
label.pack(side=LEFT,padx=10, pady=5)
canvas2 = Canvas(frame_top, width=30, height=30, bg='white')
canvas2.pack(side=LEFT,padx=10, pady=5)
canvas2.create_rectangle(0, 0, 29, 29, fill='red', outline='black')
label = Label(frame_top, text="Забронировано", fg="black",font=("Arial", 10))
label.pack(side=LEFT,padx=10, pady=5) 


seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind("<Return>",book_seat)
    
Button(text="Забронировать место",command=book_seat).pack(pady=10)

seat_cansel = Entry()
seat_cansel.pack(pady=10)
seat_cansel.bind("<Return>",book_cancel)
    
Button(text="Отменить бронь",command=book_cancel).pack(pady=10)
    
window.mainloop()

    