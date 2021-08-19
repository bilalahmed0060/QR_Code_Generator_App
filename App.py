from tkinter import *
from PIL import Image,ImageTk


root = Tk()

backs = ImageTk.PhotoImage(Image.open('static/Loading_Screen.png'))

w = int(root.winfo_screenwidth()/2 - 250)
h = int(root.winfo_screenheight()/2 - 200)

root.geometry('500x400+%s+%s' % (w,h))
root.overrideredirect(True)

Label(root,image=backs).place(x=0,y=0,relwidth=1,relheight=1)

root.update()
root.after(2500)
root.destroy()
import Main_Window
root.mainloop()

# from PIL import Image,ImageTk
#
