import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE, Y
window = tk.Tk()
window.geometry("800x600")
window.title('Крестики-Нолики')

title = tk.Label(main, text = "GUI-Tic-Tac-Toe",
    font = ("InterFace XBold", 30)
)
button = tk.Button(
    main,
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
main.pack(expand=True, fill=Y)
window.mainloop()