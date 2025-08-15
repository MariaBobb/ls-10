from tkinter import*

a = 1
def change():
    global a
    a += 1
    metka['text']= a

window = Tk()
metka = Label(text="1",bg ="blue",fg='yellow',width=30, height=3)
metka.pack()
knopka= Button(text="Декремент",width=30, height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()