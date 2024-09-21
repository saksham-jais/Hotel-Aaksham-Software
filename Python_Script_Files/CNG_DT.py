import tkinter
import customtkinter
from tkinter import  ttk
from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk,Image
from tkcalendar import DateEntry
from datetime import date
import pandas as pd
import mysql.connector as connector
import pygame
height = 600
width = 1000

root=Tk()
root.maxsize("1000","260")
root.minsize("1000","260")
root.geometry('{}x{}+{}+{}'.format(1000,260,300,300))
root.title("Change Check Out Date")
con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Password',
                      database='Hotel Management Software')
cur=con.cursor()
Data = pd.read_csv("./CSV_FILE/BillNo.csv", index_col=[0])
query = f"select * from `check in details` where `Room No`='{Data.BillNo[4]}';"
cur.execute(query)
DataLst=cur.fetchone()
print(DataLst)
frame = customtkinter.CTkFrame(master=root,bg_color="black")
frame.pack(fill=BOTH,expand=1)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))

customtkinter.CTkLabel(master=frame, text="Guest Information", font=('Times New Roman', 30, "bold")).place(x=10, y=10)
def reset():
    cal.set_date(date.today())
tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Reset",command=reset, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=300+100, y=52)
def Cng():
    from datetime import datetime
    chin_date = datetime.strptime(ChkinDt.get(), "%Y-%m-%d")
    past_date = datetime.strptime(cal.get_date().strftime("%Y-%m-%d"), "%Y-%m-%d")
    Nm_Dys=(past_date-chin_date).days
    if Nm_Dys == 0.0:
        Nm_Dys = 1
    if (past_date-chin_date).days >= 0:
        chgval=messagebox.askyesno("Change Check Out Date","Are You Sure You Want To Change Date")
        if chgval:
            # print(Nm_Dys)
            # print(DataLst[-1])
            query = f"UPDATE `Check In Details` SET `Day Out` = '{past_date.date()}',`Room Price` = '{Nm_Dys*DataLst[-1]}' WHERE (`Guest ID` = '{Data.BillNo[2]}');"
            cur.execute(query)
            # print(query)
            con.commit()
            con.close()
            root.destroy()
        else:
            pass
    else:
        messagebox.showinfo("Change Check Out Date","Checkout Date Must Greater Than Check In Date")
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Cng, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Change", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=400+150, y=52)
def cls():
    root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=500+200, y=52)
def idd():
    customtkinter.CTkLabel(master=frame,text="Guest Id :",font=('Century Gothic',16)).place(x=20, y=60)
    customtkinter.CTkLabel(master=frame,text="Guest Name :",font=('Century Gothic',16)).place(x=20, y=105)
    customtkinter.CTkLabel(master=frame,text="Old Check Out Date :",font=('Century Gothic',16)).place(x=20, y=150)

    customtkinter.CTkLabel(master=frame,text="Check In Date :",font=('Century Gothic',16)).place(x=450, y=105)
    customtkinter.CTkLabel(master=frame,text="New Check Out Date :",font=('Century Gothic',16)).place(x=450, y=150)

idd()
GsID=StringVar()
GsNm=StringVar()
Gsder=StringVar()
oldChkDt=StringVar()
ChkinDt=StringVar()
GsID.set(value=Data.BillNo[2])
GsNm.set(value=Data.BillNo[3])
oldChkDt.set(value=Data.BillNo[7])
ChkinDt.set(value=Data.BillNo[6])
Entry(frame,highlightthickness=2,textvariable=GsID,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=60,width=80,height=30)
Entry(frame,highlightthickness=2,textvariable=GsNm,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=105,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=oldChkDt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=150,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=ChkinDt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700, y=105,width=200,height=30)
# Entry(frame,highlightthickness=2,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700, y=150,width=200,height=30)
s = ttk.Style()
s.theme_use("xpnative")  # classic , alt,default , winnative , xpnative , clam , vista
s.configure(".", font=("consolas", 14, "italic"), foreground="blue")
s.configure("Treeview", foreground="black", background="light yellow", rowheight=25, fieldbackground="light yellow")
s.map("Treeview", background=[("selected", "blue")])
# s.configure("Treeview.Heading", font=("Cambria", 15, "italic"), foreground="red", background="light grey")
cal = DateEntry(frame, selectmode="day", font=("Cambria", 15, "italic"),date_pattern='dd/mm/yy',foreground="blue", width=16)
cal.place(x=700, y=150)
pygame.mixer.init()
pygame.mixer.music.load("./Voices/Change Check Out Date.mp3")
pygame.mixer.music.play()
root.mainloop()