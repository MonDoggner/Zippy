import customtkinter
from tkinter import *
from tkinter import filedialog

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

zippy_logo = customtkinter.CTkLabel(
sidebar_frame, 
text='Zippy', 
font=('system', 40)
)
zippy_logo.grid(row=0, column=0, padx=20, pady=(20, 10))

counter_label = customtkinter.CTkLabel(
app, 
text='Подсчёт символов', 
font=('system', 22)
)
counter_label.grid(row=0, column=1, padx=30, pady=20, sticky='nw')

counter_textbox = customtkinter.CTkTextbox(app, width=600)    
counter_textbox.grid(row=0, column=1, padx=20, pady=55, sticky='nw')

code_label = customtkinter.CTkLabel(
app, 
text='Кодирование', 
font=('system', 22)
)
code_label.grid(row=1, column=1, padx=30, pady=0, sticky='nw')

code_textbox = customtkinter.CTkTextbox(app, width=600)    
code_textbox.grid(row=1, column=1, padx=20, pady=35, sticky='nw')

def open_file_func():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding= "UTF-8") as file: 
            data = file.read()
            counter = {}
            temp_keys = []
            temp_values = []
            

    for i in data:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for i in counter:
        counter_textbox.insert(END, f''''{i}' - {counter[i]}''' + '\n')
        temp_keys.append(i)
        temp_values.append(counter[i])

    print(temp_keys)
    print(temp_values)

open_file_button = customtkinter.CTkButton(
master=app,
width=100,
height=25,
border_width=0,
corner_radius=8,
text='Open file',
font=('system', 20),
command=open_file_func
)    
open_file_button.place(relx=0.025, rely=0.15, anchor=NW)    

app.mainloop()
