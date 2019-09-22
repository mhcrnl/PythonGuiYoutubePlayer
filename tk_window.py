#!/usr/bin/python3
"""
    OS: Ubuntu 18.04.03 LTS
    Python 3.7.1:
        "$ python
        3.7.1 "
    Tkinter 8.6 :
        ">>> import tkinter
         >>> tkinter.TkVersion
         8.6 "
    FILE: tk_windoy.py - boiler plate for tkinter
    CREATED: 22.9.19
    AUTHOR:  mhcrnl@gmail.com
    
    RUN COMAND:
            python tk_window.py
"""
import os
import webbrowser

import requests
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, width=489, height=67, bg="blue",
                          *args, **kwargs)
        self.parent = parent

        # create the rest of gui here

        ttk.Label(parent, text="Youtube search for:").pack()
        query = ttk.Entry(parent).pack()
        tk.Button(parent, text="Search", command=self.play).pack()
        tk.Button(parent, text="Quit", command=self.quit).pack()

    def quit(self):
        self.parent.destroy()

    def play(self):
        url = 'https://www.youtube.com/watch?v=ECs1Gh5Q198'
        source_code = requests.get(url,timeout=15)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Gui Youtube Player")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
 
