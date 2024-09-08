import tkinter
import customtkinter
from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk,Image
import os
import random
import mysql.connector as connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import warnings
warnings.filterwarnings('ignore')
customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
# creating cutstom tkinter window
height = 500
width = 930
x = (app.winfo_screenwidth()//2)-(width//2)
y = (app.winfo_screenheight()//2)-(height//2)
app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
app.title('Login')

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='Wings',
                        database='Login')
cur = con.cursor()

def button_function():
    if entry1.get()=="" or entry2.get()=="":
        messagebox.showerror("Error",f"Filed Complete All The Blanks ")
    else:
        con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Wings',
                                database='Login')
        cur = con.cursor()
        cur.execute("select * from Login;")
        l = cur.fetchall()
        r=False
        for i in l:
            try:
                if entry1.get() != i[1]:
                    err="Username Is Not Same"
                if  entry2.get() != i[2]:
                    err="Password Is Not Same"
                if entry1.get() != i[1] and entry2.get() != i[2]:
                    err="User Not Found"
                if entry1.get() == i[1] and entry2.get() == i[2]:
                    r=True
            except Exception as e:
                messagebox.showerror("Error", f"{e}")
        if r:
            query = f"insert into `Login_Summary` values ('{entry1.get()}','{entry2.get()}');"
            try:
                cur.execute(query)
            except Exception as e:
                messagebox.showerror("Error",e)
            con.commit()
            con.close()
            app.destroy()
            os.system("python Main_Application.py")

        else:
            messagebox.showerror("Error", err)
def button_function1(_):
    if entry1.get()=="" or entry2.get()=="":
        messagebox.showerror("Error",f"Filed Complete All The Blanks ")
    else:
        con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Wings',
                                database='Login')
        cur = con.cursor()
        cur.execute("select * from Login;")
        l = cur.fetchall()
        r=False
        for i in l:
            try:
                if entry1.get() != i[1]:
                    err="Username Is Not Same"
                if  entry2.get() != i[2]:
                    err="Password Is Not Same"
                if entry1.get() != i[1] and entry2.get() != i[2]:
                    err="User Not Found"
                if entry1.get() == i[1] and entry2.get() == i[2]:
                    r=True
            except Exception as e:
                messagebox.showerror("Error", f"{e}")
        if r:
            query = f"insert into `Login_Summary` values ('{entry1.get()}','{entry2.get()}');"
            try:
                cur.execute(query)
            except Exception as e:
                messagebox.showerror("Error",e)
            con.commit()
            con.close()
            app.destroy()
            os.system("python Main_Application.py")

        else:
            messagebox.showerror("Error", err)
img1 = ImageTk.PhotoImage(Image.open("./assets/3.jpg"))
l1 = customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

# creating custom frame
# imgg = customtkinter.CTkImage(Image.open("").resize((20,20),Image.LANCZOS))
frame = customtkinter.CTkFrame(master=l1,width=650,height=380)
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

image = ImageTk.PhotoImage(Image.open("./assets/PhotoRoom-20231022_184533.png").resize((266,213),Image.LANCZOS) )
iim = customtkinter.CTkLabel(master=frame, image=image,text="")
iim.place(x=30, y=90)
l2 = customtkinter.CTkLabel(master=frame,text="Log into your Account",font=('Times New Roman',30,"bold"))
l2.place(x=300,y=45)
# customtkinter.CTkLabel(master=frame,text="User Name",font=('Century Gothic',18)).place(x=320, y=85)
def hide():
    openeye.configure(image=imgg3)
    entry2.configure(show="*")
    openeye.configure(command=show)
def show():
    openeye.configure(image=imgg2)
    entry2.configure(show="")
    openeye.configure(command=hide)
imgg1 = ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30)))
imgg2 = ImageTk.PhotoImage(Image.open("./images/openn.png").resize((30,30)))
imgg3 = ImageTk.PhotoImage(Image.open("./images/hide.png").resize((30,30)))
customtkinter.CTkLabel(master=frame, image=imgg1,text="").place(x=580, y=110)
openeye=customtkinter.CTkButton(master=frame,fg_color="#2b2b2b",image=imgg3,command=show,text="",width=20,height=25,hover=False)
openeye.place(x=570,y=165)
entry1 = customtkinter.CTkEntry(master=frame,placeholder_text_color="#dce4bb",font=('Century Gothic',18),width=250,height=30,placeholder_text='Username')

