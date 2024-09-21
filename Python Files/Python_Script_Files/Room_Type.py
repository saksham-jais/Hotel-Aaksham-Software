try:
    import tkinter
    import customtkinter
    from tkinter import ttk
    from tkinter import *
    from tkinter import messagebox
    from PIL import ImageTk, Image
    from tkcalendar import DateEntry
    from datetime import date
    import pandas as pd
    import mysql.connector as connector
    import os

    height = 600
    width = 1000

    root = Tk()
    root.maxsize("600", "260")
    root.minsize("600", "260")
    root.geometry('{}x{}+{}+{}'.format(600, 260, 600, 250))
    root.title("Room Status")
    con = connector.connect(host='localhost',
                            port='3306',
                            user='root',
                            password='Password',
                            database='Hotel Management Software')
    cur = con.cursor()
    Gs = pd.read_csv("./CSV_FILE/RM_Status.csv", index_col=[0])
    frame = customtkinter.CTkFrame(master=root, bg_color="black")
    frame.pack(fill=BOTH, expand=1)

    Guest_Entry = ImageTk.PhotoImage(Image.open("./images/Guest_Entry.png").resize((30, 30)))

    customtkinter.CTkLabel(master=frame, text="Room Status", font=('Times New Roman', 30, "bold")).place(x=200, y=10)


    def reset():
        RmStatus.set(Gs.RoomStatus[3])


    tkinter.Button(frame, image=Guest_Entry, compound=LEFT, fg="Black", width=120, activeforeground="black",
                   activebackground="#a8701d", height=30, text="Reset", command=reset, bg="#a8701d", anchor=W,
                   font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=450, y=52)


    def Cng():
        con = connector.connect(host='localhost',
                                port='3306',
                                user='root',
                                password='Password',
                                database='Hotel Management Software')
        cur = con.cursor()
        query = f"update `Room Status` set `Status`= '{RmStatus.get()}' where `Room No.` ='{RmNo.get()}';"
        cur.execute(query)
        con.commit()
        root.destroy()


    tkinter.Button(frame, image=Guest_Entry, compound=LEFT, command=Cng, fg="Black", width=120,
                   activeforeground="black", activebackground="#a8701d", height=30, text="Change", bg="#a8701d",
                   anchor=W, font=('Century Gothic', 15, "bold"), borderwidth=5, cursor="hand2").place(x=450, y=52 + 52)


    def cls():
        root.destroy()


    tkinter.Button(frame, image=Guest_Entry, compound=LEFT, command=cls, fg="Black", width=120,
                   activeforeground="black", activebackground="#a8701d", height=30, text="Close", bg="#a8701d",
                   anchor=W, font=('Century Gothic', 17, "bold"), borderwidth=5, cursor="hand2").place(x=450,
                                                                                                       y=52 + 52 + 52)


    def idd():
        customtkinter.CTkLabel(master=frame, text="Room No :", font=('Century Gothic', 16)).place(x=20, y=60)
        customtkinter.CTkLabel(master=frame, text="Room Type :", font=('Century Gothic', 16)).place(x=20, y=105 + 10)
        customtkinter.CTkLabel(master=frame, text="Status :", font=('Century Gothic', 16)).place(x=20, y=150 + 10 + 5)


    idd()
    RmNo = StringVar()
    RmTyp = StringVar()
    RmStatus = StringVar()
    RmNo.set(Gs.RoomStatus[1])
    RmTyp.set(Gs.RoomStatus[2])
    RmStatus.set(Gs.RoomStatus[3])
    Entry(frame, highlightthickness=2, textvariable=RmNo, highlightbackground="grey", highlightcolor="black", fg="blue",
          font="consolas 17 italic", state="readonly").place(x=200, y=60, width=80, height=30)
    Entry(frame, highlightthickness=2, textvariable=RmTyp, highlightbackground="grey", highlightcolor="black",
          fg="blue", font="consolas 17 italic", state="readonly").place(x=200, y=105 + 10, width=200, height=30)
    Entry(frame, highlightthickness=2, textvariable=RmStatus, highlightbackground="grey", highlightcolor="black",
          fg="blue", font="consolas 17 italic").place(x=200, y=150 + 15, width=200, height=30)
    root.mainloop()
except Exception as e:
    messagebox.showerror("Error",e)