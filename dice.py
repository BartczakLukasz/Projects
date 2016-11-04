import Tkinter
import tkMessageBox
from random import randint
tplyer = 0
tcomp = 0
player = 0
comp = 0
top = Tkinter.Tk()
top.resizable(width = False, height =False)
top.geometry("250x200")
def Yes():
   global player
   global comp
   tplayer = randint(1,6)
   tcomp = randint(1,6)
   message =""
   if tplayer>tcomp:
      message = "you win!"
      player+=1
   elif tplayer==tcomp:
      message = "it's a draw"
   else:
      message = "you lose!"
      comp +=1
   tkMessageBox.showinfo( "Results", "You: "+str(player)+"     Comp: "+str(comp)+"\nYou have trown "+str(tplayer)+"\n"+"Computer has trown "+str(tcomp)+"\n"+message)
def No():
   tkMessageBox.showinfo( "Wery well", "See ya!!")
   top.quit()
w = Tkinter.Label(top,text = "Want to play some dice?\n")
B1 = Tkinter.Button(top, text ="Yes", command = Yes,width = 10)
B2 = Tkinter.Button(top, text = "No", command = No,width = 10)
w.grid(row = 0,column = 0)
B1.grid(row = 1, column = 0)
B2.grid(row = 1, column = 1)
top.mainloop()
