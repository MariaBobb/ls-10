from tkinter import*


def read_name():
    name = e.get()
    print(name)
    e.delete(0,END)
def read_last_name():
    last_name= l.get()
    print(last_name)
    l.delete(0,END)
def read_patronymic():
    patronymic= p.get()
    print(patronymic)
    p.delete(0,END)
    
window = Tk()

frame1 = Frame()
frame2= Frame()
frame3= Frame()
frame1.pack()
frame2.pack()
frame3.pack()

m = Label(frame1, text="Введите имя: ", justify="center",fg='green', font='Courier 18')
m.pack(side=LEFT)
e = Entry(frame1, width=50,bg='grey',fg='white', font='Courier 18')  
e.pack(side=LEFT)
b1 = Button(frame1,text="Ввод ", justify="center",fg='green', font='Courier 18',command=read_name)
b1.pack(side=LEFT)
m1 = Label(frame2, text="Введите фамилию: ", justify="center",fg='green', font='Courier 18')
m1.pack(side=LEFT)
l = Entry(frame2, width=50,bg='grey',fg='white', font='Courier 18')  
l.pack(side=LEFT)
b = Button(frame2,text="Ввод ", justify="center",fg='green', font='Courier 18',command=read_last_name)
b.pack(side=LEFT)
m2 = Label(frame3, text="Введите отчество: ", justify="center",fg='green', font='Courier 18')
m2.pack(side=LEFT)
p = Entry(frame3, width=50,bg='grey',fg='white', font='Courier 18')  
p.pack(side=LEFT)
b2 = Button(frame3,text="Ввод ", justify="center",fg='green', font='Courier 18',command=read_patronymic)
b2.pack(side=LEFT)

window.mainloop()
