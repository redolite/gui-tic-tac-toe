from tkinter import Frame, Label, Button, TOP, Y, RIGHT

class MainMenuFrame(Frame):
    def __init__(self, master, on_start_game_btn_click):
        super().__init__(master)
        self.title = Label(self, text = "GUI-Tic-Tac-Toe",
            font = ("InterFace XBold", 30)
        )
        self.button = Button(
        self,
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
        borderwidth=4,
        command=on_start_game_btn_click
        )
        self.quit_button = Button(
        self,
        text = 'Выйти из игры',
        width = 15,
        height = 2,
        font = "Arial 20 bold",
        fg = '#000000',
        bg = '#ff0000',
        bd =  10,
        highlightthickness=4, 
        highlightcolor="#ff0000", 
        highlightbackground="#ff0000", 
        borderwidth=4,
        command=quit
        )

    def show(self):
        self.title.pack(side=TOP)
        self.button.pack(side=TOP, expand=True)
        self.pack(expand=True, fill=Y)
        self.quit_button.pack(side=TOP, expand=True)
    def quit(self, master):
        master.destroy()
    