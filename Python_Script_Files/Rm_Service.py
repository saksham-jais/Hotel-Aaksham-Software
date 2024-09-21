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
height = 780
width = 1200
root=Tk()
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y-40))
Data = pd.read_csv("./CSV_FILE/BillNo.csv", index_col=[0])
Label(text="Room Service",background="brown",font=('Times New Roman',30,"bold")).pack(anchor=N,fill=X)
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
# print(DataLst)
img1 = ImageTk.PhotoImage(Image.open("./assets/3.jpg"))
l1 = customtkinter.CTkLabel(master=root,text="",image=img1)
l1.pack(fill=BOTH,anchor=N)
frame = customtkinter.CTkFrame(master=l1,width=1090,height=700,bg_color="black")
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30,30)))
customtkinter.CTkLabel(master=frame, text="Bill Information", font=('Times New Roman', 20, "bold")).place(x=10, y=10)
customtkinter.CTkLabel(master=frame, text="Guest Details", font=('Times New Roman', 20, "bold")).place(x=500+20, y=10)
customtkinter.CTkLabel(master=frame, text="Food Details", font=('Times New Roman', 20, "bold")).place(x=10, y=170)
customtkinter.CTkLabel(master=frame, text="Liquor Details", font=('Times New Roman', 20, "bold")).place(x=500+20, y=170)
#----------------------------------------------------------------------------------------------------------------------
customtkinter.CTkLabel(master=frame, text="Guest ID :", font=('Century Gothic', 16)).place(x=550, y=50)
customtkinter.CTkLabel(master=frame, text="Guest Name :", font=('Century Gothic', 16)).place(x=550, y=90)
customtkinter.CTkLabel(master=frame, text="Room Number :", font=('Century Gothic', 16)).place(x=550, y=130)
#----------------------------------------------------------------------------------------------------------------------
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
customtkinter.CTkLabel(master=frame, text="Bill Number :", font=('Century Gothic', 16)).place(x=40, y=50)
customtkinter.CTkLabel(master=frame, text="Bill Date :", font=('Century Gothic', 16)).place(x=40, y=90)
customtkinter.CTkLabel(master=frame, text="Payment Mode :", font=('Century Gothic', 16)).place(x=40, y=130)
customtkinter.CTkLabel(master=frame, text="Food Name :", font=('Century Gothic', 16)).place(x=40, y=210)
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
#----------------------------------------------------------------------------------------------------------------------
Bill=StringVar()
Bill.set(str(Data.BillNo[0])+str(Data.BillNo[1]))
Entry(frame,highlightthickness=2,textvariable=Bill,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=50,width=203,height=30)
cal = DateEntry(frame, selectmode="day", font=("Cambria", 13, "italic"),foreground="blue", width=20)
cal.place(x=200, y=90)
#----------------------------------------------------------------------------------------------------------------------
mydata = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=20,background="grey", height=10)
mydata["value"]=["Cash","UPI","Debit Card","Credit Card","Net Banking"]
l = []
mydata.set("Cash")
mydata.place(x=200, y=130)
mydata1 = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=20,background="grey", height=10)
mydata1["value"]=["Bhel Puri","Aalo Tikki","Burger","Pizza","Italian","Chinese"]
mydata1.set("Chinese")
mydata1.place(x=200, y=210)
#----------------------------------------------------------------------------------------------------------------------
Foodrat=IntVar()
Entry(frame,highlightthickness=2,textvariable=Foodrat,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=290-40,width=203,height=30)
Foodqnt=IntVar()
Entry(frame,highlightthickness=2,textvariable=Foodqnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=330-40,width=60,height=30)
Foodamt=IntVar()
Entry(frame,highlightthickness=2,highlightbackground="grey",textvariable=Foodamt,highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=370-40,width=203,height=30)
Fooddst=IntVar()
Fooddst.set(2.0)
Entry(frame,highlightthickness=2,textvariable=Fooddst,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=410-40,width=60,height=30)
Foods_GST=IntVar()
Foods_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Foods_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=450-40,width=60,height=30)
Foodc_GST=IntVar()
Foodc_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Foodc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=200,y=490-40,width=60,height=30)
FoodTl_Amnt=IntVar()
Entry(frame,highlightthickness=2,textvariable=FoodTl_Amnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=200,y=530-40,width=203,height=30)
Fooddstprice=IntVar()
Entry(frame,highlightthickness=2,textvariable=Fooddstprice,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=410-40,width=93,height=30)
Foodss_GST=IntVar()
Entry(frame,highlightthickness=2,textvariable=Foodss_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=450-40,width=93,height=30)
Foodcc_GST=IntVar()
Entry(frame,highlightthickness=2,textvariable=Foodcc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=310,y=490-40,width=93,height=30)
#-----------------------------------------------------------------------------------------------------------------------
customtkinter.CTkLabel(master=frame, text="Liquor Name :", font=('Century Gothic', 16)).place(x=530+20, y=210)
customtkinter.CTkLabel(master=frame, text="Rate :", font=('Century Gothic', 16)).place(x=530+20, y=290-40)
customtkinter.CTkLabel(master=frame, text="Quantity :", font=('Century Gothic', 16)).place(x=530+20, y=330-40)
customtkinter.CTkLabel(master=frame, text="Amount :", font=('Century Gothic', 16)).place(x=530+20, y=370-40)
customtkinter.CTkLabel(master=frame, text="Discount :", font=('Century Gothic', 16)).place(x=530+20, y=410-40)
customtkinter.CTkLabel(master=frame, text="SGST :", font=('Century Gothic', 16)).place(x=530+20, y=450-40)
customtkinter.CTkLabel(master=frame, text="CGST :", font=('Century Gothic', 16)).place(x=530+20, y=490-40)
customtkinter.CTkLabel(master=frame, text="Total Amount :", font=('Century Gothic', 16)).place(x=530+20, y=530-40)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=780, y=410-40)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=780, y=450-40)
customtkinter.CTkLabel(master=frame, text="%", font=('Century Gothic', 16)).place(x=780, y=490-40)
#-----------------------------------------------------------------------------------------------------------------------
rat=IntVar()
Entry(frame,highlightthickness=2,textvariable=rat,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=700,y=290-40,width=203,height=30)
qnt=IntVar()
Entry(frame,highlightthickness=2,textvariable=qnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=330-40,width=60,height=30)
amt=IntVar()
Entry(frame,highlightthickness=2,highlightbackground="grey",textvariable=amt,highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=370-40,width=203,height=30)
dst=IntVar()
dst.set(2.0)
Entry(frame,highlightthickness=2,textvariable=Fooddst,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=700,y=410-40,width=60,height=30)
s_GST=IntVar()
s_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Foods_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=700,y=450-40,width=60,height=30)
c_GST=IntVar()
c_GST.set(3.0)
Entry(frame,highlightthickness=2,textvariable=Foodc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic").place(x=700,y=490-40,width=60,height=30)
Tl_Amnt=IntVar()
Entry(frame,highlightthickness=2,textvariable=Tl_Amnt,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=700,y=530-40,width=203,height=30)
dstprice=IntVar()
Entry(frame,highlightthickness=2,textvariable=dstprice,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=810,y=410-40,width=93,height=30)
ss_GST=IntVar()
Entry(frame,highlightthickness=2,textvariable=ss_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=810,y=450-40,width=93,height=30)
cc_GST=IntVar()
Entry(frame,highlightthickness=2,textvariable=cc_GST,highlightbackground="grey",highlightcolor="black",fg="blue",font="consolas 17 italic",state="disabled").place(x=810,y=490-40,width=93,height=30)
#----------------------------------------------------------------------------------------------------------------------
mydata2 = ttk.Combobox(frame, foreground="black", justify=LEFT, font="Calibri 13", width=20,background="grey", height=10)
mydata2["value"]=["Jinro Soju","McDowell’s No.1 Whisky","Royal Stag Whisky","Royal Challenge","Smirnoff","Tuborg Brewery","Johnnie Walker"]
mydata2.set("Royal Challenge")
mydata2.place(x=700, y=210)
#----------------------------------------------------------------------------------------------------------------------
def Liquorsliderevent(value):
    qnt.set(value=int(value))
    try:
        amt.set(value=int(value * rat.get()))
        dstprice.set(value=int((value*rat.get()*dst.get())/100))
        ss_GST.set(value=int((value*rat.get()*s_GST.get())/100))
        cc_GST.set(value=int((value*rat.get()*c_GST.get())/100))
        Tl_Amnt.set(value=str(rat.get()+dstprice.get()+ss_GST.get()+cc_GST.get()))
    except EXCEPTION as e:
        messagebox.showerror("Error","Error")
        # print(e)
    # print(value=int(value))
def Foodsliderevent(value):
    Foodqnt.set(value=int(value))
    try:
        Foodamt.set(value=int(value * Foodrat.get()))
        Fooddstprice.set(value=int((value * Foodrat.get() * Fooddst.get()) / 100))
        Foodss_GST.set(value=int((value * Foodrat.get() * Foods_GST.get()) / 100))
        Foodcc_GST.set(value=int((value * Foodrat.get() * Foodc_GST.get()) / 100))
        FoodTl_Amnt.set(value=str(Foodrat.get() + Fooddstprice.get() + Foodss_GST.get() + Foodcc_GST.get()))
    except EXCEPTION as e:
        messagebox.showerror("Error", "Error")
    # print(value=int(value))
customtkinter.CTkSlider(frame,from_=0,to=10,command=Liquorsliderevent,number_of_steps=10,width=100).place(x=770,y=335-40)
customtkinter.CTkSlider(frame,from_=0,to=10,command=Foodsliderevent,number_of_steps=10,width=100).place(x=270,y=335-40)
#----------------------------------------------------------------------------------------------------------------------
def New():
    for item in table.get_children():
        table.delete(item)
    for item in liqr.get_children():
        liqr.delete(item)
    cal.set_date(date.today())
    mydata2.set(value="Royal Challenge")
    mydata1.set(value="Bhel Puri")
    Foodrat.set(value=0)
    Foodqnt.set(value=0)
    Foodamt.set(value=0)
    Fooddstprice.set(value=0)
    Foodss_GST.set(value=0)
    Foodcc_GST.set(value=0)
    FoodTl_Amnt.set(value=0)
    rat.set(value=0)
    qnt.set(value=0)
    amt.set(value=0)
    dstprice.set(value=0)
    ss_GST.set(value=0)
    cc_GST.set(value=0)
    Tl_Amnt.set(value=0)
tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="New",command=New, bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=40+20-15)
def Save_Print():
    if messagebox.askyesno("Laundry Bill","Are You Sure You Want To Bill Out"):
        LstData = []
        Bdt = cal.get_date().strftime("%Y-%m-%d")
        query = f"INSERT INTO `Room Service Details` VALUES ('{Gs_ID.get()}', '{Gs_Name.get()}', '{Gs_RMNO.get()}', '{Bill.get()}', '{Bdt}','{mydata.get()}');"
        cur.execute(query)
        # print(query)
        con.commit()
        for i in table.get_children():
            l = table.item(i)["values"]
            LstData.append(l)
            # print(l)
            query = f"INSERT INTO `Food Details` VALUES ('{Bill.get()}', '{l[1]}', '{l[2]}', '{l[3]}', '{l[4]}','{l[5]}', '{l[6]}', '{l[7]}', '{l[8]}','{date.today()}');"
            cur.execute(query)
            # print(query)
            con.commit()
        for j in liqr.get_children():
            w = liqr.item(j)["values"]
            LstData.append(w)
            # print(w)
            query = f"INSERT INTO `Liquor Details` VALUES ('{Bill.get()}', '{w[1]}', '{w[2]}', '{w[3]}', '{w[4]}','{w[5]}','{w[6]}', '{w[7]}', '{w[8]}','{date.today()}');"
            cur.execute(query)
            con.commit()
            # print(query)
        Data = pd.read_csv("./CSV_FILE/BillNo.csv", index_col=[0])
        from docx2pdf import convert
        from docxtpl import DocxTemplate
        import smtplib
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        doc = DocxTemplate("./Invoice Template/Food_Invoice.docx")
        # invoice_list = []
        # tl = 0
        # for i in table.get_children():
        #     invoice_list.append(table.item(i)["values"])
        #     tl += float(table.item(i)["values"][8])
        # print(tl)
        # print(invoice_list)
        TtlAmnt=0
        for i in LstData:
            # print(i)
            TtlAmnt+=float(i[4])
        doc.render({"Bill_No": f"{Data.BillNo[0] + str(Data.BillNo[1])}",
                    "Date": f"{date.today().strftime('%d/%m/%Y')}",
                    "name": f"{Gs_Name.get()}",
                    "phone": DataLst[2],
                    "Address": DataLst[3],
                    "subtotal": f'{TtlAmnt}',
                    "invoice_list": LstData,
                    "S_gst": dst.get(),
                    "C_gst": s_GST.get(),
                    "D_gst": c_GST.get(),
                    "sgsttax": TtlAmnt*(s_GST.get()/100),
                    "cgsttax": TtlAmnt*(c_GST.get()/100),
                    "dsttax": TtlAmnt*(dst.get()/100),
                    "total": TtlAmnt+(TtlAmnt*(s_GST.get()/100)+TtlAmnt*(c_GST.get()/100)-TtlAmnt*(dst.get()/100))})
        doc.save("Food invoice.docx")
        convert(r"Food invoice.docx", r"./Invoices/Room_Service_Invoices/Room_Service.pdf")
        os.remove(r"Food invoice.docx")
        os.rename(".\\Invoices\\Room_Service_Invoices\\Room_Service.pdf",f".\\Invoices\\Room_Service_Invoices\\{Data.BillNo[0] + str(Data.BillNo[1])}.pdf")
        os.system(f".\\Invoices\\Room_Service_Invoices\\{Data.BillNo[0] + str(Data.BillNo[1])}.pdf")

        def Email():
            try:
                connect = smtplib.SMTP('smtp.gmail.com', 587)
                connect.ehlo()
                connect.starttls()
                sender_email = "sakshamjais100@gmail.com"
                sender_passwd = "aezk qvwe ltve hswh"
                connect.login(sender_email, sender_passwd)
                receiver_email = DataLst[-1]
                subject = "Room Services"
                msg_text = "Your Order Will Delivered Shortly"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email
                message.attach(MIMEText(msg_text, "plain"))
                filename = f".\\Invoices\\Room_Service_Invoices\\{Data.BillNo[0] + str(Data.BillNo[1])}.pdf"
                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {Data.BillNo[0] + str(Data.BillNo[1])}.pdf", )
                message.attach(part)
                text = message.as_string()
                connect.sendmail(sender_email, receiver_email, text)
                messagebox.showinfo("Email Send","An Invoce Is Send To Registered Mail")
            except Exception as e:
                # print(e)
                messagebox.showerror("Error",e)
            finally:
                connect.quit()
        Email()

        Data.BillNo[1] = int(Data.BillNo[1]) + 1
        Data.to_csv("./CSV_FILE/BillNo.csv")
        root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Save_Print, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=40, text="Save &\nPrint", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=90+20-15)
