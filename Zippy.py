'''
Архиватор, демонстрирующий работу алгоритма Хаффмана
'''

#===================================================================

import AppTools #самописный пакет
import customtkinter
import os
import zipfile
import shutil
import time
from tkinter import *
from tkinter import filedialog
from PIL import Image

#===================================================================

app = customtkinter.CTk()  
app.title('Zippy')
app.iconbitmap(default=os.path.join(os.path.dirname(__file__), 'assets', 'Zippy icon.ico'))
app.geometry('900x700')
app.resizable(False, False)

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

sidebar_frame = customtkinter.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
sidebar_frame.grid_rowconfigure(4, weight=1)

#===================================================================

def char_counter(char_data):
    for i in char_data:

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
    filepath = filedialog.askopenfilename(filetypes=[('Текстовые файлы', '*.txt')])

    if filepath != '':
        with open(filepath, 'r') as file: 
            
            global file_name #Самые важные переменные. Без них всё поломается
            global data
            global counter                       

            file_name = os.path.basename(filepath)
            data = file.read()             
            counter = {}    
                
            char_counter(data)
            counter_textbox_print()
            progress_bar() 
            code_textbox_print()

def save_file():
    save_filepath = filedialog.asksaveasfilename(
        initialdir=r'C:\Users\admin\Downloads',
        initialfile=f'{os.path.splitext(file_name)[0]}',
        filetypes=[('Archive', '.zip')],
        defaultextension='.zip'
    )

    if save_filepath != "":
        progress_bar()
        with zipfile.ZipFile(save_filepath, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
            zip_file.write(filepath, os.path.basename(filepath))

def select_extract_dir():
    extract_dir = filedialog.askdirectory()
    return extract_dir

def unpack_zip():
    zip_filepath = filedialog.askopenfilename()

    if zip_filepath != '':
        extract_dir = select_extract_dir()
        if extract_dir:
            progress_bar()
            shutil.unpack_archive(filename=zip_filepath, extract_dir=extract_dir)

about_counter = 0

def about():

    global about_counter     
    about_counter += 1

    about_image = customtkinter.CTkImage(
        light_image=Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'photo_2024-03-12_22-53-28.jpg')),
        dark_image=Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'photo_2024-03-12_22-53-28.jpg')),
        size=(200, 200)
    )

    if about_counter % 3 != 0:

        about_window = customtkinter.CTkToplevel()
        about_window.title('About')
        about_window.geometry('300x400')
        about_window.resizable(False, False)

        about_label = customtkinter.CTkLabel(
            master=about_window, 
            text='Zippy',
            font=('system', 40),
        )
        about_label.pack(expand=True)

        about_textbox = customtkinter.CTkTextbox(about_window, width=210, height=250) 
        about_textbox.pack(expand=True)
        about_textbox.insert(END, 
'''============Zippy===========\n
О программе:\n-Архиватор текстовых файлов.\n
Версия:\n1.1\n===========================\n
Разработал:\n-Бухаров Арсений\n
Руководитель:\n-Суханов Леонид Николаевич''')
        
    else:
        about_window = customtkinter.CTkToplevel()
        about_window.title('About')
        about_window.geometry('300x400')
        about_window.resizable(False, False)

        i_about_label = customtkinter.CTkLabel(
            master=about_window, 
            text='',
            image=about_image
        )
        i_about_label.pack(expand=True)

        s_about_label = customtkinter.CTkLabel(
            master=about_window, 
            text='Спасибо, что пользуешься, чумба!\nДобра, позитива, carpe diem',
            font=('system', 22),
        )
        s_about_label.pack(expand=True)    

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
    button_image = os.path.join(os.path.dirname(__file__), 'assets', 'open.png'),
    button_func=open_file,
    button_relx=0.15,
    button_rely=0.2,
    button_anchor=NW
)  

unpack_zip_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='Unpack  ',
    button_image = os.path.join(os.path.dirname(__file__), 'assets', 'open.png'),
    button_func=unpack_zip,
    button_relx=0.15,
    button_rely=0.25,
    button_anchor=NW
)

save_file_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='Save file',
    button_image = os.path.join(os.path.dirname(__file__), 'assets', 'save.png'),
    button_func=save_file,
    button_relx=0.15,
    button_rely=0.3,
    button_anchor=NW
)  

about_button = AppTools.Buttons(
    button_master=sidebar_frame,
    button_name='About',
    button_image = os.path.join(os.path.dirname(__file__), 'assets', 'about.png'),
    button_func=about,
    button_relx=0.17,
    button_rely=0.9,
    button_anchor=NW
)

app.mainloop()
