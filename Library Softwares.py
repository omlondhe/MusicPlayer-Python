import datetime
import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo

# con = sqlite3.connect("library")
# con.execute("CREATE TABLE BOOKS(NAME VARCHAR(20) NOT NULL, ID VARCHAR(10) PRIMARY KEY, AUTHOR VARCHAR(20))")
# con.commit()
# con.execute('''CREATE TABLE ISSUE_BOOK(ID VARCHAR(10), ROLL NUMBER(6) PRIMARY KEY, ISSUE_DT DATE NOT NULL,
# STATUS VARCHAR(4), RET_DT DATE);''')
# con.commit()
# con.execute("CREATE TABLE STUD_INFO(NAME VARCHAR(10) NOT NULL, ROLL NUMBER(6) PRIMARY KEY, PH_NO NUMBER(13))")
# con.commit()


def click(event):
    but = event.widget.cget("text")
    if but == "1.":
        ret_dt = " "
        status = "No"
        con = sqlite3.connect("library")

        def submit():
            # print(str_var.get(), int_var.get(), dt, status, ret_dt)
            con.execute("INSERT INTO ISSUE_BOOK VALUES(?, ?, ?, ?, ?)", (str_var.get(), int_var.get(),
                                                                         datetime.date.today(), status, ret_dt))
            con.commit()
            con.close()

        def reset():
            str_var.set("Select Book ID")
            int_var.set("Select Enrollment no.")

        tl = Toplevel(root)
        tl.title("Issue Book")
        tl.geometry("500x300")
        cur = con.cursor()
        Label(tl, text="Issue Book", font="ariel 35 bold").place(x=3, y=0)

        str_var = StringVar()
        str_var.set("Select Book ID")
        bk_id = cur.execute("SELECT ID FROM BOOKS")
        lst1 = []
        for i in bk_id:
            j = i[0]
            lst1.append(j)
            print(j)
            bk_op = OptionMenu(tl, str_var, *lst1)
            bk_op.place(x=5, y=85)

        int_var = IntVar()
        int_var.set("Select Enrollment no.")
        roll = cur.execute("SELECT ROLL FROM STUD_INFO")
        lst2 = []
        for i in roll:
            j = i[0]
            lst2.append(j)
            roll_op = OptionMenu(tl, int_var, *lst2)
            roll_op.place(x=171, y=85)

        s_button = Button(tl, text="Submit", padx=10, pady=3, command=submit)
        s_button.place(x=11, y=201)
        r_button = Button(tl, text="Reset", padx=12, pady=3, command=reset)
        r_button.place(x=121, y=201)
        tl.mainloop()
    elif but == "2.":
        con = sqlite3.connect("library")

        def search(event1=None):
            print(event1)
            curs = con.cursor()
            stat = "Yes"
            curs.execute(f'''UPDATE ISSUE_BOOK SET STATUS = '{stat}', RET_DT = '{datetime.date.today()}' 
WHERE ROLL = {en_no.get()}''')
            con.commit()

        tl = Toplevel(root)
        tl.title("Return Book")
        tl.geometry("500x300")
        Label(tl, text="Return Book", font="ariel 35 bold").place(x=0, y=0)
        Label(tl, text="Enter Enrollment Number : ", font="lucida 15").place(x=3, y=95)
        en_no = Entry(tl, font="lucida 15")
        en_no.place(x=251, y=95)
        en_no.focus()
        en_no.bind("<Button-1>", search)
        s_but = Button(tl, text="Return", padx=10, pady=3, command=search)
        s_but.place(x=251, y=125)
        s_but.bind("<Button-1>", search)
    elif but == "3.":
        con = sqlite3.connect("library")
        cur = con.cursor()
        exe = cur.execute("SELECT ID , ROLL, ISSUE_DT FROM ISSUE_BOOK WHERE STATUS = 'No'")
        tl = Toplevel(root)
        tl.title("Not Returned Books")
        # x = 371, y = 151
        tl.geometry("500x300")
        Label(tl, text="Not Returned Books", font="ariel 35 bold").place(x=0, y=0)

        Label(tl, text="Book ID", font="lucida 15 bold").place(x=5, y=65)
        Label(tl, text="Enrollment no.", font="lucida 15 bold").place(x=105, y=65)
        Label(tl, text="Issue dt.", font="lucida 15 bold").place(x=255, y=65)

        y_var = 100
        for i in exe:
            x_var = 5
            book = Label(tl, text=i[0], font=('', 11, ''))
            book.place(x=x_var, y=y_var)
            x_var = x_var + 100
            bid = Label(tl, text=i[1], font=('', 11, ''))
            bid.place(x=x_var, y=y_var)
            x_var = x_var + 150
            author = Label(tl, text=i[2], font=('', 11, ''))
            author.place(x=x_var, y=y_var)
            y_var = y_var + 25
        tl.mainloop()
    elif but == "4.":
        con = sqlite3.connect("library")

        def per_his(e1=None):
            print(e1)
            c = con.cursor()
            e = c.execute(f"SELECT * FROM ISSUE_BOOK WHERE ROLL = {en_no.get()}")

            Label(tl, text="Book ID", font="lucida 15 bold").place(x=5, y=65)
            Label(tl, text="Enrollment no.", font="lucida 15 bold").place(x=105, y=65)
            Label(tl, text="Issue dt.", font="lucida 15 bold").place(x=255, y=65)
            Label(tl, text="Return Status", font="lucida 15 bold").place(x=355, y=65)
            Label(tl, text="Return dt.", font="lucida 15 bold").place(x=505, y=65)

            l_his.destroy()
            en_no.destroy()
            s_but.destroy()

            y1_var = 100
            for p in e:
                x1_var = 5
                book1 = Label(tl, text=p[0], font=('', 11, ''))
                book1.place(x=x1_var, y=y1_var)
                x1_var = x1_var + 100
                sid = Label(tl, text=p[1], font=('', 11, ''))
                sid.place(x=x1_var, y=y1_var)
                x1_var = x1_var + 150
                isd = Label(tl, text=p[2], font=('', 11, ''))
                isd.place(x=x1_var, y=y1_var)
                x1_var = x1_var + 100
                r_stat = Label(tl, text=p[3], font=('', 11, ''))
                r_stat.place(x=x1_var, y=y1_var)
                x1_var = x1_var + 150
                r_dt = Label(tl, text=p[4], font=('', 11, ''))
                r_dt.place(x=x1_var, y=y1_var)
                y1_var = y1_var + 25

        tl = Toplevel(root)
        tl.title("Personal History")
        tl.geometry("500x300")
        Label(tl, text="Personal History", font="ariel 35 bold").place(x=0, y=0)

        l_his = Label(tl, text="Enter Enrollment Number : ", font="lucida 15")
        l_his.place(x=3, y=95)
        en_no = Entry(tl, font="lucida 15")
        en_no.place(x=251, y=95)
        en_no.focus()
        en_no.bind("<Button-1>", per_his)
        s_but = Button(tl, text="Access History", padx=10, pady=3, command=per_his)
        s_but.place(x=371, y=151)
        s_but.bind("<Button-1>", per_his)

        tl.mainloop()
    elif but == "5.":
        def add_book():
            cons = sqlite3.connect("library")
            cons.execute("INSERT INTO BOOKS VALUES(?, ?, ?)", (n_e.get().replace(" ", "_"),
                                                               bid_e.get().replace(" ", "_"),
                                                               a_e.get().replace(" ", "_")))
            cons.commit()
            cons.close()
            showinfo("Add a Book", "Book added                                       ")

        tl = Toplevel(root)
        tl.title("Add a Student")
        tl.geometry("500x300")
        Label(tl, text="Add a Book", font="ariel 35 bold").place(x=0, y=0)
        n_lbl = Label(tl, text="Enter Book Name    : ", font="lucida 15")
        n_lbl.place(x=3, y=70)
        n_e = Entry(tl, font="lucida 15")
        n_e.place(x=250, y=70)
        bid_lbl = Label(tl, text="Enter Book no.     : ", font="lucida 15")
        bid_lbl.place(x=3, y=110)
        bid_e = Entry(tl, font="lucida 15")
        bid_e.place(x=250, y=110)
        a_lbl = Label(tl, text="Enter Author Name  : ", font="lucida 15")
        a_lbl.place(x=3, y=150)
        a_e = Entry(tl, font="lucida 15")
        a_e.place(x=250, y=150)
        add_bk = Button(tl, text="Submit", padx=10, pady=5, command=add_book)
        add_bk.place(x=3, y=200)
        tl.mainloop()

    elif but == "6.":
        def add_stud():
            co = sqlite3.connect("library")
            co.execute("INSERT INTO STUD_INFO VALUES(?, ?, ?)", (n_e.get().replace(" ", "_"), r_e.get(), m_e.get()))
            co.commit()
            co.close()
            showinfo("Add a Student", "Student added")

        tl = Toplevel(root)
        tl.title("Add a Student")
        tl.geometry("500x300")
        Label(tl, text="Add a Student", font="ariel 35 bold").place(x=0, y=0)
        n_lbl = Label(tl, text="Enter Student Name   : ", font="lucida 15")
        n_lbl.place(x=3, y=70)
        n_e = Entry(tl, font="lucida 15")
        n_e.place(x=250, y=70)
        r_lbl = Label(tl, text="Enter Enrollment no. : ", font="lucida 15")
        r_lbl.place(x=3, y=110)
        r_e = Entry(tl, font="lucida 15")
        r_e.place(x=250, y=110)
        m_lbl = Label(tl, text="Enter Mobile Number  : ", font="lucida 15")
        m_lbl.place(x=3, y=150)
        m_e = Entry(tl, font="lucida 15")
        m_e.place(x=250, y=150)
        add_std = Button(tl, text="Submit", padx=10, pady=5, command=add_stud)
        add_std.place(x=3, y=200)
        tl.mainloop()
    elif but == "7.":
        con = sqlite3.connect("library")
        cur = con.cursor()
        exe = cur.execute("SELECT * FROM BOOKS")
        tl = Toplevel(root)
        tl.title("All Books")
        tl.geometry("500x300")
        Label(tl, text="All Books", font="ariel 35").place(x=3, y=0)
        Label(tl, text="Book", font="lucida 15 bold").place(x=5, y=65)
        Label(tl, text="Book ID", font="lucida 15 bold").place(x=105, y=65)
        Label(tl, text="Books Author", font="lucida 15 bold").place(x=205, y=65)
        y_var = 100
        for i in exe:
            x_var = 5
            book = Label(tl, text=i[0], font=('', 11, ''))
            book.place(x=x_var, y=y_var)
            x_var = x_var + 100
            bid = Label(tl, text=i[1], font=('', 11, ''))
            bid.place(x=x_var, y=y_var)
            x_var = x_var + 100
            author = Label(tl, text=i[2], font=('', 11, ''))
            author.place(x=x_var, y=y_var)
            y_var = y_var + 25
        cur.close()
        con.close()
        tl.mainloop()
    elif but == "8.":
        con = sqlite3.connect("library")
        cur = con.cursor()
        exe = cur.execute("SELECT * FROM BOOKS")
        tl = Toplevel(root)

        def search_fun(e=None):
            print(e)
            y1 = 160
            for j1 in exe:
                print(str(search.get()) in j1)
                if str(search.get()) in j1:
                    x1 = 5
                    book_nm = Label(tl, text=j1[0], font=('', 11, ''))
                    book_nm.place(x=x1, y=y1)
                    x1 = x1 + 100
                    b_id = Label(tl, text=j1[1], font=('', 11, ''))
                    b_id.place(x=x1, y=y1)
                    x1 = x1 + 100
                    auth = Label(tl, text=j1[2], font=('', 11, ''))
                    auth.place(x=x1, y=y1)
                    y1 = y1 + 25

        tl.title("Book Search Engine")
        tl.title("Search Book")
        tl.geometry("500x300")
        Label(tl, text="Book Search Engine", font="ariel 35 bold").place(x=3, y=0)
        Label(tl, text="Search here : ", font="lucida 15 bold").place(x=3, y=75)
        search = Entry(tl, font="lucida 15")
        search.place(x=150, y=75)
        search.focus()
        search.bind("<Return>", search_fun)
        search_button = Button(tl, text="Search", padx=7, pady=3, command=search_fun)
        search_button.place(x=425, y=75)
        search.bind("<Button-1>", search_fun)
        Label(tl, text="Book", font="lucida 15").place(x=5, y=115)
        Label(tl, text="Book ID", font="lucida 15").place(x=105, y=115)
        Label(tl, text="Books Author", font="lucida 15").place(x=205, y=115)
        tl.mainloop()
    elif but == "9.":
        root.quit()
        exit()


