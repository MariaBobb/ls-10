# f = open("books.txt",encoding="utf-8")

# for _ in range(3):
#     print(f.readline().strip())
# f.seek(0)
# s = (f.read()
#      .replace(',', '')
#      .replace('.', '')
#      .replace('"', '')
#      .split())
# print(max(s, key=len))


# # Апельсин маракуйя папайя айва Яблоко
# # апельсин яблоко ананас банан персик Слива
# # Банан груша слива виноград авокадо Цитрон
# # Слива Груша яблоко мандарин цитрон
# # лимон Лайм апельсин ананас персик айва
# # Хурма киви хурма манго авокадо лайм
# # Нектарин Инжир гранат Папайя Гранат
# f = open("fruit.txt", encoding='utf-8')
# s = f.read().lower().split()

# # dict
# d = {}
# for word in s:
#     d[word] = s.count(word)
# print(*d.items(), sep='\n')

# d = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(*d, sep='\n')


import tkinter as tk
root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("800x600")
text = tk.Text(root, height=8, width=40)
text.pack(pady=50)
text_2 = tk.Text(root, height=1, width=40)
text_2.pack(padx=350)

def open_file():
    f = open("fruit.txt", encoding='utf-8')
    s = f.read()
    text.insert(tk.END, s)
          
def count_words():
    c = text.get("1.0", tk.END)
    c = c.split()
    text_2.insert(tk.END, len(c))
   
open_btn = tk.Button(root, text="Открыть файл", command=open_file)
open_btn.pack(pady=5)
btn_2 = tk.Button(root, text="Посчитать слова", command=count_words)
btn_2.pack(pady=50)


root.mainloop()