entry1.place(x=320,y=110)
entry1.configure(placeholder_text='Username')
# tkinter.Button(master=frame,image=img2,command=cc,activebackground="red").place(x=350,y=165)
entry2 = customtkinter.CTkEntry(master=frame,placeholder_text_color="#dce4bb",font=('Century Gothic',18),width=250,height=30,placeholder_text='Wings',show="*")
entry2.place(x=320,y=165)

dnt=customtkinter.CTkLabel(master=frame,text="Dont Have An Account ?",font=('Century Gothic',16))
dnt.place(x=320, y=310)
def ex():
    l1.configure(image=imgg)
    frame1.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
    l3.place(x=50,y=45-30)
tkinter.Button(master=frame,command=ex,text="Sign Up",fg="gold",activeforeground="gold",relief="flat",activebackground="#2b2b2b",bg="#2b2b2b",cursor="hand2",font=('Century Gothic',16)).place(x=650, y=385)
button1 = customtkinter.CTkButton(master=frame,font=('Times New Roman',20,"bold"),width=250,text="Login",command=button_function,corner_radius=6)
app.bind('<Return>',button_function1)
button1.place(x=320,y=260)



#------------------------   FORGET PASSWORD   ------------------------------------------------

frame2 = customtkinter.CTkFrame(master=l1,width=400,height=380)
# frame2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
def forgot():
    l1.configure(image=imgg)
    frame2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
def forget_command():
    if forget_user.get() == "" or forget_cnf_password.get() == "" or forget_new_password.get() == "":
        messagebox.showinfo("Fill","Fill All The Blanks")
        # print("User Not Enter Complete Details")
    else:
        con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Wings',
                                database='Login')
        cur = con.cursor()
        cur.execute("select * from Login;")
        l = cur.fetchall()
        r=False
        for i in l:
            try:
                if forget_user.get() == i[1]:
                    r=True
            except Exception as e:
                pass
                messagebox.showerror("Error", f"{e}")
        if r:
            if forget_new_password.get() != forget_cnf_password.get():
                messagebox.showerror("Error", f"New Password And Confirm Password Are Not Same")
            else:
                con = connector.connect(host='localhost',
                                        port='3306',
                                        user='root',
                                        password='Wings',
                                        database='Login')
                cur = con.cursor()
                forget_popup = messagebox.askyesno("confirm", "Are You Sure You Want To Change Password")
                # print(forget_popup)
                if forget_popup:
                    query = f"update Login set Password = '{forget_new_password.get()}' where UserName='{forget_user.get()}'"
                    try:
                        cur.execute(query)
                    except Exception as e:
                        messagebox.showerror("Error", e)
                    con.commit()
                    # con.close()
                    frame2.place(relx=5000, rely=5000)
                    forget_user.delete(0, END)
                    forget_new_password.delete(0, END)
                    forget_cnf_password.delete(0, END)
                else:
                    pass
        else:
            messagebox.showerror("Error", "User Not Found")

forget = customtkinter.CTkButton(master=frame,text="Forget password?",
                                 font=('Century Gothic',15),
                                 width=100,
                                 corner_radius=6,
                                 fg_color="#2b2b2b",
                                 # hover=False,
                                 command=forgot,hover_color="#3e3c3c")
forget.place(x=425,y=210)


customtkinter.CTkLabel(master=frame2, image=ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30))),text="").place(x=340, y=90)

def forget_ex():
    entry1.delete(0, END)
    entry2.delete(0, END)
    frame2.place(relx=5000, rely=5000)
tkinter.Button(master=frame2,command=forget_ex,text="Login",fg="gold",activeforeground="gold",relief="flat",activebackground="#2b2b2b",bg="#2b2b2b",cursor="hand2",font=('Century Gothic',16)).place(x=230+60, y=395)
def forget_hide():
    forget_eye.configure(image=imgg3)
    forget_new_password.configure(show="*")
    forget_cnf_password.configure(show="*")
    forget_eye.configure(command=forget_show)
def forget_show():
    forget_eye.configure(image=imgg2)
    forget_new_password.configure(show="")
    forget_cnf_password.configure(show="")
    forget_eye.configure(command=forget_hide)
forget_eye=customtkinter.CTkButton(master=frame2,fg_color="#2b2b2b",image=imgg3,command=forget_show,text="",width=20,height=25,hover=False)
forget_eye.place(x=333,y=140)


