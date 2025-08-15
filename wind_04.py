from tkinter import*


def read_name():
    name = e.get()
    print(name)
    e.delete(0,END)
def read_city():
    city = c.get()
    print(city)
    c.delete(0,END)
    
window = Tk()

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

m = Label(frame_top, text="Введите имя: ", justify="center",fg='green', font='Courier 18')
m.pack(side=LEFT)
e = Entry(frame_top, width=50,bg='grey',fg='white', font='Courier 18')  #justify выравнивание
e.pack(side=LEFT)
b1 = Button(frame_top,text="Ввод ", justify="center",fg='green', font='Courier 18',command=read_name)
b1.pack()
m1 = Label(frame_bottom, text="Введите город: ", justify="center",fg='green', font='Courier 18')
m1.pack(side=LEFT)
c = Entry(frame_bottom, width=50,bg='grey',fg='white', font='Courier 18')  #justify выравнивание
c.pack(side=LEFT)
b = Button(frame_bottom,text="Ввод ", justify="center",fg='green', font='Courier 18',command=read_city)
b.pack()
window.mainloop()
