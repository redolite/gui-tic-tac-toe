import tkinter as tk
from tkinter import TOP, BOTTOM, CENTER, SE, Y, BOTH

from main_menu_frame import MainMenuFrame
from game_frame import GameFrame

window = tk.Tk()

window.geometry("800x600")
window.title('Крестики-Нолики')


def start_game():
    main_menu.pack_forget()
    game.show()

def end_game():
    game.grid_forget()
    main_menu.show()



game = GameFrame(window, end_game)
main_menu = MainMenuFrame(window, start_game)
main_menu.show()
window.mainloop()
