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
import os
import pygame
height = 730
width = 1200
root=Tk()
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y-30))

Label(text="Guest Check In",background="brown",font=('Times New Roman',30,"bold")).pack(anchor=N,fill=X)
con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Password',
                      database='Hotel Management Software')
cur=con.cursor()
img1 = ImageTk.PhotoImage(Image.open("./assets/3.jpg"))
l1 = customtkinter.CTkLabel(master=root,text="",image=img1)
l1.pack(fill=BOTH,anchor=N)

frame = customtkinter.CTkFrame(master=l1,width=1000,height=650,bg_color="black")
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))

customtkinter.CTkLabel(master=frame, text="Guest Information", font=('Times New Roman', 30, "bold")).place(x=10, y=10)
customtkinter.CTkLabel(master=frame, text="Payment Information", font=('Times New Roman', 30, "bold")).place(x=500, y=10)
def Gstry():
    os.system("python ./Python_Script_Files/Gs_Entry.py")
    Gs = pd.read_csv("./CSV_FILE/GStDTL.csv", index_col=[0],keep_default_na=False)
    GsID.set(Gs.hii[1])
    GsNm.set(Gs.hii[2])
    Gsder.set(Gs.hii[3])
    Gsgion.set(Gs.hii[4])
    GsAddress.set(Gs.hii[5])
    GsCity.set(Gs.hii[6])
    GsCntry.set(Gs.hii[7])
    GsCntNO.set(Gs.hii[8])
    GsIDType.set(Gs.hii[9])
    GsIDNo.set(Gs.hii[10])
    GsEmailIDNO.set(Gs.hii[11])
    global CstmrImg
    CstmrImg = ImageTk.PhotoImage(Image.open(Gs.hii[12]).resize((100, 100)))
    Imglbl.configure(image=CstmrImg)
tkinter.Button(frame, image=Guest_Entry,compound=CENTER,command=Gstry, fg="Black", width=50, activeforeground="black",activebackground="#a8701d", height=30, bg="#a8701d", anchor=W, borderwidth=5, cursor="hand2").place(x=210, y=52)
CstmrImg = ImageTk.PhotoImage(Image.open("./assets/passportsizephoto.webp").resize((100, 100)))
Imglbl=Label(frame,image=CstmrImg)
Imglbl.place(x=365, y=110)
def reset():
    GsID.set("")
    GsNm.set("")
    Gsder.set("")
    Gsgion.set("")
    GsAddress.set("")
    GsCity.set("")
    GsCntry.set("")
    GsCntNO.set("")
    GsIDType.set("")
    GsIDNo.set("")
    GsEmailIDNO.set("")
    global CstmrImg
    CstmrImg = ImageTk.PhotoImage(Image.open("./assets/passportsizephoto.webp").resize((100, 100)))
    Imglbl.configure(image=CstmrImg)
tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Reset",command=reset, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=350, y=52)
def rr():
    Pymnt.set(0)
    mydata.set("Cash")
    cal.set_date(date.today())
    cal1.set_date(date.today())
    cal2.set_date(date.today())
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=rr, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Reset", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=50)
sn=1
# def Add():
#     global sn
#     if int(Pymnt.get())<=int(file.RoomDetails[3]):
#         table.insert("",END, values=(sn, mydata.get(), Pymnt.get(), cal.get_date().strftime("%d-%m-%Y")))
#         sn+=1
#     else:
#         print("Line Number 82  Import Message Box")
# tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Add",command=Add, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=100)
# def rm():
#     # print(table.selection())
#     try:
#         table.delete(table.selection())
#     except :
#         pass
# tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=rm, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Remove", bg="#a8701d", anchor=W,font=('Century Gothic', 16, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=160)
# def upp():
#     j=table.item(table.selection())['values']
#     print(j)
#     cal.set_date(j[3])
#     Pymnt.set(j[2])
#     mydata.set(j[1])
# tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=upp, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Update", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=220)
def CHk():
    if Pymnt.get() <= rm_price.get():
        if GsID.get() == "" or  GsNm.get() == "":
            err = messagebox.showerror("Fill Details", "Select The Customer")
            if err == "ok":
                pass
        else:
            Cnf = messagebox.askyesno("Check In", "Are You Sure You Want To Check In")
            if Cnf:
                con = connector.connect(host='localhost',
                                        port='3306',
                                        user='root',
                                        password='Password',
                                        database='Hotel Management Software')
                cur = con.cursor()
                c = cal1.get_date().strftime("%Y-%m-%d")
                c1 = cal2.get_date().strftime("%Y-%m-%d")
                c2 = cal.get_date().strftime("%Y-%m-%d")
                query = f"insert into `Check In Details` values ('{GsID.get()}','{GsNm.get()}','{Rm.get()}','{Rm_Type.get()}','{c}','{c1}','{rm_price.get()}','{Pymnt.get()}','{mydata.get()}','{c2}','Active','Direct','{Rm_Prc.get()}');"
                # try:
                cur.execute(query)
                con.commit()
                # print(query)
                # except Exception as e:
                #     print(e)
                query = f"Delete from `Room Status` where `Room No.`='{Rm.get()}';"
                cur.execute(query)
                con.commit()
                # print(query)
                query = f"Update `customer details` set `Status`='Active' where `Guest ID`='{GsID.get()}';"
                cur.execute(query)
                # print(query)
                con.commit()
                # GsID.set("")
                # GsNm.set("")
                # Gsder.set("")
                # Gsgion.set("")
                # GsAddress.set("")
                # GsCity.set("")
                # GsCntry.set("")
                # GsCntNO.set("")
                # GsIDType.set("")
                # GsIDNo.set("")
                # GsEmailIDNO.set("")
                messagebox.showinfo("Check In","You Are Check In")
                root.destroy()
    else :
        messagebox.showinfo("Check In Payment", "Advance Payment Must Be Smaller Than Or Equal To Total Payment")
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=CHk, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Check In", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=100)
def cls():
    if messagebox.askyesno("Close","Are You Sure You Want To Close"):
        root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=850, y=150)
def idd():
    customtkinter.CTkLabel(master=frame,text="Guest Id :",font=('Century Gothic',16)).place(x=20, y=60)
    customtkinter.CTkLabel(master=frame,text="Guest Name :",font=('Century Gothic',16)).place(x=20, y=105)
    customtkinter.CTkLabel(master=frame,text="Gender :",font=('Century Gothic',16)).place(x=20, y=150)
    customtkinter.CTkLabel(master=frame,text="Religion :",font=('Century Gothic',16)).place(x=20, y=195)
    customtkinter.CTkLabel(master=frame,text="Address :",font=('Century Gothic',16)).place(x=20, y=240)
    customtkinter.CTkLabel(master=frame,text="City :",font=('Century Gothic',16)).place(x=20, y=285)
    customtkinter.CTkLabel(master=frame,text="Country :",font=('Century Gothic',16)).place(x=20, y=330)
    customtkinter.CTkLabel(master=frame,text="Contact No :",font=('Century Gothic',16)).place(x=20, y=375)
    customtkinter.CTkLabel(master=frame,text="ID TYPE :",font=('Century Gothic',16)).place(x=20, y=420)
    customtkinter.CTkLabel(master=frame,text="ID NUMBER :",font=('Century Gothic',16)).place(x=20, y=465)
    customtkinter.CTkLabel(master=frame,text="Email ID :",font=('Century Gothic',16)).place(x=20, y=510)

    #--------------------------------------------------------------------------------------------------
    customtkinter.CTkLabel(master=frame, text="Room No :", font=('Century Gothic', 16)).place(x=510, y=60)
    customtkinter.CTkLabel(master=frame, text="Room Type :", font=('Century Gothic', 16)).place(x=510, y=110)
    customtkinter.CTkLabel(master=frame, text="Room Price :", font=('Century Gothic', 16)).place(x=510, y=160)
    customtkinter.CTkLabel(master=frame, text="Date In :", font=('Century Gothic', 16)).place(x=510, y=180+30)
    customtkinter.CTkLabel(master=frame, text="Date Out :", font=('Century Gothic', 16)).place(x=510, y=220+40)
    customtkinter.CTkLabel(master=frame, text="Number Of Days :", font=('Century Gothic', 16)).place(x=510, y=260+50)
    customtkinter.CTkLabel(master=frame, text="Total Amount :", font=('Century Gothic', 16)).place(x=510, y=300+60)
    customtkinter.CTkLabel(master=frame, text="Advance Payment :", font=('Century Gothic', 16)).place(x=510,y=340+70)
    customtkinter.CTkLabel(master=frame, text="Payment Mode :", font=('Century Gothic', 16)).place(x=510, y=380+80)
    customtkinter.CTkLabel(master=frame, text="Payment Date :", font=('Century Gothic', 16)).place(x=510, y=380+40+90)