customtkinter.CTkLabel(master=frame2,text="Reset Password",font=('Times New Roman',30,"bold")).place(x=110,y=30)
forget_dnt=customtkinter.CTkLabel(master=frame2,text="Return Back",font=('Century Gothic',16))
forget_dnt.place(x=90+50, y=320)
forget_user = customtkinter.CTkEntry(master=frame2,font=('Century Gothic',18),width=230,height=30,placeholder_text='UserName')
forget_user.place(x=100,y=110-20)
forget_new_password = customtkinter.CTkEntry(master=frame2,font=('Century Gothic',18),width=230,height=30,placeholder_text='Wings',show="*")
forget_new_password.place(x=100,y=150+10-20)
forget_cnf_password = customtkinter.CTkEntry(master=frame2,font=('Century Gothic',18),width=230,height=30,placeholder_text='Confirm Password',show="*")
forget_cnf_password.place(x=100,y=210-20)
forget_button =customtkinter.CTkButton(master=frame2,font=('Times New Roman',25,"bold"),width=230,text="Submit",command=forget_command,corner_radius=6,height=30)
forget_button.place(x=100,y=270)
def forgotUserNm():
    l1.configure(image=imgg)
    frame3.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
customtkinter.CTkButton(master=frame2,text="Forget User Name?",
                                 font=('Century Gothic',15),
                                 width=100,
                                 corner_radius=6,
                                 fg_color="#2b2b2b",
                                 # hover=False,
                                 command=forgotUserNm,hover_color="#3e3c3c").place(x=180,y=230)
#--------------------------------------------------    Forget User Name      ------------------------------------------------------------------
frame3 = customtkinter.CTkFrame(master=l1,width=400,height=380)
# frame3.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
customtkinter.CTkLabel(master=frame3,text="Reset Username",font=('Times New Roman',30,"bold")).place(x=100,y=30)

customtkinter.CTkLabel(master=frame3, image=ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30))),text="").place(x=340, y=110)
customtkinter.CTkLabel(master=frame3, image=ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30))),text="").place(x=340, y=165)

UserNmentry = customtkinter.CTkEntry(master=frame3,font=('Century Gothic',18),width=230,height=30,placeholder_text='Email ID')
UserNmentry.place(x=90,y=110)
UserNmentry1 = customtkinter.CTkEntry(master=frame3,font=('Century Gothic',18),width=230,height=30,placeholder_text='OTP')
UserNmentry1.place(x=90,y=165)
OTP=random.randint(100000,999999)
def Sndotp():
    if UserNmentry.get()[-10:] != "@gmail.com":
        messagebox.showerror("Invalid","Invalid Mail Id")
    else:
        con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Wings',
                                database='Login')
        cur = con.cursor()
        # print(UserNmentry.get())
        query =f"select * from Login where `Email ID`='{UserNmentry.get()}'"
        cur.execute(query)
        Data=cur.fetchone()
        # print(Data)
        if Data == None:
            messagebox.showinfo("Reset Username", "No Username Found With This Email ID")
        else:
            messagebox.showinfo("Resetting Username", "An OTP Is Send To Given Mail ID")
            try:
                connect = smtplib.SMTP('smtp.gmail.com', 587)
                connect.ehlo()
                connect.starttls()
                sender_email = "sakshamjais100@gmail.com"
                sender_passwd = "aezk qvwe ltve hswh"
                connect.login(sender_email, sender_passwd)
                receiver_email = Data[0]
                subject = "Aaksham Hotel Verification Code"
                msg_text = (f"Your OTP For Reseting Username Is : - {OTP}")
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email
                message.attach(MIMEText(msg_text, "plain"))
                text = message.as_string()
                connect.sendmail(sender_email, receiver_email, text)
                # print("Successfully email📧 sent")
                messagebox.showinfo("Email Send","An Email Is Send To Your Mail ID")
            except Exception as e:
                messagebox.showerror("Error", e)
            finally:
                connect.quit()
customtkinter.CTkButton(master=frame3,text="Send OTP",
                                 font=('Century Gothic',15),
                                 width=100,
                                 corner_radius=6,
                                 fg_color="#2b2b2b",
                                 # hover=False,
                                 command= Sndotp,hover_color="#3e3c3c").place(x=230,y=210)
frame4 = customtkinter.CTkFrame(master=l1,width=400,height=380)

customtkinter.CTkLabel(master=frame3,text="Return Back",font=('Century Gothic',16)).place(x=90+40, y=300)
def forget_ex():
    entry1.delete(0, END)
    entry2.delete(0, END)
    frame2.place(relx=5000, rely=5000)
    frame3.place(relx=5000, rely=5000)
