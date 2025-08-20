from tkinter import*
import os
import shutil
from tkinter import filedialog as fd

window = Tk()
window.withdraw()

direct = fd.askdirectory(title="Выберите папку с документами для их копирования")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        print(f"Папка {new_dir} уже существует")
    for file in os.listdir(direct):
        if file.lower().endswith((".doc",".docx")):
            source_file = os.path.join(direct,file)
            destination = os.path.join(new_dir,file)
            try:
                shutil.move(source_file,destination)
                print("Файл перемещен")
            except Exception as e:
                print(f"Ошибка перемещения {file}:{e}")
    print("Все скопировано")
else:
    print("Папка не была выбрана")
    

window.mainloop()