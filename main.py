import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE
window = tk.Tk()
window.geometry("800x600")

title = tk.Label(window, text = "GUI-Tic-Tac-Toe",
    font = ("InterFace XBold", 30)
)
button = tk.Button(
    window,
    text = 'Начать игру',
    width = 15,
    height = 2,
    font = "Arial 20 bold",
)

title.pack(side=TOP)
button.pack(side=TOP, expand=True)
window.mainloop()