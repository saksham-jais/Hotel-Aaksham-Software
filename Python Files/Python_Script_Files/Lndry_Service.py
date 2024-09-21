import tkinter
import customtkinter
from tkinter import  ttk
from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk,Image
import pandas as pd
from tkcalendar import DateEntry
import mysql.connector as connector
from datetime import date
import os
import pygame
height =700
width = 1200
root=Tk()
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y-20))
Label(text="Laundry Service",background="brown",font=('Times New Roman',30,"bold")).pack(anchor=N,fill=X)
con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Password',
                      database='Hotel Management Software')
cur=con.cursor()
Data = pd.read_csv("./CSV_FILE/BillNo.csv", index_col=[0])
query = f"select chkindtl.`Guest ID`,chkindtl.`Guest Name`,cstmdtl.`Contact No.`,CONCAT (cstmdtl.Address, ', ', cstmdtl.City, ', ', cstmdtl.Country) as Address,cstmdtl.`Email ID`from `check in details`chkindtl  right join `customer details` cstmdtl using (`Guest ID`) where chkindtl.`Room No`='{Data.BillNo[4]}';"
cur.execute(query)
DataLst=cur.fetchone()
print(DataLst)
img1 = ImageTk.PhotoImage(Image.open("./assets/3.jpg"))
l1 = customtkinter.CTkLabel(master=root,text="",image=img1)
l1.pack(fill=BOTH,anchor=N)
frame = customtkinter.CTkFrame(master=l1,width=1090,height=560,bg_color="black")
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))
customtkinter.CTkLabel(master=frame, text="Bill Information", font=('Times New Roman', 20, "bold")).place(x=10, y=10)
customtkinter.CTkLabel(master=frame, text="Guest Details", font=('Times New Roman', 20, "bold")).place(x=500+20, y=10)
customtkinter.CTkLabel(master=frame, text="Laundry Service Details", font=('Times New Roman', 20, "bold")).place(x=10, y=170)
#-----------------------------------------------------------------------------------------------------------------------
customtkinter.CTkLabel(master=frame, text="Guest ID :", font=('Century Gothic', 16)).place(x=550, y=50)
customtkinter.CTkLabel(master=frame, text="Guest Name :", font=('Century Gothic', 16)).place(x=550, y=90)
customtkinter.CTkLabel(master=frame, text="Room Number :", font=('Century Gothic', 16)).place(x=550, y=130)
#-----------------------------------------------------------------------------------------------------------------------
customtkinter.CTkLabel(master=frame, text="Bill Number :", font=('Century Gothic', 16)).place(x=40, y=50)
customtkinter.CTkLabel(master=frame, text="Bill Date :", font=('Century Gothic', 16)).place(x=40, y=90)
customtkinter.CTkLabel(master=frame, text="Payment Mode :", font=('Century Gothic', 16)).place(x=40, y=130)
#-----------------------------------------------------------------------------------------------------------------------
# customtkinter.CTkLabel(master=frame, text="Bill Number :", font=('Century Gothic', 16)).place(x=40, y=50)
# customtkinter.CTkLabel(master=frame, text="Bill Date :", font=('Century Gothic', 16)).place(x=40, y=90)
# customtkinter.CTkLabel(master=frame, text="Payment Mode :", font=('Century Gothic', 16)).place(x=40, y=130)
# -----------------------------------------------------------------------------------------------------------------------
customtkinter.CTkLabel(master=frame, text="Service Name :", font=('Century Gothic', 16)).place(x=40, y=210)
customtkinter.CTkLabel(master=frame, text="Rate :", font=('Century Gothic', 16)).place(x=40, y=250)
customtkinter.CTkLabel(master=frame, text="Quantity :", font=('Century Gothic', 16)).place(x=40, y=290)
customtkinter.CTkLabel(master=frame, text="Amount :", font=('Century Gothic', 16)).place(x=40, y=330)
customtkinter.CTkLabel(master=frame, text="Discount :", font=('Century Gothic', 16)).place(x=40, y=370)
customtkinter.CTkLabel(master=frame, text="SGST :", font=('Century Gothic', 16)).place(x=40, y=410)
customtkinter.CTkLabel(master=frame, text="CGST :", font=('Century Gothic', 16)).place(x=40, y=450)
customtkinter.CTkLabel(master=frame, text="Total Amount :", font=('Century Gothic', 16)).place(x=40, y=490)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=280, y=410-40)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=280, y=450-40)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=280, y=490-40)
#-----------------------------------------------------------------------------------------------------------------------
Gs_ID=StringVar()
Gs_ID.set(Data.BillNo[2])
Entry(frame,highlightthickness=2,textvariable=Gs_ID,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=50,width=203,height=30)
Gs_Name=StringVar()
Gs_Name.set(Data.BillNo[3])
Entry(frame,highlightthickness=2,textvariable=Gs_Name,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=90,width=203,height=30)
Gs_RMNO=StringVar()
Gs_RMNO.set(Data.BillNo[4])
Entry(frame,highlightthickness=2,textvariable=Gs_RMNO,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=130,width=203,height=30)
#----------------------------------------------------------------------------------------------------------------------
Bill=StringVar()
Lndry_Data = pd.read_csv("./CSV_FILE/Lndry_BillNo.csv", index_col=[0])
Bill.set(str(Lndry_Data.LndryBill[0])+str(Lndry_Data.LndryBill[1]))
Entry(frame,highlightthickness=2,textvariable=Bill,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=50,width=203,height=30)
cal = DateEntry(frame, selectmode="day", font=("Cambria", 13, "italic"),foreground="blue", width=20)
cal.place(x=200, y=90)
#----------------------------------------------------------------------------------------------------------------------
mydata = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=20, state='readonly',background="grey", height=10)
mydata["value"]=["Cash","UPI","Debit Card","Credit Card","Net Banking"]
l = []
mydata.set("Cash")
mydata.place(x=200, y=130)
mydata1 = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=20, state='readonly',background="grey", height=10)
mydata1["value"]=["Dry Cleaning","Washing"]
mydata1.set("Washing")
mydata1.place(x=200, y=210)
def mydata1_selected(e):
    if mydata1.get()=="Dry Cleaning":
        # print("Dry Cleaning")
        Lndryrat.set("55")

    else:
        # print("Washing")
        Lndryrat.set("10")
