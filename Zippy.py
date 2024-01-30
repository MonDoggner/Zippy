from typing import Optional, Tuple, Union
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

class App(customtkinter.CTk):
    '''
    Класс, который создаёт "основу" приложения
    '''
    def __init__(self, app_name: str, app_icon: str, app_size: str, app_resizable: bool):
        super().__init__()

        self.app_name = app_name
        self.app_icon = app_icon
        self.app_size = app_size
        self.app_resizable = app_resizable

        self.title(f'{self.app_name}')
        self.iconbitmap(default=f'{self.app_icon}')
        self.geometry(f'{self.app_size}')

        if self.app_resizable == True:
            self.resizable()
        else:
            self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.app_logo = customtkinter.CTkLabel(
            self.sidebar_frame, 
            text=f'{self.app_name}', 
            font=('system', 40)
        )
        self.app_logo.grid(row=0, column=0, padx=20, pady=(20, 10))



class FirstScreen(App):
    def __init__(self, app_name: str, app_icon: str, app_size: str, app_resizable: bool):
        super().__init__(app_name, app_icon, app_size, app_resizable)

        self.counter_label = customtkinter.CTkLabel(
            self, 
            text='Подсчёт символов', 
            font=('system', 22)
        )
        self.counter_label.grid(row=0, column=1, padx=30, pady=20, sticky='nw')

        self.counter_textbox = customtkinter.CTkTextbox(self, width=600)    
        self.counter_textbox.grid(row=0, column=1, padx=20, pady=55, sticky='nw')

        self.code_label = customtkinter.CTkLabel(
            self, 
            text='Кодирование', 
            font=('system', 22)
        )
        self.code_label.grid(row=1, column=1, padx=30, pady=0, sticky='nw')

        self.code_textbox = customtkinter.CTkTextbox(self, width=600)    
        self.code_textbox.grid(row=1, column=1, padx=20, pady=35, sticky='nw')

        self.open_file_button = customtkinter.CTkButton(
            master=self,
            width=100,
            height=25,
            border_width=0,
            corner_radius=8,
            text='Open file',
            font=('system', 20),
            command=FirstScreen.open_file
        )    
        self.open_file_button.place(relx=0.025, rely=0.15, anchor=NW)

    @classmethod
    def open_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath != "":
            with open(self.filepath, "r", encoding= "UTF-8") as file: 
                global data
                global counter            
                try:
                    data = file.read()             
                    counter = {}    
                    self.char_counter(data)
                    self.counter_textbox_print() 
                    self.code_textbox_print()
                    with self.open('logs.txt', 'a', encoding='UTF-8') as logs:
                        logs.write(f'{datetime.now()}\nУспешное кодирование {self.filepath}\n\n')
                except UnicodeDecodeError:
                    with open('logs.txt', 'a', encoding='UTF-8') as logs:
                        logs.write(f'{datetime.now()}\nОшибка: Выбран не текстовый файл\n\n')
    @classmethod
    def char_counter(self, char_data):
        for i in char_data:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

    @classmethod
    def counter_textbox_print(self):
        for i in counter:
            self.counter_textbox.insert(END, f''''{i}' - {counter[i]}''' + '\n')

    @classmethod
    def code_textbox_print(self):
        code = self.huffman_encode(data)
        for ch in code:
            self.code_textbox.insert(END, f''''{ch}' - {code[ch]}''' + '\n')    

    @classmethod
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
    
    @classmethod
    def destroyer(self):
        self.counter_label.destroy()
        self.counter_textbox.destroy()
        self.code_label.destroy()
        self.code_textbox.destroy()

app = FirstScreen(
    app_name='Zippy', 
    app_icon='Zippy icon.ico', 
    app_size='900x700', 
    app_resizable=False
)

def logs_textbox_print(self, data):
    self.logs_textbox.insert(END, f''''{data}''' + '\n')

def logs_open(self):   

    self.destroyer()  

    logs_label = customtkinter.CTkLabel(
        app, 
        text='История', 
        font=('system', 22)
    )
    logs_label.grid(row=1, column=1, padx=100, pady=0, sticky='nw')

    logs_textbox = customtkinter.CTkTextbox(app, width=600)    
    logs_textbox.grid(row=1, column=1, padx=100, pady=35, sticky='nws')

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
