import AppTools #самописный пакет
import customtkinter
from tkinter import *
from datetime import datetime
from tkinter import filedialog

#стандартное создание окна приложения
app = customtkinter.CTk()  
app.title("Zippy")
app.iconbitmap(default="Zippy icon.ico")
app.geometry("900x700")
app.resizable(False, False)

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)

counter_textbox = customtkinter.CTkTextbox(app, width=600)    
counter_textbox.grid(row=0, column=1, padx=20, pady=55, sticky='nw')

code_textbox = customtkinter.CTkTextbox(app, width=600)    
code_textbox.grid(row=1, column=1, padx=20, pady=35, sticky='nw')

#подписи
zippy_logo = AppTools.Labels(
    label_master=sidebar_frame, 
    label_name='Zippy', 
    label_font=('system', 40),
    label_row=0, 
    label_column=0, 
    label_padx=20, 
    label_pady=(20, 10),
    label_sticky=None
)

counter_label = AppTools.Labels(
    label_master=app,
    label_name='Подсчёт символов', 
    label_row=0, 
    label_column=1, 
    label_padx=30, 
    label_pady=20, 
    label_sticky='nw'
)

code_label = AppTools.Labels(
    label_master=app,
    label_name='Кодирование',
    label_row=1, 
    label_column=1, 
    label_padx=30, 
    label_pady=0, 
    label_sticky='nw' 
)

#функции
def char_counter(sym_data):
    for i in sym_data:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

def counter_textbox_print():
    for i in counter:
        counter_textbox.insert(END, f''''{i}' - {counter[i]}''' + '\n')

def code_textbox_print():
    code = AppTools.encode(data)
    for ch in code:
        code_textbox.insert(END, f''''{ch}' - {code[ch]}''' + '\n')

def logs_textbox_print(data):
    code_textbox.insert(END, f''''{data}''' + '\n')

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding= "UTF-8") as file: 
            global data
            global counter            
            try:
                data = file.read()             
                counter = {}    
                char_counter(data)
                counter_textbox_print() 
                code_textbox_print()
                with open('AppTools\\logs.txt', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nУспешное кодирование {filepath}\n\n')
            except UnicodeDecodeError:
                with open('AppTools\\logs.tx', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nОшибка: Выбран не текстовый файл\n\n')

#кнопки
open_file_button = AppTools.Buttons(
    button_master=app,
    button_name='Open file',
    button_func=open_file,
    button_relx=0.025,
    button_rely=0.15,
    button_anchor=NW
)  

save_file_button = AppTools.Buttons(
    button_master=app,
    button_name='Save file',
    button_func=open_file,
    button_relx=0.025,
    button_rely=0.2,
    button_anchor=NW
)  

app.mainloop()