mydata1.bind('<<ComboboxSelected>>',mydata1_selected)

#-------------------------------------------------------------------------------------------------------------------------
Lndryrat=StringVar()
Lndryrat.set("10")
Entry(frame,highlightthickness=2,textvariable=Lndryrat,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=290-40,width=203,height=30)
Lndryqnt=StringVar()
Entry(frame,highlightthickness=2,textvariable=Lndryqnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=330-40,width=60,height=30)
Lndryamt=DoubleVar()
Entry(frame,highlightthickness=2,highlightbackground="grey",textvariable=Lndryamt,highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=370-40,width=203,height=30)
Lndrydst=DoubleVar()
Lndrydst.set(2.0)
Entry(frame,highlightthickness=2,textvariable=Lndrydst,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=410-40,width=60,height=30)
Lndrys_GST=DoubleVar()
Lndrys_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Lndrys_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=450-40,width=60,height=30)
Lndryc_GST=StringVar()
Lndryc_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Lndryc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=490-40,width=60,height=30)
LndryTl_Amnt=DoubleVar()
Entry(frame,highlightthickness=2,textvariable=LndryTl_Amnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=530-40,width=203,height=30)
Lndrydstprice=DoubleVar()
Entry(frame,highlightthickness=2,textvariable=Lndrydstprice,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=410-40,width=93,height=30)
Lndryss_GST=DoubleVar()
Entry(frame,highlightthickness=2,textvariable=Lndryss_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=450-40,width=93,height=30)
Lndrycc_GST=DoubleVar()
Entry(frame,highlightthickness=2,textvariable=Lndrycc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=490-40,width=93,height=30)
#-----------------------------------------------------------------------------------------------------------------------
def Lndrysliderevent(value):
    Lndryqnt.set(value=int(value))
    try:
        Lndryamt.set(value=float(value * float(Lndryrat.get())))
        Lndrydstprice.set(value=float((value * float(Lndryrat.get()) * float(Lndrydst.get()) / 100)))
        Lndryss_GST.set(value=float((value * float(Lndryrat.get()) * float(Lndrys_GST.get()) / 100)))
        Lndrycc_GST.set(value=float((value * float(Lndryrat.get()) * float(Lndryc_GST.get()) / 100)))
        LndryTl_Amnt.set(value=str(float(Lndryamt.get()) - float(Lndrydstprice.get()) + float(Lndryss_GST.get()) + float(Lndrycc_GST.get())))
        LndryTl_Amnt.set(value="{:.2f}".format(LndryTl_Amnt.get()))
    except EXCEPTION as e:
        print(e)
    # print(value=int(value))
