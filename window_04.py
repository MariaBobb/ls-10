from tkinter import*
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def read():
    t=text.get(1.0,END)
    print(t)

def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open (file, 'r') as f:
                s=f.read()
            text.insert(1.0,s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'файл не найден.')
    except Exception as e:
        mb.showerror("Ошибка", f"Неизвестная ошибка: {e}")
    
    
def delete():
    text.delete(1.0,END)
def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(("TXT files","*.txt"),
                       ("all files:","*.*")))
        if file:
            with open(file,'w') as f:
                s = text.get(0,END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'файл не найден.')
    except Exception as e:
        mb.showerror("Ошибка", f"Неизвестная ошибка: {e}")
def quit(): 
    window.destroy()
            
window = Tk()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть",command=insert)
filemenu.add_command(label="Новый",command=delete)
filemenu.add_command(label="Сохранить",command=save)

filemenu.add_separator()
filemenu.add_separator()

filemenu.add_command(label="Выход", command=quit)

mainmenu.add_cascade(label="Файл", menu=filemenu)

text = Text(width=50, height=30,bg='black',fg='white')
text.pack(side=LEFT)
scroll = Scrollbar(command = text.yview)
scroll.pack(side=LEFT,fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text="Ввод", command=read)
b.pack()
b2 = Button(text="Открыть файл", command=insert)
b2.pack()

b3 = Button(text="Удаление текста", command=delete)
b3.pack()
b4 = Button(text="Сохранить", command=save)
b4.pack()



window.mainloop()