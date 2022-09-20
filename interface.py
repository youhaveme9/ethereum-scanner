import tkinter as tk
from turtle import title
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ttkbootstrap.themes.user as theme

print(theme.USER_THEMES)

root = ttk.Window(themename="darkly", title="Hello", size=(500, 500))
l1 = ttk.Label(bootstyle="success", text="Hello")
l1.pack(side=LEFT, padx=5, pady=10)

root.mainloop()