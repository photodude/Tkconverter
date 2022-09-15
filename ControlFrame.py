# source https://www.pythontutorial.net/tkinter/tkraise/
import tkinter as tk
from tkinter import ttk
from ConverterFrame import ConverterFrame
from TemperatureConverter import TemperatureConverter

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'
        self.container = container

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='F to C',
            value=0,
            variable=self.selected_value,
            command=lambda:self.change_frame()).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='C to F',
            value=1,
            variable=self.selected_value,
            command=lambda:self.change_frame()).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.change_frame()

    def f_to_c(self):
        self.frames[0] = ConverterFrame(
            self.container,
            'Fahrenheit',
            TemperatureConverter.fahrenheit_to_celsius
            )
    def c_to_f(self):
        self.frames[1] = ConverterFrame(
            self.container,
            'Celsius',
            TemperatureConverter.celsius_to_fahrenheit
            )

    def change_frame(self):
        active_frame = self.selected_value.get()
        if active_frame == 0:
            self.f_to_c()
        elif active_frame == 1:
            self.c_to_f()
        else:
            self.f_to_c()

        for frame in self.frames.values():
            frame.reset()
            frame.grid_remove()
        frame = self.frames[active_frame]
        frame.reset()
        frame.tkraise()
        frame.grid()
        frame.focus_set()
