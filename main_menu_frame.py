from tkinter import Frame, Label, Button, TOP, Y

class MainMenuFrame(Frame):
    def __init__(self, master, onclick):
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
        command=onclick
        )
        self.title.pack(side=TOP)
        self.button.pack(side=TOP, expand=True)
        self.pack(expand=True, fill=Y)