root = Tk()
root.title("Library Management")
root.geometry("500x425")

l0 = Label(root, text="Library Management", font="ariel 35 bold")
l0.place(x=0, y=0)

b1 = Button(root, text="1.", padx=5, pady=3)
b1.place(x=3, y=70)
b1.bind("<Button-1>", click)
l1 = Label(root, text=" Issue Book", font="lucida 15")
l1.place(x=30, y=70)

b2 = Button(root, text="2.", padx=5, pady=3)
b2.place(x=3, y=110)
b2.bind("<Button-1>", click)
l2 = Label(root, text=" Return Book", font="lucida 15")
l2.place(x=30, y=110)

b3 = Button(root, text="3.", padx=5, pady=3)
b3.place(x=3, y=150)
b3.bind("<Button-1>", click)
l3 = Label(root, text=" Not returned Books", font="lucida 15")
l3.place(x=30, y=150)

b4 = Button(root, text="4.", padx=5, pady=3)
b4.place(x=3, y=190)
b4.bind("<Button-1>", click)
l4 = Label(root, text=" Personal History", font="lucida 15")
l4.place(x=30, y=190)

b5 = Button(root, text="5.", padx=5, pady=3)
b5.place(x=3, y=230)
b5.bind("<Button-1>", click)
l5 = Label(root, text=" Add new Book", font="lucida 15")
l5.place(x=30, y=230)

b6 = Button(root, text="6.", padx=5, pady=3)
b6.place(x=3, y=270)
b6.bind("<Button-1>", click)
l6 = Label(root, text=" Add new Student", font="lucida 15")
l6.place(x=30, y=270)

b7 = Button(root, text="7.", padx=5, pady=3)
b7.place(x=3, y=310)
b7.bind("<Button-1>", click)
l7 = Label(root, text=" All Books", font="lucida 15")
l7.place(x=30, y=310)

b8 = Button(root, text="8.", padx=5, pady=3)
b8.place(x=3, y=350)
b8.bind("<Button-1>", click)
l8 = Label(root, text=" Search Book", font="lucida 15")
l8.place(x=30, y=350)

b9 = Button(root, text="9.", padx=5, pady=3)
b9.place(x=3, y=390)
b9.bind("<Button-1>", click)
l9 = Label(root, text=" Exit", font="5")
l9.place(x=30, y=390)

root.mainloop()
