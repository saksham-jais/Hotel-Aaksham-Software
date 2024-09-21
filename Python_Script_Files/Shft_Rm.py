import tkinter
import customtkinter
from tkinter import  ttk
from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk,Image
import mysql.connector as connector
import pygame
import pandas as pd
height = 600
width = 1000

root=Tk()
root.maxsize("1000","300")
root.minsize("1000","300")
root.geometry('{}x{}+{}+{}'.format(1000,300,300,300))
root.title("Shift Room")
frame = customtkinter.CTkFrame(master=root,bg_color="black")
frame.pack(fill=BOTH,expand=1)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))

customtkinter.CTkLabel(master=frame, text="Guest Information", font=('Times New Roman', 30, "bold")).place(x=10, y=10)
# def Gstry():
#     # GsID.set("")
#     # GsNm.set("")
#     # Gsder.set("")
#     # Gsgion.set("")
#     # GsAddress.set("")
#     # GsCity.set("")
#     # GsCntry.set("")
#     # GsCntNO.set("")
#     # GsIDType.set("")
#     # GsIDNo.set("")
#     os.system("python Gs_Entry.py")
#     Gs = pd.read_csv("hi.csv", index_col=[0])
#     GsID.set(Data.hii[1])
#     GsNm.set(Data.hii[2])
#     Gsder.set(Data.hii[3])
#     Gsgion.set(Data.hii[4])
#     GsAddress.set(Data.hii[5])
#     GsCity.set(Data.hii[6])
#     GsCntry.set(Data.hii[7])
#     GsCntNO.set(Data.hii[8])
#     GsIDType.set(Data.hii[9])
#     GsIDNo.set(Data.hii[10])
#     # os.close("Main_Box.py")
#     # print(5656565655555555555555555555555)
def reset():
    mydata.set("")
    NwRmType.set("")
tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Reset",command=reset, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=300+100, y=52)
def CHk():
    if mydata.get() == "":
        messagebox.showerror("Shift Room","Select The Room")
    else:
        Cnf=messagebox.askyesno("Change Room","Are You Sure You Want To Change")
        if Cnf:
            query = f"select `Room Price` from `Check In Details` where `Room No`='{OldRmNo.get()}';"
            cur.execute(query)
            # print(query)
            query = f"insert into `room status` values ('{OldRmNo.get()}','{RmType.get()}','Dirty','{cur.fetchone()[0]}');"
            cur.execute(query)
            # print(query)
            con.commit()
            query = f"delete from `Room Status` where `Room No.`= '{mydata.get()}';"
            cur.execute(query)
            con.commit()
            # prc = 0
            # for i in dict:
            #     if i == mydata.get():
            #         prc = dict[i][1]
            query = (
                f"UPDATE `Check In Details` SET `Room No` = '{mydata.get()}',`Room Type`='{NwRmType.get()}',`Room Original Price`='{DataLst[-1]}'"
                f"WHERE (`Guest ID` = '{Data.BillNo[2]}');")
            cur.execute(query)
            # print(query)
            con.commit()
            con.close()
            root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=CHk, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Shift", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=400+150, y=52)
def cls():
    root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=500+200, y=52)
def idd():
    customtkinter.CTkLabel(master=frame,text="Guest Id :",font=('Century Gothic',16)).place(x=20, y=60)
    customtkinter.CTkLabel(master=frame,text="Guest Name :",font=('Century Gothic',16)).place(x=20, y=105)
    customtkinter.CTkLabel(master=frame,text="Old Room Number :",font=('Century Gothic',16)).place(x=20, y=150)
    customtkinter.CTkLabel(master=frame,text="Room Type :",font=('Century Gothic',16)).place(x=20, y=195)
    customtkinter.CTkLabel(master=frame,text="Check In Date :",font=('Century Gothic',16)).place(x=450, y=105)
    customtkinter.CTkLabel(master=frame,text="New Room Number :",font=('Century Gothic',16)).place(x=450, y=150)
    customtkinter.CTkLabel(master=frame,text="New Room  Type :",font=('Century Gothic',16)).place(x=450, y=195)
idd()
GsID=StringVar()
GsNm=StringVar()
OldRmNo=StringVar()
RmType=StringVar()
ChkInDt=StringVar()
NwRmType=StringVar()

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

GsID.set(Data.BillNo[2])
GsNm.set(Data.BillNo[3])
OldRmNo.set(Data.BillNo[4])
RmType.set(Data.BillNo[5])
ChkInDt.set(Data.BillNo[7])
NwRmType.set("")

Entry(frame,highlightthickness=2,textvariable=GsID,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=60,width=50,height=30)
Entry(frame,highlightthickness=2,textvariable=GsNm,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=105,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=OldRmNo,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=150,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=RmType,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=195,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=ChkInDt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700, y=105,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=NwRmType,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700, y=195,width=200,height=30)
# Entry(frame,highlightthickness=2,textvariable=GsCntry,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700, y=195,width=200,height=30)
con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='Password',
                        database='Hotel Management Software')
cur = con.cursor()
query = "select `Room No.`,`room Type`,Price from `room status` where `status`='vacant';"
cur.execute(query)
l=[]
dict={}
for i in cur.fetchall():
    l.append(i[0])
    dict[i[0]]=[i[1],i[2]]
# print(dict)
mydata = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=10, state='readonly',background="grey", height=10)
mydata["value"]=l
def mydata_selected(_):
    for i in dict:
        if i == mydata.get():
            NwRmType.set(dict[i][0])
mydata.bind('<<ComboboxSelected>>',mydata_selected)
# for j in range(1, 501):
#     l.append(f"API {j}")
#
# mydata["value"] = l
mydata.place(x=700, y=150)
# mydata1 = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=10, state='readonly',background="grey", height=10)
# mydata1["value"]=["Cash","UPI","Debit Card","Credit Card","Net Banking"]
# l = []
# for j in range(1, 501):
#     l.append(f"API {j}")
#
# mydata["value"] = l
# mydata1.set("Cash")
# mydata1.place(x=700, y=195)
pygame.mixer.init()
pygame.mixer.music.load("./Voices/Shift Room.mp3")
pygame.mixer.music.play()
root.mainloop()