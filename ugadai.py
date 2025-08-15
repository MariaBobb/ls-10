from tkinter import*
from tkinter import messagebox as mb
import random


def check():
    s = e.get()
    s = int(s)
    rnd = random.randint(1,10)
    if s==rnd:
        mb.showinfo(title="Результат", message='Угадал!')
    else:
        mb.showinfo(title="Результат", message='Неудача...')
    answer = mb.askretrycancel(title="Вопрос",message = "Загадать еще?")  #askyesno да/нет  askokcancel ок/отмена askretrycancel повтор/отмена
    if answer:
        e.delete(0,END)
    else:
        window.destroy()  #закроет окно
    

window = Tk()
window.title("Игра 'Угадай число")
m1 = Label(text='Введи число и нажми на кнопку.')
e = Entry()
e.pack()
b = Button(text = "Угадать", command=check)
b.pack()
m = Label(height=3,width=40)
m.pack()

window.mainloop()
