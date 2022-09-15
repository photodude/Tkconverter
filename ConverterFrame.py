# source https://www.pythontutorial.net/tkinter/tkraise/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class ConverterFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter
        # tag = str(self)
        # self._add_bindtag(self, tag)
        # self.bind_class(tag, '<Return>', lambda *args: self.enter_key())

        self.master.bind('<Return>', self.convert)

        # field options
        options = {'padx': 5, 'pady': 0}

        # temperature label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w', **options)

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
        self.temperature_entry.focus()

        # button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button.grid(column=2, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)
        # self.convert_button.bind('<Return>', lambda event=None: self.convert)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''

    def enter_key(self):
        self.convert()

    # def _add_bindtag(self, widget, tag):
    #     bindtags = widget.bindtags()
    #     if tag not in bindtags:
    #         widget.bindtags((tag,) + bindtags)
    #     for child in widget.winfo_children():
    #         self._add_bindtag(child, tag)
