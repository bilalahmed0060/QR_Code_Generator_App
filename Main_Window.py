from tkinter import *
from PIL import Image,ImageTk
import qrcode
from tkinter import filedialog
# import win32gui, win32con
#
# #This code is for hiding the Command Terminal
# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide , win32con.SW_HIDE)

root = Tk()
global a
def get1(event):
    c1 = A1.get()
    c2 = A2.get()
    c3 = A3.get()
    if len(c1) > 0 or len(c2) > 0 or len(c3) > 0:
        submit['state'] = NORMAL
    else:
        submit['state'] = DISABLED

def get2(event):
    c4 = G.get('1.0','end-1c')
    if len(c4) > 0:
        submit['state'] = NORMAL
    else:
        submit['state'] = DISABLED


def Account():
    btn1['state'] = DISABLED
    btn2['state'] = NORMAL

    frames2.place_forget()
    G.delete("1.0","end")
    G.place_forget()
    frames1.place(x=20,y=98)

    A1.place(x=44, y=154)
    A2.place(x=44,y=232)
    A3.place(x=44,y=305)


def General():
    btn1['state'] = NORMAL
    btn2['state'] = DISABLED

    frames1.place_forget()

    A1.delete(0,"end")
    A2.delete(0,"end")
    A3.delete(0,"end")

    A1.place_forget()
    A2.place_forget()
    A3.place_forget()
    frames2.place(x=22,y=95)
    G.place(x=43,y=144,height=160)

def done():
    global l
    btn3['state'] = NORMAL
    btn4['state'] = NORMAL
    c1 = A1.get()
    c2 = A2.get()
    c3 = A3.get()
    c4 = G.get('1.0', 'end-1c')
    l1 = [c1,c2,c3]
    b = ""
    if len(c1) > 0 or len(c2) > 0 or len(c3) > 0:
        for x in l1:
            if len(x) == 0:
                pass
            else:
                b = b + x + "\n\n"
    else:
        b = c4

    img = qrcode.QRCode(box_size=9,border=1)
    img.add_data(b)
    img.make()
    l = img.make_image()
    l.save("qrcode_test.png")

    imgs = Image.open("qrcode_test.png")
    imgs = imgs.resize((220, 200), Image.ANTIALIAS)
    imgs = ImageTk.PhotoImage(imgs)

    qr.config(image = imgs)
    qr.photo = imgs
    qr.place(x=354,y=100)

def saving():
    global l

    a = filedialog.asksaveasfilename(filetypes=[("PNG", "*.png")])
    l.save(a + str('.png'))

def clearing():
    qr.place_forget()
    btn3['state'] = DISABLED

backs = ImageTk.PhotoImage(Image.open('static/Main_Screen.png'))
BTN1 = ImageTk.PhotoImage(Image.open('static/btn1.png'))
BTN2 = ImageTk.PhotoImage(Image.open('static/btn2.png'))
BTN3 = ImageTk.PhotoImage(Image.open('static/btn3.png'))
BTN4 = ImageTk.PhotoImage(Image.open('static/btn4.png'))
Done = ImageTk.PhotoImage(Image.open('static/submit.png'))

frame1 = ImageTk.PhotoImage(Image.open('static/frame1.png'))
frame2 = ImageTk.PhotoImage(Image.open('static/frame2.png'))

w = int(root.winfo_screenwidth()/2 - 300)
h = int(root.winfo_screenheight()/2 - 175)

root.geometry("600x350+%s+%s" % (w,h))
root.title("QRCODE MAKER")
root.resizable(0,0)

Label(root,image=backs).place(x=0,y=0,relwidth=1,relheight=1)

btn1 = Button(root,image=BTN1,bd=0,highlightthickness=0,state=DISABLED,command=Account)
btn1.place(x=20,y=62)

btn2 = Button(root,image=BTN2,bd=0,highlightthickness=0,command=General)
btn2.place(x=105,y=62)

btn3 = Button(root,image=BTN3,bd=0,highlightthickness=0,command = saving,state=DISABLED)
btn4 = Button(root,image=BTN4,bd=0,highlightthickness=0,command=clearing,state=DISABLED)

btn3.place(x=500, y=315)
btn4.place(x=415, y=315)

submit = Button(root,image=Done,bd=0,highlightthickness=0,state=DISABLED,command=done)
submit.place(x=293,y=175)

frames1 = Label(root,image=frame1,bd=0)
frames1.place(x=20,y=98)

frames2 = Label(root,image=frame2,bd=0)

A1 = Entry(root,width=33,bd=0,bg='#f594ab',fg='white')
A1.place(x=44,y=154)

A2 = Entry(root,width=33,bd=0,bg='#f594ab',fg='white')
A2.place(x=44,y=232)

A3 = Entry(root,width=33,bd=0,bg='#f594ab',fg='white',show="*")
A3.place(x=44,y=305)

G = Text(root,width=26,bd=0,bg='#f594ab',fg='white')

A1.bind("<Key>",get1)
A2.bind("<Key>",get1)
A3.bind("<Key>",get1)
G.bind("<Key>",get2)

qr = Label(root)

root.mainloop()