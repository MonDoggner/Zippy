'''
Библеотека, упрощающая создание элементов GUI
'''
import customtkinter
from tkinter import *
from tkinter import filedialog
from datetime import datetime
from PIL import Image

class Buttons:
    '''
    Класс, создающий кнопки.
    Теперь мы можем размещать их без отдельной функции!
    '''
    def __init__(self, button_master:any, button_name, button_relx, button_rely, button_anchor, button_func, button_image:None) -> None:

        self.button_master = button_master
        self.button_name = button_name
        self.button_relx = button_relx
        self.button_rely = button_rely
        self.button_anchor = button_anchor
        self.button_func = button_func
        self.button_image = button_image

        button = customtkinter.CTkButton(
            master=self.button_master,
            width=100,
            height=25,
            border_width=0,
            corner_radius=8,
            text=self.button_name,
            font=('system', 20),
            image=customtkinter.CTkImage(dark_image=Image.open(self.button_image)),
            command=self.button_func
        )    
        button.place(relx=self.button_relx, rely=self.button_rely, anchor=self.button_anchor)

class Labels:
    '''
    Класс, создающий подписи.
    Теперь мы можем размещать их без отдельной функции!
    '''
    def __init__(self, label_master, label_name, label_row, label_column, label_padx, label_pady, label_sticky, label_font=('system', 22)) -> None:
        
        self.label_master = label_master
        self.label_name = label_name
        self.label_font = label_font
        self.label_row = label_row
        self.label_column = label_column
        self.label_padx = label_padx
        self.label_pady = label_pady
        self.label_sticky = label_sticky

        label = customtkinter.CTkLabel(
            master=self.label_master, 
            text=self.label_name, 
            font=self.label_font
        )
        label.grid(row=self.label_row, column=self.label_column, padx=self.label_padx, pady=self.label_pady, sticky=self.label_sticky)
