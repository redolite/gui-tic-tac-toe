import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE, Y, BOTH

from main_menu_frame import MainMenuFrame
window = tk.Tk()

window.geometry("800x600")
window.title('Крестики-Нолики')
game = tk.Frame(window, bg="red")

def start_game():
    main_menu_frame.destroy()
    game.pack(fill=BOTH, expand=True)

main_menu_frame = MainMenuFrame(window, start_game)
window.mainloop()