customtkinter.CTkSlider(frame,from_=0,to=10,command=Lndrysliderevent,number_of_steps=10,width=100).place(x=270,y=335-40)
#----------------------------------------------------------------------------------------------------------------------
snn=1
def LndryCart():
    global snn
    table.insert("",END, values=(
    snn, mydata1.get(), Lndryrat.get(), Lndryqnt.get(), Lndryamt.get(), Lndrydst.get(), Lndrys_GST.get(), Lndryc_GST.get(), "{:.2f}".format(LndryTl_Amnt.get())))
    snn += 1
    mydata1.set(value="Washing")
    Lndryrat.set(value=10)
    Lndryqnt.set(value=0)
    Lndryamt.set(value=0)
    Lndrydstprice.set(value=0)
    Lndryss_GST.set(value=0)
    Lndrycc_GST.set(value=0)
    LndryTl_Amnt.set(value=0)
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=LndryCart, fg="Black", width=110, activeforeground="black",activebackground="#a8701d", height=40, text="Add To\nCart", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=415, y=210)
def rset():
    mydata1.set(value="Washing")
    Lndryrat.set(value=10)
    Lndryqnt.set(value=0)
    Lndryamt.set(value=0)
    Lndrydstprice.set(value=0)
    Lndryss_GST.set(value=0)
    Lndrycc_GST.set(value=0)
    LndryTl_Amnt.set(value=0)
    global snn
    for rmv in table.get_children():
        table.delete(rmv)
    snn=1
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=rset, fg="Black", width=110, activeforeground="black",activebackground="#a8701d", height=30, text="Reset", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=415, y=270)
def Lndryrm():
    try:
        table.delete(table.selection())
    except:
        pass
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Lndryrm, fg="Black", width=110, activeforeground="black",activebackground="#a8701d", height=30, text="Remove", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=415, y=320)
#----------------------------------------------------------------------------------------------------------------------
# def New():
#     for item in table.get_children():
#         table.delete(item)
#     cal.set_date(date.today())
#     mydata.set(value="Cash")
#     mydata1.set(value="Washing")
#     Lndryrat.set(value=0)
#     Lndryqnt.set(value=0)
#     Lndryamt.set(value=0)
#     Lndrydstprice.set(value=0)
#     Lndryss_GST.set(value=0)
#     Lndrycc_GST.set(value=0)
#     LndryTl_Amnt.set(value=0)
# tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="New",command=New, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=40+20-15)
def Save_Print():
    if messagebox.askyesno("Laundry Bill","Are You Sure You Want To Bill Out"):
        Bdt = cal.get_date().strftime("%Y-%m-%d")
        query = f"INSERT INTO `Laundry Service Details` VALUES ('{Gs_ID.get()}', '{Gs_Name.get()}', '{Gs_RMNO.get()}', '{Bill.get()}', '{Bdt}','{mydata.get()}');"
        # print(query)
        cur.execute(query)
        con.commit()
        for i in table.get_children():
            l = table.item(i)["values"]
            query = f"INSERT INTO `Laundry Details` VALUES ('{Bill.get()}', '{l[1]}', '{l[2]}', '{l[3]}', '{l[4]}','{l[5]}', '{l[6]}', '{l[7]}', '{l[8]}','{date.today()}');"
            # print(query)
            cur.execute(query)
            con.commit()
        from docx2pdf import convert
        from docxtpl import DocxTemplate
        import smtplib
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        doc = DocxTemplate("./Invoice Template/Laundry Invoice Template.docx")
        invoice_list = []
        tl = 0
        for i in table.get_children():
            invoice_list.append(table.item(i)["values"])
            tl += float(table.item(i)["values"][8])
        # print(tl)
        # print(invoice_list)
        TtlAmnt=0
        for i in invoice_list:
            TtlAmnt+=float(i[8])
        Lndry_Data = pd.read_csv("./CSV_FILE/Lndry_BillNo.csv", index_col=[0])
        doc.render({"Bill_No": f"{Lndry_Data.LndryBill[0] + Lndry_Data.LndryBill[1]}",
                    "Date": f"{date.today().strftime('%d/%m/%Y')}",
                    "name": f"{Gs_Name.get()}",
                    "phone": DataLst[2],
                    "Address": DataLst[3],
                    "date": f'{date.today().strftime("%d/%b/%y")}',
                    "subtotal": f'{TtlAmnt}',
                    "invoice_list": invoice_list,
                    "salestax": f"{TtlAmnt*0.1}",
                    "total": f"{'{:.2f}'.format(tl+(tl*0.1))}"})
        doc.save("Laundry invoice.docx")
        convert(r"Laundry invoice.docx", r"./Invoices/Laundry_Service_Invoices/LaundryInvoice.pdf")
        os.remove(r"Laundry invoice.docx")
        os.rename(".\\Invoices\\Laundry_Service_Invoices\\LaundryInvoice.pdf",f".\\Invoices\\Laundry_Service_Invoices\\{Lndry_Data.LndryBill[0] + Lndry_Data.LndryBill[1]}.pdf")
        os.system(f".\\Invoices\\Laundry_Service_Invoices\\{Lndry_Data.LndryBill[0] + Lndry_Data.LndryBill[1]}.pdf")
        def Email():
            try:
                connect = smtplib.SMTP('smtp.gmail.com', 587)
                connect.ehlo()
                connect.starttls()
                sender_email = "sakshamjais100@gmail.com"
                sender_passwd = "aezk qvwe ltve hswh"
                connect.login(sender_email, sender_passwd)
                receiver_email = DataLst[-1]
                subject = "Laundry Service Bill"
                msg_text = "We Will Soon Pickup You Cloths....And Delivered Shortly"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email
                message.attach(MIMEText(msg_text, "plain"))
                filename = f".\\Invoices\\Laundry_Service_Invoices\\{Lndry_Data.LndryBill[0] + Lndry_Data.LndryBill[1]}.pdf"
                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {Lndry_Data.LndryBill[0] + Lndry_Data.LndryBill[1]}.pdf", )
                message.attach(part)
                text = message.as_string()
                connect.sendmail(sender_email, receiver_email, text)
                # print("Successfully email📧 sent")
                messagebox.showinfo("Mailed","Invoice Is Mailed To The Registered Mail ID")
            except Exception as e:
                print(e)
            finally:
                connect.quit()
        Email()
        Lndry_Data = pd.read_csv("./CSV_FILE/Lndry_BillNo.csv", index_col=[0])
        Lndry_Data.LndryBill[1] = int(Lndry_Data.LndryBill[1]) + 1
        Lndry_Data.to_csv("./CSV_FILE/Lndry_BillNo.csv")
        root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Save_Print, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=40, text="Save &\nPrint", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=90+20-15)
