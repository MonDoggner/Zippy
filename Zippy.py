#===================================================================

import AppTools #самописный пакет
import customtkinter
import os
import tempfile
import shutil
import time
from tkinter import *
from tkinter import filedialog
from datetime import datetime

#===================================================================

app = customtkinter.CTk()  
app.title("Zippy")
app.iconbitmap(default="assets\Zippy icon.ico")
app.geometry("900x700")
app.resizable(False, False)

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

sidebar_frame = customtkinter.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)

#===================================================================

def char_counter(sym_data):
    for i in sym_data:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

def counter_textbox_print():
    for i in counter:
        counter_textbox.insert(END, f''''{i}' - {counter[i]}''' + '\n')

def progress_bar():
        zippy_progress_bar['maximum'] = 100    
    
        for i in range(101):
            zippy_progress_bar['value'] = i
            zippy_progress_bar.step()
            app.update()
            time.sleep(0.1)        
        
        zippy_progress_bar['value'] = 0
        
def code_textbox_print():
    code = AppTools.encode(data)
    for ch in code:
        code_textbox.insert(END, f''''{ch}' - {code[ch]}''' + '\n')

def open_file():
    global filepath
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding= "UTF-8") as file: 
            
            global file_name #Самые важные переменные. Без них всё поломается
            global data
            global counter
                       
            try:

                file_name = os.path.basename(filepath)
                data = file.read()             
                counter = {}    
                
                char_counter(data)
                counter_textbox_print()
                progress_bar() 
                code_textbox_print()
                
                with open('AppTools\\logs.txt', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nУспешное кодирование {file_name}\n\n')

            except UnicodeDecodeError:
                with open('AppTools\\logs.txt', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nОшибка: Выбран не текстовый файл\n\n')

def save_file():
    save_filepath = filedialog.asksaveasfilename(
        initialdir='C:\\Users\\admin\\Downloads',
        initialfile=f'{os.path.splitext(file_name)[0]}',
        filetypes=[('Архив','.zip')], 
        defaultextension='.zip'
    )
    
    if save_filepath != "":
        try:
            
            temp_dir = tempfile.mkdtemp()
            shutil.copy(filepath, temp_dir)            
            temp_archive = shutil.make_archive(base_name=save_filepath, format='zip', root_dir=temp_dir)
            os.rename(temp_archive, save_filepath)

            with open('AppTools\\logs.txt', 'a', encoding='UTF-8') as logs:
                logs.write(f'{datetime.now()}\nУспешное сохранение {file_name}\n\n')

        except Exception as e:
            with open('AppTools\\logs.txt', 'a', encoding='UTF-8') as logs:
                logs.write(f'{datetime.now()}\nОшибка: {e}\n\n')

#===================================================================
                
counter_textbox = customtkinter.CTkTextbox(app, width=600)    
counter_textbox.grid(row=0, column=1, padx=50, pady=55, sticky='ne')

zippy_progress_bar = customtkinter.CTkProgressBar(master=app, determinate_speed=0.5)
zippy_progress_bar.grid(row=1, column=1, padx=250, pady=10, sticky='ne')
zippy_progress_bar.set(0)

code_textbox = customtkinter.CTkTextbox(app, width=600)    
code_textbox.grid(row=2, column=1, padx=50, pady=35, sticky='ne')

#===================================================================

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
    label_padx=100, 
    label_pady=20, 
    label_sticky='nw'
)

code_label = AppTools.Labels(
    label_master=app,
    label_name='Кодирование',
    label_row=2, 
    label_column=1, 
    label_padx=100, 
    label_pady=0, 
    label_sticky='nw' 
)

open_file_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='Open file',
    button_image = 'assets\\open.png',
    button_func=open_file,
    button_relx=0.17,
    button_rely=0.2,
    button_anchor=NW
)  

save_file_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='Save file',
    button_image = 'assets\\save.png',
    button_func=save_file,
    button_relx=0.17,
    button_rely=0.25,
    button_anchor=NW
)  

about_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='About',
    button_image = 'assets\\about.png',
    button_func=...,
    button_relx=0.17,
    button_rely=0.9,
    button_anchor=NW
)

app.mainloop()
