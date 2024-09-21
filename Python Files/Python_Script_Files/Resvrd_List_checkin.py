import tkinter
import customtkinter
from tkinter import  ttk
from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk,Image
import pandas as pd
import mysql.connector as connector
from tkcalendar import DateEntry
from datetime import date
import os
height = 730
width = 1200
root=Tk()
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y-30))
con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Password',
                      database='Hotel Management Software')
cur=con.cursor()
Label(text="List Of Reservatives",background="brown",font=('Times New Roman',30,"bold")).pack(anchor=N,fill=X)

img1 = ImageTk.PhotoImage(Image.open("./assets/3.jpg"))
l1 = customtkinter.CTkLabel(master=root,text="",image=img1)
l1.pack(fill=BOTH,anchor=N)

frame = customtkinter.CTkFrame(master=l1,width=1000,height=550,bg_color="black")
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))

customtkinter.CTkLabel(master=frame, text="Search By Guest ID :", font=('Century Gothic', 16)).place(x=20, y=30)
customtkinter.CTkLabel(master=frame, text="Search By Guest Name :", font=('Century Gothic', 16)).place(x=20, y=80)
customtkinter.CTkLabel(master=frame, text="Search By Contact Number :", font=('Century Gothic', 16)).place(x=20, y=130)
E1Var=StringVar()
E1Var.set("")
E2Var=StringVar()
E2Var.set("")
E3Var=StringVar()
E3Var.set("")
E1=Entry(frame,highlightthickness=2,textvariable=E1Var,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic")
E1.place(x=280,y=30,width=200,height=30)
E2=Entry(frame,highlightthickness=2,textvariable=E2Var,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic")
E2.place(x=280,y=80,width=200,height=30)
E3=Entry(frame,highlightthickness=2,textvariable=E3Var,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic")
E3.place(x=280,y=130,width=200,height=30)
def Scrh():
    if E1.get()==""and E2.get()=="":
        for item in table.get_children():
            table.delete(item)
        query = "select * from `Reservation Details`  right join `customer details` using (`Guest ID`) where `Reservation Details`.`Room No` is not null and `Contact No.`='{E3.get()}';"
        cur.execute(query)
        sn = 1
        for row in cur.fetchall():
            table.insert("", END, values=(
            sn, row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[13], row[14],
            row[15], row[16], row[17], row[18]))
            sn += 1
    elif E2.get()==""and E3.get()=="":
        for item in table.get_children():
            table.delete(item)
        query = "select * from `Reservation Details`  right join `customer details` using (`Guest ID`) where `Reservation Details`.`Room No` is not null  and `Guest ID`='{E1.get()}';"
        cur.execute(query)
        sn = 1
        for row in cur.fetchall():
            table.insert("", END, values=(
            sn, row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[13], row[14],
            row[15], row[16], row[17], row[18]))
            sn += 1
    elif E1.get()==""and E3.get()=="":
        for item in table.get_children():
            table.delete(item)
        query = "select * from `Reservation Details`  right join `customer details` using (`Guest ID`) where `Reservation Details`.`Room No` is not null;"
        cur.execute(query)
        sn = 1
        for row in cur.fetchall():
            table.insert("", END, values=(
            sn, row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[13], row[14],
            row[15], row[16], row[17], row[18]))
            sn += 1
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Scrh, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Search", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=500+20, y=30)
def Rset():
    E1Var.set("")
    E2Var.set("")
    E3Var.set("")
    for item in table.get_children():
        table.delete(item)
    query = "select * from `Reservation Details`  right join `customer details` using (`Guest ID`) where `Reservation Details`.`Room No` is not null;"
    cur.execute(query)
    sn = 1
    for row in cur.fetchall():
        table.insert("", END, values=(
        sn, row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[13], row[14], row[15],
        row[16], row[17], row[18]))
        sn += 1
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Rset, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Reset", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=650+20, y=30)
# tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Excel", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=650, y=30)
def cls():
    fu = ["","","","","","","","","","","","","","","","",""]
    so = pd.Series(data=fu, name="hii")
    sep = pd.DataFrame(so)
    sep.to_csv("./CSV_FILE/GStDTL.csv")
    root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=800+20, y=30)

s = ttk.Style()
s.theme_use("winnative")  # classic , alt,default , winnative , xpnative , clam , vista

#      FOR INSERT VALUES

s.configure(".", font=("consolas", 14, "italic"), foreground="blue")

#     TO APPLY ON WHOLE TREEVIEW

s.configure("Treeview", foreground="black", background="light yellow", rowheight=25, fieldbackground="light yellow")
s.map("Treeview", background=[("selected", "blue")])
s.configure("Treeview.Heading", font=("Cambria", 15, "italic"), foreground="red", background="light grey")

frm1 = Frame(frame, relief=SUNKEN, borderwidth=4)
frm1.place(x=20, y=200, width=950, height=300)
scbr_x = Scrollbar(frm1, orient=HORIZONTAL)
scbr_y = Scrollbar(frm1, orient=VERTICAL)
#     TO APPLY ON COLUMNS
# s.configure("Treeview.Heading",font=("Cambria",17,"italic"),foreground="red",background="light grey")
table = ttk.Treeview(frm1, cursor="hand2", columns=("SN_No.", "Gs_ID", "Gs_Name", "Gender","Religion","Address","City","Country","Contact_No","ID_Type","ID_No","Room_No","Room_Type","Date_In","Date_Out","Room_Charges","Payment"),
                         selectmode="browse", xscrollcommand=scbr_x.set, yscrollcommand=scbr_y.set)

scbr_x.pack(side=BOTTOM, fill=X)
scbr_y.pack(side=RIGHT, fill=Y)
scbr_x.config(command=table.xview)
scbr_y.config(command=table.yview)
table.heading("SN_No.", text="Sn No.", anchor=CENTER)
table.heading("Gs_ID", text="Guest ID", anchor=CENTER)
table.heading("Gs_Name", text="Guest Name", anchor=CENTER)
table.heading("Gender", text="Gender", anchor=CENTER)
table.heading("Religion", text="Religion", anchor=CENTER)
table.heading("Address", text="Address", anchor=CENTER)
table.heading("City", text="City", anchor=CENTER)
table.heading("Country", text="Country", anchor=CENTER)
table.heading("Contact_No", text="Contact Number", anchor=CENTER)
table.heading("ID_Type", text="ID Type", anchor=CENTER)
table.heading("ID_No", text="ID No", anchor=CENTER)
table.heading("Room_No", text="Room No", anchor=CENTER)
table.heading("Room_Type", text="Room Type", anchor=CENTER)
table.heading("Date_In", text="Date In", anchor=CENTER)
table.heading("Date_Out", text="Date Out", anchor=CENTER)
table.heading("Room_Charges", text="Room Charges", anchor=CENTER)
table.heading("Payment", text="Payment", anchor=CENTER)
table.pack(fill=BOTH, expand=1)


table["show"] = "headings"
table.column("SN_No.", width=90, anchor=CENTER, minwidth=90)
table.column("Gs_ID", width=110, anchor=CENTER, minwidth=110)
table.column("Gs_Name", width=150, anchor=CENTER, minwidth=150)
table.column("Gender", width=130, anchor=CENTER, minwidth=130)
table.column("Religion", width=140, anchor=CENTER, minwidth=140)
table.column("Address", width=140, anchor=CENTER, minwidth=140)
table.column("City", width=140, anchor=CENTER, minwidth=140)
table.column("Country", width=140, anchor=CENTER, minwidth=140)
table.column("Contact_No", width=160, anchor=CENTER, minwidth=140)
table.column("ID_Type", width=140, anchor=CENTER, minwidth=120)
table.column("ID_No", width=140, anchor=CENTER, minwidth=120)
table.column("Room_No", width=140, anchor=CENTER, minwidth=120)
table.column("Room_Type", width=140, anchor=CENTER, minwidth=120)
table.column("Date_In", width=140, anchor=CENTER, minwidth=120)
table.column("Date_Out", width=140, anchor=CENTER, minwidth=120)
table.column("Room_Charges", width=140, anchor=CENTER, minwidth=120)
table.column("Payment", width=140, anchor=CENTER, minwidth=120)
query = "select * from `Reservation Details`  right join `customer details` using (`Guest ID`) where `Reservation Details`.`Room No` is not null;"
cur.execute(query)
sn=1
for row in cur.fetchall():
    table.insert("",END, values=(sn, row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],row[15], row[16], row[17], row[18], row[19], row[20]))
    sn+=1
# table.insert(parent="",index=0,values=(1,101,"Anjali","Female","Hinduism","Jodhpur","Rajasthan","Bharat","+919102020202","Passport",'1P85DF256'))
# table.insert(parent="",index=1,values=(2,102,"Mohan","Male","Hinduism","Lucknow","Uttar Pradesh","Bharat","+919105050505","Aadhar Card",'12121212121'))
# table.insert(parent="",index=2,values=(3,103,"Rakesh","Transgender","None","Kerala","Kerala","Bharat","+919103003302","Passport",'1P25RF56456'))
def table_select(_):
    fu=[]
    for i in table.selection():
        fu.append(table.item(i)['values'])
    so = pd.Series(data=fu[0], name="hii")
    sep = pd.DataFrame(so)
    sep.to_csv("./CSV_FILE/GStDTL.csv")
    # print(so)
    root.destroy()
table.bind('<<TreeviewSelect>>',table_select)

root.mainloop()