def cls():
    root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=90+20+50-5)

#-----------------------------------------------------------------------------------------------------------------------
frm1 = Frame(frame, relief=SUNKEN, borderwidth=4)
frm1.place(x=550, y=210, width=520, height=300)
scbr_x = Scrollbar(frm1, orient=HORIZONTAL)
scbr_y = Scrollbar(frm1, orient=VERTICAL)

s = ttk.Style()
s.theme_use("winnative")  # classic , alt,default , winnative , xpnative , clam , vista

#      FOR INSERT VALUES

s.configure(".", font=("consolas", 14, "italic"), foreground="blue")

#     TO APPLY ON WHOLE TREEVIEW

s.configure("Treeview", foreground="black", background="light yellow", rowheight=25, fieldbackground="light yellow")
s.map("Treeview", background=[("selected", "blue")])
s.configure("Treeview.Heading", font=("Cambria", 15, "italic"), foreground="red", background="light grey")

#     TO APPLY ON COLUMNS
# s.configure("Treeview.Heading",font=("Cambria",17,"italic"),foreground="red",background="light grey")
table = ttk.Treeview(frm1, cursor="hand2", columns=("SN_No.","Fd_Nm", "Rate", "Quantity", "Amount","Discount","S_GST","C_GST","Ttl_Amnt"),selectmode="browse", xscrollcommand=scbr_x.set, yscrollcommand=scbr_y.set)

scbr_x.pack(side=BOTTOM, fill=X)
scbr_y.pack(side=RIGHT, fill=Y)
scbr_x.config(command=table.xview)
scbr_y.config(command=table.yview)
table.heading("SN_No.", text="Sn No.", anchor=CENTER)
table.heading("Fd_Nm", text="Service Name", anchor=CENTER)
table.heading("Rate", text="Rate", anchor=CENTER)
table.heading("Quantity", text="Quantity", anchor=CENTER)
table.heading("Amount", text="Amount", anchor=CENTER)
table.heading("Discount", text="Discount", anchor=CENTER)
table.heading("S_GST", text="S GST", anchor=CENTER)
table.heading("C_GST", text="C GST", anchor=CENTER)
table.heading("Ttl_Amnt", text="Total Amount", anchor=CENTER)

table.pack(fill=BOTH, expand=1)
def table_selected(_):
    pass

table["show"] = "headings"
table.column("SN_No.", width=90, anchor=CENTER, minwidth=50)
table.column("Fd_Nm", width=170, anchor=CENTER, minwidth=150)
table.column("Rate", width=100, anchor=CENTER, minwidth=70)
table.column("Quantity", width=140, anchor=CENTER, minwidth=120)
table.column("Amount", width=140, anchor=CENTER, minwidth=120)
table.column("Discount", width=140, anchor=CENTER, minwidth=120)
table.column("S_GST", width=140, anchor=CENTER, minwidth=120)
table.column("C_GST", width=140, anchor=CENTER, minwidth=120)
table.column("Ttl_Amnt", width=140, anchor=CENTER, minwidth=120)
table.bind('<<TreeviewSelect>>',table_selected)
pygame.mixer.init()
pygame.mixer.music.load("./Voices/Laundry Services.mp3")
pygame.mixer.music.play()

root.mainloop()
