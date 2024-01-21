import customtkinter
import heapq
from tkinter import *
from datetime import datetime
from tkinter import filedialog
from collections import Counter, namedtuple

class Node (namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

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
    code = huffman_encode(data)
    for ch in code:
        code_textbox.insert(END, f''''{ch}' - {code[ch]}''' + '\n')

def huffman_encode(data):
    line = []

    for ch, freq in Counter(data).items():
        line.append((freq, len(line), Leaf(ch)))

    heapq.heapify(line)

    count = len(line)
    while len(line) > 1:
        freq1, _count1, left = heapq.heappop(line)
        freq2, _count2, right = heapq.heappop(line)
        heapq.heappush(line, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if line:
        [(_freq, _count, root)] = line
        code = {}
    root.walk(code, '')
    
    return code  

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
                with open('logs.txt', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nУспешное кодирование {filepath}\n\n')
            except Exception as e:
                with open('logs.txt', 'a', encoding='UTF-8') as logs:
                    logs.write(f'{datetime.now()}\nОшибка:{e}\n\n')

def logs_textbox_print(data):
    code_textbox.insert(END, f''''{data}''' + '\n')

def logs_open():   

    counter_label.destroy()
    counter_textbox.destroy()
    code_label.destroy()
    code_textbox.destroy()

    logs_label = customtkinter.CTkLabel(
        app, 
        text='История', 
        font=('system', 22)
    )
    logs_label.grid(row=1, column=1, padx=30, pady=0, sticky='nw')

    logs_textbox = customtkinter.CTkTextbox(app, width=600)    
    logs_textbox.grid(row=1, column=1, padx=20, pady=35, sticky='nw')


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

open_file_button = customtkinter.CTkButton(
    master=app,
    width=100,
    height=25,
    border_width=0,
    corner_radius=8,
    text='Open file',
    font=('system', 20),
    command=open_file
)    
open_file_button.place(relx=0.025, rely=0.15, anchor=NW)

logs_button = customtkinter.CTkButton(
    master=app,
    width=100,
    height=25,
    border_width=0,
    corner_radius=8,
    text='Logs',
    font=('system', 20),
    command=logs_open
)    
logs_button.place(relx=0.025, rely=0.2, anchor=NW)

app.mainloop()