def cls():
    root.destroy()
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=cls, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Close", bg="#a8701d", anchor=W,font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=90+20+50-5)
sn=1
def LiquorCart():
    # (sn, mydata2.get(), rat.get(), qnt.get(), amt.get(), dstprice.get(), ss_GST.get(), cc_GST.get(), Tl_Amnt.get(),
    #  cal.get_date().strftime("%d-%m-%Y"), mydata.get()))
    global sn
    liqr.insert(parent="", index=0, values=(sn, mydata2.get(), rat.get(), qnt.get(),amt.get(),dst.get(),s_GST.get(),c_GST.get(),Tl_Amnt.get()))
    sn += 1
    mydata2.set(value="Royal Challenge")
    rat.set(value=0)
    qnt.set(value=0)
    amt.set(value=0)
    dstprice.set(value=0)
    ss_GST.set(value=0)
    cc_GST.set(value=0)
    Tl_Amnt.set(value=0)
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=LiquorCart, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=40, text="Add To\nCart", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=280-70)
def Liquorrm():
    try:
        liqr.delete(liqr.selection())
    except:
        pass
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Liquorrm, fg="Black", width=120, activeforeground="black",activebackground="#a8701d", height=30, text="Remove", bg="#a8701d", anchor=W,font=('Century Gothic', 16, "bold"), borderwidth=5, cursor="hand2").place(x=940, y=340-70)
snn=1
def FoodCart():
    global snn
    table.insert(parent="", index=0, values=(
    snn, mydata1.get(), Foodrat.get(), Foodqnt.get(), Foodamt.get(), Fooddst.get(),Foods_GST.get(), Foodc_GST.get(), FoodTl_Amnt.get()))
    snn += 1
    mydata1.set(value="Bhel Puri")
    Foodrat.set(value=0)
    Foodqnt.set(value=0)
    Foodamt.set(value=0)
    Fooddstprice.set(value=0)
    Foodss_GST.set(value=0)
    Foodcc_GST.set(value=0)
    FoodTl_Amnt.set(value=0)
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=FoodCart, fg="Black", width=110, activeforeground="black",activebackground="#a8701d", height=40, text="Add To\nCart", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=415, y=210)
def Foodrm():
    try:
        table.delete(table.selection())
    except:
        pass
