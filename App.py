import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from ControlFrame import ControlFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry('300x120')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()