idd()
GsID=StringVar()
GsNm=StringVar()
Gsder=StringVar()
Gsgion=StringVar()
GsAddress=StringVar()
GsCity=StringVar()
GsCntry=StringVar()
GsCntNO=StringVar()
GsIDType=StringVar()
GsIDNo=StringVar()
GsEmailIDNO=StringVar()
GsID.set("")
GsNm.set("")
Gsder.set("")
Gsgion.set("")
GsAddress.set("")
GsCity.set("")
GsCntry.set("")
GsCntNO.set("")
GsIDType.set("")
GsIDNo.set("")
GsEmailIDNO.set("")
Entry(frame,highlightthickness=2,textvariable=GsID,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=60,width=50,height=30)
Entry(frame,highlightthickness=2,textvariable=GsNm,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=105,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=Gsder,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=150,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=Gsgion,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=195,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsAddress,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=240,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsCity,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=285,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsCntry,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=330,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsCntNO,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=375,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsIDType,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=420,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsIDNo,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=465,width=200,height=30)
Entry(frame,highlightthickness=2,textvariable=GsEmailIDNO,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=140,y=510,width=200,height=30)

# file1 = open("readme.txt", "r")
file = pd.read_csv('./CSV_FILE/RMNO_RMPRICE.csv')
Rm=StringVar()
Rm.set(file.RoomDetails[1])
Rm_Type=StringVar()
Rm_Type.set(file.RoomDetails[2])
Rm_Prc=StringVar()
Rm_Prc.set(file.RoomDetails[3])
Days=StringVar()
rm_price=IntVar()
Pymnt=IntVar()
Entry(frame,textvariable=Rm,highlightthickness=2,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=690,y=60,width=80,height=30)
Entry(frame,textvariable=Rm_Type,highlightthickness=2,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 15 italic",state="disabled").place(x=690,y=60+40+10,width=135,height=30)
Entry(frame,textvariable=Rm_Prc,highlightthickness=2,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=690,y=100+40+20,width=80,height=30)
Entry(frame,highlightthickness=2,textvariable=Days,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=690,y=220+40+50,width=50,height=30)
Entry(frame,highlightthickness=2,state="disabled",textvariable=rm_price,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=690,y=260+40+60,width=135,height=30)
en=Entry(frame,highlightthickness=2,textvariable=Pymnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic")
en.place(x=690,y=300+40+70,width=135,height=30)
cal1 = DateEntry(frame,selectmode="day", font=("Cambria", 13, "italic"),foreground="blue", width=10+2)
cal1.place(x=690, y=140+40+30)
cal2 = DateEntry(frame, selectmode="day", font=("Cambria", 13, "italic"),foreground="blue", width=10+2)
cal2.place(x=690, y=180+40+40)
cal = DateEntry(frame, selectmode="day", font=("Cambria", 13, "italic"),foreground="blue", width=10+2)
cal.place(x=690, y=380+40+90)
def cal2_calevent_create(_):
    if (cal2.get_date() - cal1.get_date()).days >=0:
        Days.set((cal2.get_date() - cal1.get_date()).days)
        rm_price.set(value=int(file.RoomDetails[3])*(cal2.get_date()-cal1.get_date()).days)
        if rm_price.get() == 0:
            rm_price.set(int(file.RoomDetails[3]))
    else :
        messagebox.showinfo("Check Out Date", "Checkout Date Must Greater Than Check In Date")
    # print(int(file.RoomDetails[1])*(cal2.get_date()-cal1.get_date()).days)
cal2.bind("<<DateEntrySelected>>", cal2_calevent_create)
Days.set((cal2.get_date()-cal1.get_date()).days)
    #------------------------------------     SLIDER     ---------------------------------------------
# def sliderevent(value):
#     Person.set(value=int(value))
# customtkinter.CTkSlider(frame,from_=0,to=10,number_of_steps=10,width=80,command=sliderevent).place(x=750,y=220)
    #-------------------------------------------------------------------------------------------------
mydata = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=10, state='readonly',background="grey", height=10)
mydata["value"]=["Cash","UPI","Debit Card","Credit Card","Net Banking"]
# for j in range(1, 501):
#     l.append(f"API {j}")
#
# mydata["value"] = l
mydata.set("Cash")
mydata.place(x=690, y=340+40+80)
#---------------------------------------------------------------------------------------------------
# frm1 = Frame(frame, relief=SUNKEN, borderwidth=4)
# # frm1.place(x=500, y=420, width=480, height=200)
# scbr_x = Scrollbar(frm1, orient=HORIZONTAL)
# scbr_y = Scrollbar(frm1, orient=VERTICAL)
#
s = ttk.Style()
s.theme_use("winnative")  # classic , alt,default , winnative , xpnative , clam , vista
#
# #      FOR INSERT VALUES
#
s.configure(".", font=("consolas", 14, "italic"), foreground="blue")
#
# #     TO APPLY ON WHOLE TREEVIEW
#
s.configure("Treeview", foreground="black", background="light yellow", rowheight=25, fieldbackground="light yellow")
s.map("Treeview", background=[("selected", "blue")])
s.configure("Treeview.Heading", font=("Cambria", 15, "italic"), foreground="red", background="light grey")
#
# #     TO APPLY ON COLUMNS
# # s.configure("Treeview.Heading",font=("Cambria",17,"italic"),foreground="red",background="light grey")
# table = ttk.Treeview(frm1, cursor="hand2", columns=("SN_No.", "Payment_MD", "Payment", "Payment_Dt"),
#                          selectmode="browse", xscrollcommand=scbr_x.set, yscrollcommand=scbr_y.set)
#
# scbr_x.pack(side=BOTTOM, fill=X)
# scbr_y.pack(side=RIGHT, fill=Y)
# scbr_x.config(command=table.xview)
# scbr_y.config(command=table.yview)
# table.heading("SN_No.", text="Sn No.", anchor=CENTER)
# table.heading("Payment_MD", text="Payment Mode", anchor=CENTER)
# table.heading("Payment", text="Payment", anchor=CENTER)
# table.heading("Payment_Dt", text="Payment Date", anchor=CENTER)
# table.pack(fill=BOTH, expand=1)
#
#
# table["show"] = "headings"
# table.column("SN_No.", width=90, anchor=CENTER, minwidth=50)
# table.column("Payment_MD", width=170, anchor=CENTER, minwidth=150)
# table.column("Payment", width=100, anchor=CENTER, minwidth=70)
# table.column("Payment_Dt", width=140, anchor=CENTER, minwidth=120)
pygame.mixer.init()
pygame.mixer.music.load("./Voices/Check In.mp3")
pygame.mixer.music.play()
root.mainloop()