tkinter.Button(frame, image=Guest_Entry, compound=LEFT,command=Foodrm, fg="Black", width=110, activeforeground="black",activebackground="#a8701d", height=30, text="Remove", bg="#a8701d", anchor=W,font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=415, y=270)
#----------------------------------------------------------------------------------------------------------------------
frm1 = Frame(frame, relief=SUNKEN, borderwidth=4)
frm1.place(x=40, y=530, width=490, height=150)
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
table.heading("Fd_Nm", text="Food Name", anchor=CENTER)
table.heading("Rate", text="Rate", anchor=CENTER)
table.heading("Quantity", text="Quantity", anchor=CENTER)
table.heading("Amount", text="Amount", anchor=CENTER)
table.heading("Discount", text="Discount", anchor=CENTER)
table.heading("S_GST", text="S GST", anchor=CENTER)
table.heading("C_GST", text="C GST", anchor=CENTER)
table.heading("Ttl_Amnt", text="Total Amount", anchor=CENTER)

table.pack(fill=BOTH, expand=1)


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

#----------------------------------------------------------------------------------------------------------------------
frm2 = Frame(frame, relief=SUNKEN, borderwidth=4)
frm2.place(x=550, y=530, width=490, height=150)
scbr_x = Scrollbar(frm2, orient=HORIZONTAL)
scbr_y = Scrollbar(frm2, orient=VERTICAL)
liqr = ttk.Treeview(frm2, cursor="hand2", columns=("SN_No.","Liqr_Nm", "Rate", "Quantity", "Amount","Discount","S_GST","C_GST","Ttl_Amnt"),selectmode="browse", xscrollcommand=scbr_x.set, yscrollcommand=scbr_y.set)

