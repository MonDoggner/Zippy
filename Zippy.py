import customtkinter
from tkinter import *
from tkinter import filedialog

app = customtkinter.CTk()  
app.title("Zippy")
app.iconbitmap(default="Zippy icon.ico")
app.geometry("800x600")
app.resizable(False, False)

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)

zippy_label = customtkinter.CTkLabel(
sidebar_frame, 
text='Zippy', 
font=('system', 40)
)
zippy_label.grid(row=0, column=0, padx=20, pady=(20, 10))

textbox = customtkinter.CTkTextbox(app, width=600)    
textbox.grid(row=0, column=1, padx=20, pady=10, sticky='n')

def open_and_count():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r", encoding= "UTF-8") as file: 
            data = file.read()
            counter = {}

    for i in data:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for i in counter:
        print(f'{i} - {counter[i]}')

    textbox.insert(END, 'Подсчёт символов:\n\n')
    for i in counter:
        textbox.insert(END, f''''{i}' - {counter[i]}''' + '\n')

open_button = customtkinter.CTkButton(
master=app,
width=100,
height=25,
border_width=0,
corner_radius=8,
text='Open file',
font=('system', 20),
command=open_and_count
)    
open_button.place(relx=0.03, rely=0.15, anchor=NW)    

app.mainloop()
