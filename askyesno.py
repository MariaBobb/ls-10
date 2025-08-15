from tkinter import*
from tkinter import messagebox as mb

def check():
    answer = mb.askretrycancel(title="Вопрос",message = "Передать данные?")  #askyesno да/нет  askokcancel ок/отмена askretrycancel повтор/отмена
    if answer:
        s = e.get()
        e.delete(0,END)
        m["text"] = s
    

window = Tk()
e = Entry()
e.pack()
b = Button(text = "Передать?", command=check)
b.pack()
m = Label(height=3)
m.pack()
window.mainloop()
