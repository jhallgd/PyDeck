from tkinter import *
import blackJack_model as blj

game = blj.black_jack()
game.startGame()

window = Tk()
canvas = Canvas()

window.maxsize(600, 600) 
window.title("PyDeck: Black Jack")

frame = Frame(window)
frame.pack()

window.mainloop()   