scbr_x.pack(side=BOTTOM, fill=X)
scbr_y.pack(side=RIGHT, fill=Y)
scbr_x.config(command=liqr.xview)
scbr_y.config(command=liqr.yview)
liqr.heading("SN_No.", text="Sn No.", anchor=CENTER)
liqr.heading("Liqr_Nm", text="Liquor Name", anchor=CENTER)
liqr.heading("Rate", text="Rate", anchor=CENTER)
liqr.heading("Quantity", text="Quantity", anchor=CENTER)
liqr.heading("Amount", text="Amount", anchor=CENTER)
liqr.heading("Discount", text="Discount", anchor=CENTER)
liqr.heading("S_GST", text="S GST", anchor=CENTER)
liqr.heading("C_GST", text="C GST", anchor=CENTER)
liqr.heading("Ttl_Amnt", text="Total Amount", anchor=CENTER)
liqr.pack(fill=BOTH, expand=1)


liqr["show"] = "headings"
liqr.column("SN_No.", width=90, anchor=CENTER, minwidth=50)
liqr.column("Liqr_Nm", width=200, anchor=CENTER, minwidth=150)
liqr.column("Rate", width=100, anchor=CENTER, minwidth=70)
liqr.column("Quantity", width=140, anchor=CENTER, minwidth=120)
liqr.column("Amount", width=140, anchor=CENTER, minwidth=120)
liqr.column("Discount", width=140, anchor=CENTER, minwidth=120)
liqr.column("S_GST", width=140, anchor=CENTER, minwidth=120)
liqr.column("C_GST", width=140, anchor=CENTER, minwidth=120)
liqr.column("Ttl_Amnt", width=140, anchor=CENTER, minwidth=120)
#----------------------------------------------------------------------------------------------------------------------
pygame.mixer.init()
pygame.mixer.music.load("./Voices/Room Services.mp3")
pygame.mixer.music.play()

root.mainloop()