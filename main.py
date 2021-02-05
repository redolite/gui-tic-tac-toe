import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE
window = tk.Tk()
window.geometry("800x600")
window.title('Крестики-Нолики')

title = tk.Label(window, text = "GUI-Tic-Tac-Toe",
    font = ("InterFace XBold", 30)
)
button = tk.Button(
    window,
    text = 'Начать игру',
    width = 15,
    height = 2,
    font = "Arial 20 bold",
    fg = '#000000',
    bg = '#32CD32',
    bd =  10,
    highlightthickness=4, 
    highlightcolor="#32CD32", 
    highlightbackground="#32CD32", 
    borderwidth=4
    # borderwidth = '2',
    # highlightcolor = 'black'
)

title.pack(side=TOP)
button.pack(side=TOP, expand=True)
window.mainloop()