tkinter.Button(master=frame3,command=forget_ex,text="Login",fg="gold",activeforeground="gold",relief="flat",activebackground="#2b2b2b",bg="#2b2b2b",cursor="hand2",font=('Century Gothic',16)).place(x=230+50, y=370)
def ChgUsrNm():
    try:
        # print(OTP)
        # print(UserNmentry1.get())
        if int(UserNmentry1.get()) == OTP:
            if messagebox.askyesno("Change","Are YOu Sure You Want To Change"):
                l1.configure(image=imgg)
                frame4.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
        else:
            messagebox.showerror("Error","OTP Doest Not Match")
    except Exception as e :
        messagebox.showerror("Error","Please Input Details Firstly")
UserNmforget_button =customtkinter.CTkButton(master=frame3,font=('Times New Roman',25,"bold"),width=230,text="Submit",command=ChgUsrNm,corner_radius=6,height=30)
UserNmforget_button.place(x=90,y=250)

#------------------------------------------------------------------  Change USername   ---------------------------------------------------------------------------

frame4 = customtkinter.CTkFrame(master=l1,width=400,height=380)
# frame4.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=110)
customtkinter.CTkLabel(master=frame4, image=ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30))),text="").place(x=340, y=110)
customtkinter.CTkLabel(master=frame4, image=ImageTk.PhotoImage(Image.open("./images/user.png").resize((30,30))),text="").place(x=340, y=165)
CngUsrNmLbl = customtkinter.CTkLabel(master=frame4,text="Change Username",font=('Times New Roman',30,"bold"))
CngUsrNmLbl.place(x=90,y=30)
CngUsrNmEntry = customtkinter.CTkEntry(master=frame4,font=('Century Gothic',18),width=230,height=30,placeholder_text='New Username')
CngUsrNmEntry.place(x=90,y=110)
CngUsrNmEntry1 = customtkinter.CTkEntry(master=frame4,font=('Century Gothic',18),width=230,height=30,placeholder_text='Confirm Username')
CngUsrNmEntry1.place(x=90,y=165)
def ChgUsrNm():
    if CngUsrNmEntry.get()==CngUsrNmEntry1.get():
        if messagebox.askyesno("Change","Are You Sure YOu Want To Change Your USer Name"):
            con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Wings',
                                database='Login')
            cur = con.cursor()
            query=f"update login set UserName = '{CngUsrNmEntry.get()}' where `Email ID`='{UserNmentry.get()}'"
            print(query)
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Resetting Username","You UserName Is Changed")
            CngUsrNmEntry.delete(0,END)
            CngUsrNmEntry1.delete(0,END)
            frame2.place(relx=5000, rely=5000)
            frame3.place(relx=5000, rely=5000)
            frame4.place(relx=5000, rely=5000)
            UserNmentry1.delete(0, END)
            UserNmentry.delete(0, END)
    else:
        messagebox.showerror("Resetting Username","Username And Confirm Username are Not Same")
UserNmforget_button =customtkinter.CTkButton(master=frame4,font=('Times New Roman',25,"bold"),width=230,text="Change Username",command=ChgUsrNm,corner_radius=6,height=30)
UserNmforget_button.place(x=90,y=230)

#------------------------------------------------------------------   Sign Up   ----------------------------------------------------------------
imgg = ImageTk.PhotoImage(Image.open("./assets/7.jpg"))
frame1 = customtkinter.CTkFrame(master=l1,width=400,height=380)
l3 = customtkinter.CTkLabel(master=frame1,text="    Create An Account",font=('Times New Roman',30,"bold"))
emailimgg = ImageTk.PhotoImage(Image.open("./images/email.png").resize((33,33)))
def hidee():
    openeyee.configure(image=imgg3)
    passs.configure(show="*")
    cnfpass.configure(show="*")
    openeyee.configure(command=showw)
def showw():
    openeyee.configure(image=imgg2)
    passs.configure(show="")
    cnfpass.configure(show="")
    openeyee.configure(command=hidee)
