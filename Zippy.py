import customtkinter
from tkinter import *
from tkinter import filedialog

app = customtkinter.CTk()  
app.geometry("800x600")
app.title("Zippy")

code_list = [] # Список, куда будут записываться символы из тексте (в виде чисел из словаря)

# Словарь со всеми возможными символами для русского языка
all = [
        "А", 
        "Б", 
        "В",
        "Г",
        "Д",
        "Е",
        "Ё", 
        "Ж", 
        "З", 
        "И", 
        "Й", 
        "К", 
        "Л", 
        "М", 
        "Н", 
        "О", 
        "П", 
        "Р", 
        "С", 
        "Т", 
        "У", 
        "Ф", 
        "Х", 
        "Ц", 
        "Ч", 
        "Ш", 
        "Щ", 
        "Ъ", 
        "Ы", 
        "Ь", 
        "Э", 
        "Ю",
        "Я",
        "а", 
        "б", 
        "в", 
        "г", 
        "д", 
        "е", 
        "ё",
        "ж", 
        "з", 
        "и", 
        "й", 
        "к", 
        "л", 
        "м", 
        "н", 
        "о", 
        "п", 
        "р", 
        "с", 
        "т", 
        "у", 
        "ф", 
        "х", 
        "ц", 
        "ч", 
        "ш",  
        "щ", 
        "ъ", 
        "ы", 
        "ь", 
        "э", 
        "ю",
        "я",    
        " ",
        ",",
        ".",
        "-",
        "+",
        "/",
        "*",
        "(",
        ")", 
        "{",
        "}",
        "[",
        "]",
        "?",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "№",
        ">",
        "<",
        ":",
        ";",
        "'",
        '"',
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "\n",
        "\t"
    ]

#Функция выводит в терминал числовые значения каждого символа
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding= "UTF-8") as file: 
            data = file.read()
            print(data) 
            for i in data:
                if i in all:
                    code_list.append(all.index(i))
            print(*code_list)               
                    


open_button = customtkinter.CTkButton(
    master=app,
    width=120,
    height=32,
    border_width=0,
    corner_radius=8,
    text='Open file',
    command=open_file)    
open_button.place(relx=0.5, rely=0.5, anchor=CENTER)


app.mainloop()
