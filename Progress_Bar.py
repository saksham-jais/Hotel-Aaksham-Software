from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk
import mysql.connector as connector
import os
import warnings
warnings.filterwarnings('ignore')
root = Tk()
con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='Wings',
                        database='Login')
cur = con.cursor()
height = 400
width = 730
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)
root.config(background="blue")
image = ImageTk.PhotoImage(Image.open("./assets/progress.png").resize((width,height)) )
bg_label= Label(root, image=image, bg="#2F6C60")
bg_label.place(x=0, y=0)
progress_label= Label(root, text="", font=("Ubuntu Mono", 1, "italic"), fg="#536ca6", bg="#536ca6")
progress_label.place (x=30, y=370)
progress=ttk.Style()
progress.theme_use('alt')
progress.configure ("red.Horizontal.TProgressbar", background='gold')
progress = Progressbar (root,orient=HORIZONTAL, length=730, mode='determinate' ,style="red.Horizontal.TProgressbar")
progress.place(x=0, y=387)
def top():
    query ="select * from Login;"
    cur.execute(query)
    l=[]
    for i in cur.fetchall():
        l.append(i[1:])
    # print(l)
    query ="select * from `Login Summary`;"
    cur.execute(query)
    j=[]
    for i in cur.fetchall():
        j.append(i)
    # print(j)
    mtch=False
    for i in j:
        for k in l:
            if i[0] == k[0] and i[1]==k[1]:
                mtch=True
    if mtch:
        root.destroy()
        os.system("python Main_Application.py")
    else:
        root.destroy()
        os.system("python Login.py")
i = 0
def load():
    global i
    if i <= 100:
        # txt = '' + (str(i)+'%')
        # progress_label.config(text=txt)
        progress['value'] = i
        i += 1
        progress_label.after (50, load)
    else:
        top()
load()
root.mainloop()
