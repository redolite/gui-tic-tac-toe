import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE, Y, BOTH

from main_menu_frame import MainMenuFrame
from game_frame import GameFrame

window = tk.Tk()

window.geometry("800x600")
window.title('Крестики-Нолики')


def start_game():
    main_menu_frame.destroy()
    game = GameFrame(window)
    game.show()


main_menu_frame = MainMenuFrame(window, start_game)
window.mainloop()