openeyee=customtkinter.CTkButton(master=frame1,fg_color="#2b2b2b",image=imgg3,command=showw,text="",width=20,height=25,hover=False)
openeyee.place(x=333,y=180-30)
email = customtkinter.CTkEntry(master=frame1,font=('Century Gothic',18),width=230,height=30,placeholder_text='Email')
email.place(x=100,y=100-30)
# imgg1 = ImageTk.PhotoImage(Image.open("./images/user.png").resize((25,25)))
user = customtkinter.CTkEntry(master=frame1,font=('Century Gothic',18),width=230,height=30,placeholder_text='UserName')
user.place(x=100,y=140-30)
customtkinter.CTkLabel(master=frame1,image=imgg1,text="").place(x=340,y=140-30)
customtkinter.CTkLabel(master=frame1,image=emailimgg,text="").place(x=340,y=100-30)
passs = customtkinter.CTkEntry(master=frame1,font=('Century Gothic',18),width=230,height=30,placeholder_text='Wings',show="*")
passs.place(x=100,y=180-30)
cnfpass = customtkinter.CTkEntry(master=frame1,font=('Century Gothic',18),width=230,height=30,placeholder_text='Confirm Password',show="*")
cnfpass.place(x=100,y=220-30)
chk_terms=tkinter.StringVar(value=0)
chkbx=customtkinter.CTkCheckBox(master=frame1,font=('Century Gothic',16),text="I Agree To The Terms & Conditions",variable=chk_terms,onvalue=1,offvalue=0,checkbox_width=25,checkbox_height=25,corner_radius=25,fg_color="blue",border_color="white",hover=False,border_width=2)#checkmark_color="red"
chkbx.place(x=75,y=270-30)
def cmd():
    if email.get() == "" or user.get() == "" or passs.get() == "" or cnfpass.get() == "":
        messagebox.showinfo("Fill","Fill All The Blanks")
        # print("User Not Enter Complete Details")
    else:
        if passs.get() != cnfpass.get():
            messagebox.showerror("Error",f"Password And Confirm Password Are Not Same")
        else:
            if chkbx.get() == 0:
                # print(chkbx.get())
                messagebox.showinfo("Check","Check Our Terms And Conditions")
                # print("Check Box Not Checked")
            else:
                if messagebox.askyesno("SignUp","Are You Sure You Want To Sign Up "):
                    try:
                        connect = smtplib.SMTP('smtp.gmail.com', 587)
                        connect.ehlo()
                        connect.starttls()
                        sender_email = "sakshamjais100@gmail.com"
                        sender_passwd = "aezk qvwe ltve hswh"
                        connect.login(sender_email, sender_passwd)
                        receiver_email = email.get()
                        subject = "Aaksham Hotel Verification Details"
                        msg_text = (f"User ID :- {user.get()}\nPassword :- {passs.get()}\nNow You Are Registerd With us...\nThanks & Regards \n Hotel Aaksham")
                        message = MIMEMultipart()
                        message["From"] = sender_email
                        message["To"] = receiver_email
                        message["Subject"] = subject
                        message["Bcc"] = receiver_email
                        message.attach(MIMEText(msg_text, "plain"))
                        text = message.as_string()
                        connect.sendmail(sender_email, receiver_email, text)
                        messagebox.showinfo("Mail","A Mail Is Send To Your Mail ID")
                        query = f"insert into Login values('{email.get()}','{user.get()}','{passs.get()}');"
                        # print(query)
                        cur.execute(query)
                        con.commit()
                        # con.close()
                        frame1.place(relx=5000, rely=5000)
                        email.delete(0, END)
                        user.delete(0, END)
                        passs.delete(0, END)
                        cnfpass.delete(0, END)
                        chk_terms.set(value=0)
                    except Exception as e:
                        messagebox.showerror("Error", e)
                    finally:
                        connect.quit()

customtkinter.CTkButton(master=frame1,font=('Times New Roman',25,"bold"),width=230,text="Sign Up",command=cmd,corner_radius=6,height=30).place(x=100,y=310-30)

sign_UP_dnt=customtkinter.CTkLabel(master=frame1,text="I Have An Account",font=('Century Gothic',16))
sign_UP_dnt.place(x=90+20, y=320+10)
def sign_UP_ex():
    entry1.delete(0,END)
    entry2.delete(0,END)
    frame1.place(relx=5000, rely=5000)
tkinter.Button(master=frame1,command=sign_UP_ex,text="Login",fg="gold",activeforeground="gold",relief="flat",activebackground="#2b2b2b",bg="#2b2b2b",cursor="hand2",font=('Century Gothic',16)).place(x=340, y=410)

#--------------------------------------------------------------------------------------------------
# Create custom button

# You can easily integrate authentication system


app.mainloop()