from tkinter import*


def change():
    metka['text'] = "Черная метка!"
    metka['bg'] = 'black'

window = Tk()
metka = Label(text="Привет!",bg="yellow",fg="red",
              width=30,height=5)  #bg - заливка текста, fg - изменение цвета  #изменение размера сетки width=315,height=5
metka.pack()
knopka = Button(text="Изменить метку", width=15,height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
