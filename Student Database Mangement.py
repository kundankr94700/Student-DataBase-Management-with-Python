from threading import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.font import Font
from playsound import playsound
from time import *
from tkinter import filedialog
from PIL import Image, ImageDraw,ImageFont
import sqlite3
from os import *

class th1(Thread):

    def run(self):

        conn = sqlite3.connect('stu_database.sqlite')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE if not exists Student
                                             (Roll INT PRIMARY KEY     NOT NULL,
                                             FIRST_NAME           TEXT    NOT NULL,
                                             LAST_NAME           TEXT    NOT NULL,
                                             FATHER_NAME           TEXT    NOT NULL,
                                             MOTHER_NAME           TEXT    NOT NULL,
                                             DATE_OF_BIRTH          DATE    NOT NULL,
                                             COURSE           TEXT    NOT NULL,
                                             SEMESTER           TEXT    NOT NULL,
                                             BATCH           TEXT    NOT NULL,
                                             MOBILE_NO           TEXT    NOT NULL,
                                             COUNTRY          TEXT    NOT NULL,
                                             ADDRESS        CHAR(50),
                                             IMAGE varchar2(150) not null,
                                             SIGN varchar2(150) not null,
                                             MARKS          INT);''')

        conn.commit()
        conn.close()



        def login():


            s1 = ss1.get()
            s2 = ss2.get()
            if s1 == 'Kundan' and s2 == 'Hello':
                class th3(Thread):
                    def run(self):


                        ss1.set('')
                        ss2.set('')
                        top1 = Toplevel()
                        top1.title("Student Database")

                        f4 = Font(family="Time New Roman", size=13, weight="bold", underline=1)
                        f5 = Font(family="Time New Roman", size=16, weight="bold", underline=1)
                        f6 = Font(family="Time New Roman", size=14, weight="bold")
                        f7 = Font(family="Time New Roman", size=12)




                        LL1 = Label(top1, text='Database Operation ', fg='Red', font=f4).place(x=65, y=35)
                        LL2 = Label(top1, text='Student Database Management', fg='Red', font=f5).place(x=450, y=15)

                        def add(roll, f_name, l_name, fa_name, ma_name, dob, course, sem, batch, mobile, country,
                                Address, marks,image,sign):
                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()

                            cursor.execute("INSERT INTO Student (Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN) \
                                                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ", (roll, f_name, l_name, fa_name, ma_name, dob, course, sem, batch, mobile, country, Address,marks,image,sign,));
                            conn.commit()
                            conn.close()


                        def display():

                            class tt11(Thread):
                                def run(self):
                                    conn = sqlite3.connect('stu_database.sqlite')
                                    cursor = conn.cursor()
                                    z = 0
                                    for row in cursor.execute("SELECT Roll from Student"):
                                        z += 1
                                    conn.commit()
                                    conn.close()
                                    t5 = Toplevel()
                                    t5.geometry("800x800+400+10")
                                    LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7, fg='green').place(
                                        x=670, y=360)
                                    llll = Listbox(t5)
                                    conn = sqlite3.connect('stu_database.sqlite')
                                    cursor = conn.cursor()
                                    l3 = Label(t5, text="Student DataBase Management System", fg='red', font=f1).place(
                                        x=300, y=30)
                                    lis1 = []
                                    lis2 = []
                                    for row in cursor.execute(
                                            "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS from Student"):
                                        lis1.append(str(row[0]))
                                        lis2.append(row[1] + ' ' + row[2])

                                    conn.commit()
                                    conn.close()

                                    def dis1():
                                        y15 = int(x15.get())
                                        conn = sqlite3.connect('stu_database.sqlite')
                                        cursor = conn.cursor()

                                        for row in cursor.execute(
                                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN from Student where Roll=?",
                                                (y15,)):
                                            a2 = row[1] + ' ' + row[2]
                                            LL3 = Label(t5, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                                                x=240, y=180)
                                            LL5 = Label(t5,
                                                        text='Father\'s Name        :%s                         ' % row[
                                                            3], font=f6, fg='Skyblue').place(x=240, y=220)
                                            LL6 = Label(t5,
                                                        text='Mother\'s Name       :%s                          ' % row[
                                                            4], font=f6, fg='Skyblue').place(x=240, y=260)
                                            LL7 = Label(t5,
                                                        text='Date of Birth \t: %s                              ' % row[
                                                            5], font=f6, fg='Skyblue').place(x=240, y=300)
                                            LL8 = Label(t5,
                                                        text='Course \t\t: %s                                   ' % row[
                                                            6], font=f6, fg='Skyblue').place(x=240, y=340)
                                            LL9 = Label(t5,
                                                        text='Semester\t: %s                                    ' % row[
                                                            7], font=f6, fg='Skyblue').place(x=240, y=380)
                                            LL10 = Label(t5,
                                                         text='Batch \t\t:%s                                    ' % row[
                                                             8], font=f6, fg='Skyblue').place(x=240, y=420)
                                            LL11 = Label(t5,
                                                         text='Mobile \t\t: %s                                  ' % row[
                                                             9], font=f6, fg='Skyblue').place(x=240, y=460)
                                            LL12 = Label(t5,
                                                         text='Country \t\t: %s                                 ' % row[
                                                             10], font=f6, fg='Skyblue').place(x=240, y=500)
                                            LL13 = Label(t5,
                                                         text='Address \t\t: %s                                 ' % row[
                                                             11], font=f6, fg='Skyblue').place(x=240, y=540)
                                            LL14 = Label(t5,
                                                         text='RoLL  \t\t: %s                                   ' % row[
                                                             0], font=f6, fg='Skyblue').place(x=240, y=570)
                                            LL14 = Label(t5,
                                                         text='Marks  \t\t: %s                                  ' % row[
                                                             12], font=f6, fg='Skyblue').place(x=240, y=600)
                                            ph = row[13]
                                            si = row[14]

                                        conn.commit()
                                        conn.close()
                                        ima = ('Do You Want to See Image ')
                                        l = Label(t5, text=ima, font=f6).place(x=140, y=640)
                                        d1 = IntVar()
                                        d2 = IntVar()
                                        r1 = Radiobutton(t5, text='Photo', value=1, variable=d1, font=f6).place(x=450,
                                                                                                                y=640)
                                        r2 = Radiobutton(t5, text='Signature', value=2, variable=d2, font=f6).place(
                                            x=550, y=640)

                                        def pho():
                                            if d1.get() == 1 and d2.get() == 2:
                                                Image.open(ph).show()
                                                Image.open(si).show()
                                                d1.set(0)
                                                d2.set(0)
                                            elif d1.get() == 1 or d2.get() == 2:
                                                if d1.get() == 1:
                                                    Image.open(ph).show()
                                                    d1.set(0)
                                                else:
                                                    Image.open(si).show()
                                                    d2.set(0)
                                            else:
                                                pass

                                        BBB1 = Button(t5, text='Next', bg='Green', fg='white', width=25, font=f4,
                                                      command=pho).place(x=350, y=690)


                                    def dis2():
                                        y16 = x16.get()
                                        conn = sqlite3.connect('stu_database.sqlite')
                                        cursor = conn.cursor()
                                        z1, z2 = y16.split(' ')

                                        for row in cursor.execute(
                                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN from Student where FIRST_NAME=? and LAST_NAME= ?",
                                                (z1, z2,)):

                                            a2 = row[1] + ' ' + row[2]
                                            LL3 = Label(t5, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                                                x=240,
                                                y=180)
                                            LL5 = Label(t5,
                                                        text='Father\'s Name        :%s                         ' % row[
                                                            3],
                                                        font=f6, fg='Skyblue').place(x=240, y=220)
                                            LL6 = Label(t5,
                                                        text='Mother\'s Name       :%s                          ' % row[
                                                            4],
                                                        font=f6, fg='Skyblue').place(x=240, y=260)
                                            LL7 = Label(t5,
                                                        text='Date of Birth \t: %s                              ' % row[
                                                            5],
                                                        font=f6, fg='Skyblue').place(x=240, y=300)
                                            LL8 = Label(t5,
                                                        text='Course \t\t: %s                                   ' % row[
                                                            6],
                                                        font=f6, fg='Skyblue').place(x=240, y=340)
                                            LL9 = Label(t5,
                                                        text='Semester\t: %s                                    ' % row[
                                                            7],
                                                        font=f6, fg='Skyblue').place(x=240, y=380)
                                            LL10 = Label(t5,
                                                         text='Batch \t\t:%s                                    ' % row[
                                                             8],
                                                         font=f6, fg='Skyblue').place(x=240, y=420)
                                            LL11 = Label(t5,
                                                         text='Mobile \t\t: %s                                  ' % row[
                                                             9],
                                                         font=f6, fg='Skyblue').place(x=240, y=460)
                                            LL12 = Label(t5,
                                                         text='Country \t\t: %s                                 ' % row[
                                                             10],
                                                         font=f6, fg='Skyblue').place(x=240, y=500)
                                            LL13 = Label(t5,
                                                         text='Address \t\t: %s                                 ' % row[
                                                             11],
                                                         font=f6, fg='Skyblue').place(x=240, y=540)
                                            LL14 = Label(t5,
                                                         text='RoLL  \t\t: %s                                   ' % row[
                                                             0],
                                                         font=f6, fg='Skyblue').place(x=240, y=570)
                                            LL14 = Label(t5,
                                                         text='Marks  \t\t: %s                                  ' % row[
                                                             12],
                                                         font=f6, fg='Skyblue').place(x=240, y=600)
                                            ph=row[13]
                                            si=row[14]

                                        conn.commit()
                                        conn.close()
                                        ima = ('Do You Want to See Image ')
                                        l = Label(t5, text=ima, font=f6).place(x=140, y=640)
                                        d1 = IntVar()
                                        d2 = IntVar()
                                        r1 = Radiobutton(t5, text='Photo', value=1, variable=d1, font=f6).place(x=450,
                                                                                                                y=640)
                                        r2 = Radiobutton(t5, text='Signature', value=2, variable=d2, font=f6).place(
                                            x=550, y=640)

                                        def pho():
                                            if d1.get() == 1 and d2.get() == 2:
                                                Image.open(ph).show()
                                                Image.open(si).show()
                                                d1.set(0)
                                                d2.set(0)
                                            elif d1.get() == 1 or d2.get() == 2:
                                                if d1.get() == 1:
                                                    Image.open(ph).show()
                                                    d1.set(0)
                                                else:
                                                    Image.open(si).show()
                                                    d2.set(0)
                                            else:
                                                pass

                                        BBB1 = Button(t5, text='Next', bg='Green', fg='white', width=25, font=f4,
                                                      command=pho).place(x=350, y=690)
                                    x15 = StringVar()
                                    x16 = StringVar()
                                    x17 = StringVar()
                                    c6 = Combobox(t5, values=lis1, width=18, textvariable=x15).place(x=280, y=80)
                                    x15.set('Select Roll Number ')
                                    c7 = Combobox(t5, values=lis2, width=18, textvariable=x16).place(x=280, y=120)
                                    x16.set('Select Name ')

                                    b1 = Button(t5, text='Display', command=dis1, width=30, height=1, bg='green',fg='white', font=f3).place(x=480, y=80)
                                    b3 = Button(t5, text='Display', command=dis2, width=30, height=1, font=f3).place(x=480, y=120)

                            class tt12(Thread):
                                def run(self):
                                    playsound('Audio\\disp.mp3')
                            ttt11=tt11()
                            ttt12=tt12()
                            ttt11.start()
                            sleep(0.05)
                            ttt12.start()
                        def search(pp):
                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()
                            z,y = 0,0
                            for row in cursor.execute(
                                    "SELECT Roll from Student"):
                                if pp==row[0]:
                                    y=1

                                z += 1
                            conn.commit()
                            conn.close()
                            if y==1:
                                LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7, fg='green').place(x=670,
                                                                                                                  y=360)

                                conn = sqlite3.connect('stu_database.sqlite')
                                cursor = conn.cursor()
                                top4 = Toplevel()
                                top4.title("Display Record")
                                top4.geometry("550x720+600+50")
                                l3 = Label(top4, text="Student DataBase Management System", fg='red', font=f1).place(
                                    x=120,
                                    y=30)
                                for row in cursor.execute(
                                        "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN from Student where Roll=?",
                                        (pp,)):
                                    a2 = row[1] + ' ' + row[2]
                                    LL3 = Label(top4, text='Name \t\t: %s' % a2, font=f6, fg='Skyblue').place(
                                        x=140, y=80)
                                    LL5 = Label(top4,
                                                text='Father\'s Name        :%s                         ' % row[
                                                    3], font=f6, fg='Skyblue').place(x=140, y=120)
                                    LL6 = Label(top4,
                                                text='Mother\'s Name       :%s                          ' % row[
                                                    4], font=f6, fg='Skyblue').place(x=140, y=160)
                                    LL7 = Label(top4,
                                                text='Date of Birth \t: %s                              ' % row[
                                                    5], font=f6, fg='Skyblue').place(x=140, y=200)
                                    LL8 = Label(top4,
                                                text='Course \t\t: %s                                   ' % row[
                                                    6], font=f6, fg='Skyblue').place(x=140, y=240)
                                    LL9 = Label(top4,
                                                text='Semester\t: %s                                    ' % row[
                                                    7], font=f6, fg='Skyblue').place(x=140, y=280)
                                    LL10 = Label(top4,
                                                 text='Batch \t\t:%s                                    ' % row[
                                                     8], font=f6, fg='Skyblue').place(x=140, y=320)
                                    LL11 = Label(top4,
                                                 text='Mobile \t\t: %s                                  ' % row[
                                                     9], font=f6, fg='Skyblue').place(x=140, y=360)
                                    LL12 = Label(top4,
                                                 text='Country \t\t: %s                                 ' % row[
                                                     10], font=f6, fg='Skyblue').place(x=140, y=400)
                                    LL13 = Label(top4,
                                                 text='Address \t\t: %s                                 ' % row[
                                                     11], font=f6, fg='Skyblue').place(x=140, y=440)
                                    LL14 = Label(top4,
                                                 text='RoLL  \t\t: %s                                   ' % row[
                                                     0], font=f6, fg='Skyblue').place(x=140, y=470)
                                    LL14 = Label(top4,
                                                 text='Marks  \t\t: %s                                  ' % row[
                                                     12], font=f6, fg='Skyblue').place(x=140, y=500)
                                    ph = row[13]
                                    si = row[14]
                                conn.commit()
                                conn.close()
                                ima = ('Do You Want to See Image ')
                                l = Label(top4, text=ima, font=f6).place(x=20, y=540)
                                d1 = IntVar()
                                d2 = IntVar()
                                r1 = Radiobutton(top4, text='Photo', value=1, variable=d1, font=f6).place(x=300, y=540)
                                r2 = Radiobutton(top4, text='Signature', value=2, variable=d2, font=f6).place(x=400,
                                                                                                              y=540)

                                def pho():
                                    if d1.get() == 1 and d2.get() == 2:
                                        Image.open(ph).show()
                                        Image.open(si).show()
                                        d1.set(0)
                                        d2.set(0)
                                    elif d1.get() == 1 or d2.get() == 2:
                                        if d1.get() == 1:
                                            Image.open(ph).show()
                                            d1.set(0)
                                        else:
                                            Image.open(si).show()
                                            d2.set(0)
                                    else:
                                        pass

                                BBB1 = Button(top4, text='Next', bg='Green', fg='white', width=25, font=f4,
                                              command=pho).place(x=150, y=590)
                                BBB1 = Button(top4, text='Close', bg='red', fg='white', width=25, font=f4,
                                              command=top4.destroy).place(x=150, y=640)
                            else:
                                top8 = Toplevel()
                                top8.title("Display Record")
                                top8.geometry("350x50+600+300")
                                l=Label(top8,text='Record Not Found',font=f6,fg='red').pack()
                                playsound('record1.mp3')



                        def updateM(j, i):

                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()

                            conn.execute("UPDATE Student set MARKS = ? where ROLL = ?", (i, j))
                            conn.commit()

                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()



                        def updateA(j, i):
                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()

                            conn.execute("UPDATE Student set ADDRESS = ? where ROLL = ?", (i, j))
                            conn.commit()

                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()



                        def updateP(j, i):
                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()

                            conn.execute("UPDATE Student set MOBILE_NO = ? where ROLL = ?", (i, j))
                            conn.commit()

                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()


                        def delete(k):
                            conn = sqlite3.connect('stu_database.sqlite')
                            cursor = conn.cursor()
                            z, y = 0, 0
                            for row in cursor.execute(
                                    "SELECT Roll from Student"):
                                if k == row[0]:
                                    y = 1

                                z += 1
                            conn.commit()
                            conn.close()
                            if y == 1:
                                conn = sqlite3.connect('stu_database.sqlite')
                                cursor = conn.cursor()
                                conn.execute("DELETE from  Student where ROLL = ?", (k,))
                                conn.commit()

                            else:
                                top8 = Toplevel()
                                top8.title("Display Record")
                                top8.geometry("350x50+600+300")
                                l=Label(top8,text='Record Not Found',font=f6,fg='red').pack()
                                playsound('record1.mp3')



                        def add_record():
                            yy1 = xx1.get()
                            yy2 = xx2.get()
                            yy3 = xx3.get()
                            yy4 = xx4.get()
                            yy5 = xx5.get()
                            yy6 = xx6.get()
                            yy7 = xx7.get()
                            yy8 = xx8.get()
                            yy9 = xx9.get()
                            yy10 =xx10.get()
                            yy11 = xx11.get()
                            yy12 = xx12.get()
                            yy13 = xx13.get()
                            yy14 = xx14.get()
                            yy15 = xx15.get()

                            l11='ABCDEFGHIJKLMNOPQRSTUVWXYQ '
                            l12=list(l11)
                            def valid(qq):
                                for i in qq:
                                    if i not in l12:
                                        return 1

                            if yy1 == '' or yy2 == '' or yy3 == '' or yy4 == '' or yy5 == '' or yy6 == '' or yy7 == '' or yy8 == '' or yy9 == '' or yy10 == '' or yy11 == '' or yy12 == '' or yy13 == '' or yy14 == '' or yy15 == '':
                                if yy14 == '' or yy15 == '':
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text="Please Upload Photos And Signature Both .",
                                               fg='skyblue', font=f1).place(x=50, y=15)
                                    playsound('add11.mp3')
                                else:

                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11,
                                               text="Some Details are Not Entered \n please Fill all the details",
                                               fg='skyblue', font=f1).place(x=50, y=15)
                                    playsound('Audio\\add1.mp3')


                            elif yy9.isdigit() == FALSE or len(yy9) !=10 or yy12.isdigit() == False or yy13.isdigit()==False :
                                if (yy9.isdigit() == FALSE or len(yy9) != 10) and (yy12.isdigit() == False):
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text="Invalid ROll and Mobile Number.", fg='skyblue',
                                               font=f1).place(x=50, y=15)
                                    playsound('add2.mp3')


                                elif yy12.isdigit() == False:
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text="Invalid Roll Number.", fg='skyblue',
                                               font=f1).place(x=80, y=25)
                                    playsound('Audio\\add3.mp3')

                                elif yy13.isdigit() == False :
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text=" Invalid Marks", fg='skyblue',
                                               font=f1).place(x=80, y=25)
                                    playsound('Audio\\add9.mp3')

                                else:
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text="Invalid  Mobile Number.", fg='skyblue',
                                               font=f1).place(x=80, y=25)
                                    playsound('Audio\\add4.mp3')

                            elif yy1.isalpha() == False or yy2.isalpha() == False or valid(yy3.upper())==1 or valid(yy4.upper())==1 :
                                top11 = Toplevel()
                                top11.title("ADD  Record")
                                top11.geometry("400x80+600+200")
                                l3 = Label(top11,
                                           text="Some Details are Not in Appropriate Format ",
                                           fg='skyblue', font=f1).place(x=50, y=15)
                                playsound('add8.mp3')

                            else:
                                yyx12=int(yy12)
                                yy13=int(yy13)
                                if (yy13) > 100:
                                    top11 = Toplevel()
                                    top11.title("ADD  Record")
                                    top11.geometry("320x80+600+200")
                                    l3 = Label(top11, text=" Marks Greater Then 100 .", fg='skyblue',
                                               font=f1).place(x=80, y=25)
                                    playsound('add10.mp3')
                                else:
                                    v = 1
                                    conn = sqlite3.connect('stu_database.sqlite')
                                    cursor = conn.cursor()
                                    for row in cursor.execute("SELECT Roll from Student "):
                                        zz = row[0]
                                        if zz == yyx12:
                                            top11 = Toplevel()
                                            top11.title("ADD  Record")
                                            top11.geometry("400x80+600+200")
                                            l3 = Label(top11, text="Record Already Exist.", fg='skyblue',
                                                       font=f1).place(x=120, y=25)
                                            v = 10

                                            break

                                    conn.commit()
                                    conn.close()
                                    if v == 1:
                                        add(yyx12, yy1, yy2, yy3, yy4, yy5, yy6, yy7, yy8, yy9, yy10, yy11, yy13,yy14,yy15)
                                        conn = sqlite3.connect('stu_database.sqlite')
                                        cursor = conn.cursor()
                                        z = 0
                                        for row in cursor.execute(
                                                "SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS from Student"):
                                            z += 1
                                        conn.commit()
                                        conn.close()
                                        LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7,
                                                     fg='green').place(
                                            x=670, y=360)
                                        playsound('add5.mp3')
                                    else:
                                        playsound('add7.mp3')



                        def delete_record():
                            class th5(Thread):
                                def run(self):

                                    def dele():
                                        yyy1 = int(xxx1.get())
                                        delete(yyy1)
                                        conn = sqlite3.connect('stu_database.sqlite')
                                        cursor = conn.cursor()
                                        z = 0
                                        for row in cursor.execute("SELECT Roll from Student"):
                                            z += 1
                                        conn.commit()
                                        conn.close()
                                        LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7,
                                                     fg='green').place(x=670,
                                                                       y=360)

                                        top2.destroy()

                                    top2 = Toplevel()
                                    top2.title("Delete Record")
                                    top2.geometry("400x200+600+200")
                                    xxx1 = StringVar()
                                    l3 = Label(top2, text="Student DataBase Management System", fg='skyblue',
                                               font=f1).place(
                                        x=50, y=15)
                                    LLL1 = Label(top2, text='Enter Roll Number:', font=f6, fg='red').place(x=40, y=60)
                                    EEE1 = Entry(top2, textvariable=xxx1, width=14, font=f7).place(x=240, y=63)
                                    BBB1 = Button(top2, text='Delete', bg='Green', fg='white', width=25, font=f4,
                                                  command=dele).place(x=70, y=110)
                            class th6(Thread):
                                def run(self):
                                    playsound('roll3.mp3')
                            t5=th5()
                            t6=th6()
                            t5.start()
                            sleep(0.05)
                            t6.start()
                        def Search_record():

                            class th7(Thread):
                                def run(self):
                                    def sear():
                                        top3.destroy()
                                        yyyy1 = int(xxxx1.get())
                                        search(yyyy1)

                                        top3.destroy()

                                    top3 = Toplevel()
                                    top3.title("Search  Record")
                                    top3.geometry("400x200+600+200")
                                    xxxx1 = StringVar()
                                    l3 = Label(top3, text="Student DataBase Management System", fg='skyblue',
                                               font=f1).place(
                                        x=50, y=15)
                                    LLL1 = Label(top3, text='Enter Roll Number:', font=f6, fg='red').place(x=40, y=50)
                                    EEE1 = Entry(top3, textvariable=xxxx1, width=14, font=f7).place(x=240, y=53)
                                    BBB1 = Button(top3, text='Search', bg='Green', fg='white', width=25, font=f4,
                                                  command=sear).place(x=70, y=110)
                            class th8(Thread):
                                def run(self):
                                    playsound('roll1.mp3')

                            t7 = th7()
                            t8 = th8()
                            t7.start()
                            sleep(0.2)
                            t8.start()


                        def clear():
                            aaa=messagebox.askyesno('Clear','Do you Want to Clear')
                            if aaa==True:
                                xx1.set('')
                                xx2.set('')
                                xx3.set('')
                                xx4.set('')
                                xx5.set('')
                                xx6.set('Select course')
                                xx7.set('select semester')
                                xx8.set('')
                                xx9.set('')
                                xx10.set('select country')
                                xx11.set('')
                                xx12.set('')
                                xx13.set('')



                        def update_record():
                            class th9(Thread):
                                def run(self):

                                    def upda():
                                        conn = sqlite3.connect('stu_database.sqlite')
                                        cursor = conn.cursor()
                                        z, y = 0, 0
                                        for row in cursor.execute(
                                                "SELECT Roll from Student"):
                                            if int(xxxx1.get())== row[0]:
                                                y = 1

                                            z += 1
                                        conn.commit()
                                        conn.close()
                                        if y==1:
                                            top6.destroy()
                                            yyyy1 = int(xxxx1.get())
                                            top5 = Toplevel()
                                            top5.title("Update  Record")
                                            top5.geometry("400x400+450+100")

                                            def marks():
                                                def Mar():
                                                    top5.destroy()
                                                    zz1 = int(qq1.get())
                                                    updateM(yyyy1, zz1)

                                                    top7.destroy()

                                                top7 = Toplevel()
                                                top7.title("Search  Record")
                                                top7.geometry("400x200+600+200")
                                                qq1 = StringVar()
                                                l3 = Label(top7, text="Student DataBase Management System",
                                                           fg='skyblue',
                                                           font=f1).place(
                                                    x=50, y=15)
                                                LLL1 = Label(top7, text='Enter New Marks:', font=f6, fg='red').place(
                                                    x=40,
                                                    y=50)
                                                EEE1 = Entry(top7, textvariable=qq1, width=14, font=f7).place(x=240,
                                                                                                              y=53)
                                                BBB1 = Button(top7, text='Done', bg='Green', fg='white', width=25,
                                                              font=f4,
                                                              command=Mar).place(x=70, y=110)

                                            def address():
                                                def Arr():
                                                    top5.destroy()
                                                    zzz1 = qqq1.get()
                                                    updateA(yyyy1, zzz1)

                                                    top8.destroy()

                                                top8 = Toplevel()
                                                top8.title("Modify  Record")
                                                top8.geometry("600x200+600+200")
                                                qqq1 = StringVar()
                                                l3 = Label(top8, text="Student DataBase Management System",
                                                           fg='skyblue',
                                                           font=f1).place(x=200, y=15)

                                                LLL1 = Label(top8, text='Enter New Address:', font=f6, fg='red').place(
                                                    x=40,
                                                    y=50)
                                                EEE1 = Entry(top8, textvariable=qqq1, width=30, font=f7).place(x=240,
                                                                                                               y=53)
                                                BBB1 = Button(top8, text='Done', bg='Green', fg='white', width=25,
                                                              font=f4,
                                                              command=Arr).place(x=150, y=110)

                                            def phone():
                                                def pho():
                                                    top5.destroy()
                                                    zzzz1 = int(qqqq1.get())
                                                    updateP(yyyy1, zzzz1)

                                                    top9.destroy()

                                                top9 = Toplevel()
                                                top9.title("Modify  Record")
                                                top9.geometry("400x200+600+200")
                                                qqqq1 = StringVar()
                                                l3 = Label(top9, text="Student DataBase Management System",
                                                           fg='skyblue',
                                                           font=f1).place(x=50, y=15)

                                                LLL1 = Label(top9, text='Enter New Phone:', font=f6, fg='red').place(
                                                    x=40,
                                                    y=50)
                                                EEE1 = Entry(top9, textvariable=qqqq1, width=14, font=f7).place(x=240,
                                                                                                                y=53)
                                                BBB1 = Button(top9, text='Done', bg='Green', fg='white', width=25,
                                                              font=f4,
                                                              command=pho).place(x=70, y=110)

                                            l3 = Label(top5, text="Student DataBase Management System", fg='skyblue',
                                                       font=f1).place(x=50, y=15)

                                            LLL1 = Label(top5, text='Select The Field:', font=f6, fg='red').place(x=120,
                                                                                                                  y=50)
                                            BBB1 = Button(top5, text='Marks', bg='Green', fg='white', width=25, font=f4,
                                                          command=marks).place(x=70, y=110)
                                            BBB2 = Button(top5, text='Address', bg='skyblue', fg='white', width=25,
                                                          font=f4,
                                                          command=address).place(x=70, y=160)
                                            BBB3 = Button(top5, text='Phone', bg='white', fg='black', width=25, font=f4,
                                                          command=phone).place(x=70, y=210)
                                            BBB4 = Button(top5, text='Close', bg='red', fg='white', width=25, font=f4,
                                                          command=top5.destroy).place(x=70, y=260)
                                        else:
                                            top15 = Toplevel()
                                            top15.title("Display Record")
                                            top15.geometry("350x50+600+300")
                                            l = Label(top15, text='Record Not Found', font=f6, fg='red').pack()
                                            playsound('record1.mp3')


                                    top6 = Toplevel()
                                    top6.title("Update Record")
                                    top6.geometry("400x200+750+200")
                                    xxxx1 = StringVar()
                                    l3 = Label(top6, text="Student DataBase Management System", fg='skyblue',
                                               font=f1).place(
                                        x=50, y=15)
                                    LLL1 = Label(top6, text='Enter Roll Number:', font=f6, fg='red').place(x=40, y=50)
                                    EEE1 = Entry(top6, textvariable=xxxx1, width=14, font=f7).place(x=240, y=53)
                                    BBB1 = Button(top6, text='Next', bg='Green', fg='white', width=25, font=f4,
                                                  command=upda).place(x=70, y=110)
                                    BBB1 = Button(top6, text='close', bg='red', fg='white', width=25, font=f4,
                                                  command=top6.destroy).place(x=70, y=150)
                            class th10(Thread):
                                def run(self):
                                    playsound('roll2.mp3')
                            t9=th9()
                            t10=th10()
                            t9.start()
                            sleep(0.2)
                            t10.start()

                        xx1 = StringVar()
                        xx2 = StringVar()
                        xx3 = StringVar()
                        xx4 = StringVar()
                        xx5 = StringVar()
                        xx6 = StringVar()
                        xx7 = StringVar()
                        xx8 = StringVar()
                        xx9 = StringVar()
                        xx10 = StringVar()
                        xx11 = StringVar()
                        xx12 = StringVar()
                        xx13 = StringVar()
                        xx14= StringVar()
                        xx15= StringVar()

                        LL3 = Label(top1, text='First Name:', font=f6, fg='Skyblue').place(x=260, y=80)
                        LL4 = Label(top1, text='Last Name:', font=f6, fg='Skyblue').place(x=550, y=80)
                        LL5 = Label(top1, text='Father\'s Name:', font=f6, fg='Skyblue').place(x=260, y=120)
                        LL6 = Label(top1, text='Mother\'s Name:', font=f6, fg='Skyblue').place(x=550, y=120)
                        LL7 = Label(top1, text='Date of Birth:', font=f6, fg='Skyblue').place(x=260, y=160)
                        LL8 = Label(top1, text='Course :', font=f6, fg='Skyblue').place(x=550, y=160)
                        LL9 = Label(top1, text='Semester:', font=f6, fg='Skyblue').place(x=260, y=200)
                        LL10 = Label(top1, text='Batch:', font=f6, fg='Skyblue').place(x=550, y=200)
                        LL11 = Label(top1, text='Mobile:', font=f6, fg='Skyblue').place(x=260, y=240)
                        LL12 = Label(top1, text='Country:', font=f6, fg='Skyblue').place(x=550, y=240)
                        LL13 = Label(top1, text='Address:', font=f6, fg='Skyblue').place(x=260, y=280)
                        LL14 = Label(top1, text='RoLL:', font=f6, fg='Skyblue').place(x=260, y=320)
                        LL14 = Label(top1, text='Marks:', font=f6, fg='Skyblue').place(x=550, y=320)
                        l3 = Label(top1, text="Copyright @ Kundan Kumar & Team", fg='Blue').place(x=20, y=380)

                        cour=['B.Tech','M.Tech','BSA','MCA','DCA','MBA','LAW']
                        sem=['1st','2nd','3rd','4th','5th','6th','7th','8th']
                        coun=['India','Nepal','Bhutan','Afganistan','Other']
                        bat=['2017 Onwards','2018 Onwards','2019 Onwards']

                        EE1 = Entry(top1, textvariable=xx1, width=14, font=f7).place(x=410, y=80)
                        EE2 = Entry(top1, textvariable=xx2, width=14, font=f7).place(x=700, y=80)
                        EE3 = Entry(top1, textvariable=xx3, width=14, font=f7).place(x=410, y=120)
                        EE4 = Entry(top1, textvariable=xx4, width=14, font=f7).place(x=700, y=120)
                        EE5 = Entry(top1, textvariable=xx5, width=14, font=f7).place(x=410, y=160)
                        c1=Combobox(top1,values=cour,width=18,textvariable=xx6).place(x=700,y=160)
                        xx6.set('Select Course ')
                        c2 = Combobox(top1, values=sem, width=18,textvariable=xx7).place(x=410, y=200)
                        xx7.set('Select Semester ')

                        c3 = Combobox(top1, values=coun, width=18,textvariable=xx10).place(x=700, y=240)
                        xx10.set('Select Country ')
                        c4 = Combobox(top1, values=bat, width=18, textvariable=xx8).place(x=700, y=200)
                        xx8.set('Select Batch ')
                        EE9 = Entry(top1, textvariable=xx9, width=14, font=f7).place(x=410, y=240)
                        EE11 = Entry(top1, textvariable=xx11, width=46, font=f7).place(x=410, y=280)
                        EE12 = Entry(top1, textvariable=xx12, width=14, font=f7).place(x=410, y=320)
                        EE13 = Entry(top1, textvariable=xx13, width=14, font=f7).place(x=700, y=320)
                        EE14 = Entry(top1, textvariable=xx14, width=14, font=f7)
                        EE15 = Entry(top1, textvariable=xx15, width=14, font=f7)
                        xx14.set('')
                        xx15.set('')
                        def image_upload():
                            xxx14 = filedialog.askopenfilename(initialdir="/", title="select file",filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
                            xx14.set(xxx14)


                        def sign_upload():

                            xxx15 = filedialog.askopenfilename(initialdir="/", title="select file",filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))
                            xx15.set(xxx15)

                        def ID_Ge():

                            def gen():
                                top3.destroy()



                                pp = int(xxxx1.get())

                                conn = sqlite3.connect('stu_database.sqlite')
                                cursor = conn.cursor()
                                z, y = 0, 0
                                for row in cursor.execute(
                                        "SELECT Roll from Student"):
                                    if pp == row[0]:
                                        y = 1

                                    z += 1
                                conn.commit()
                                conn.close()
                                if y == 1:
                                    image = Image.new('RGB', (500, 360), (255, 255, 255))
                                    d = ImageDraw.Draw(image)
                                    color = 'rgb(0, 0, 0)'

                                    font1 = ImageFont.truetype("arial.ttf", 15)
                                    font2 = ImageFont.truetype("arial.ttf", 18)
                                    font3 = ImageFont.truetype("arial.ttf", 22)
                                    d.text((83, 80), '12 K.M. Stone,Amritsar-jalandhar G.T. Road,Amritsar', fill=color,
                                           font=font1)
                                    d.text((120, 97), 'Tel:0183-5069530,5069532,5069534', fill=color, font=font1)
                                    LLL2 = Label(top1, text='Number Of Records : %d ' % z, font=f7, fg='green').place(
                                        x=670,
                                        y=360)

                                    conn = sqlite3.connect('stu_database.sqlite')
                                    cursor = conn.cursor()

                                    for row in cursor.execute("SELECT Roll,FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,DATE_OF_BIRTH,COURSE,SEMESTER,BATCH,MOBILE_NO,COUNTRY,ADDRESS,MARKS,IMAGE,SIGN from Student where Roll=?",(pp,)) :
                                        a=row[1].capitalize()+' ' +row[2].capitalize()
                                        d.text((120, 120), a, fill=color, font=font3)
                                        d.text((19, 145), 'F_Name         ' + row[3].capitalize(), fill=color, font=font2)
                                        d.text((19, 170), 'M_Name        ' + row[4].capitalize(), fill=color, font=font2)
                                        d.text((19, 195), 'Roll No          ' + str(row[0]), fill=color, font=font2)
                                        d.text((19, 220), 'Course           ' + row[6], fill=color, font=font2)
                                        d.text((19, 245), 'DOB              ' + row[5], fill=color, font=font2)
                                        d.text((220, 220), 'Semester ' + row[7], fill=color, font=font2)
                                        d.text((19, 270), 'Mobile_No      ' + row[9], fill=color, font=font2)
                                        d.text((19, 295), 'Country          ' + row[10].capitalize(), fill=color, font=font2)
                                        d.text((19, 320), 'Address          ' + row[11].capitalize(), fill=color, font=font2)
                                        img = row[14]
                                        img3 = row[13]
                                    conn.commit()
                                    conn.close()
                                    img4 = Image.open('log.png').resize((450, 80), Image.ANTIALIAS)
                                    img1 = Image.open(img).resize((105, 60), Image.ANTIALIAS)
                                    img2 = Image.open(img3).resize((105, 150), Image.ANTIALIAS)
                                    image.paste(img2, (369, 120))
                                    image.paste(img4, (0, 0))
                                    image.paste(img1, (369, 280))
                                    image.save('D:\\Student Database Management\\ID\\%s'%(str(a) + '.png'))
                                    image.show()
                                    playsound('Audio\\id11.mp3')

                                else:
                                    top8 = Toplevel()
                                    top8.title("ID Generator ")
                                    top8.geometry("350x50+600+300")
                                    l = Label(top8, text='Record Not Found', font=f6, fg='red').pack()
                                    playsound('Audio\\record1.mp3')


                                top3.destroy()

                            top3 = Toplevel()
                            top3.title("Generate ID")
                            top3.geometry("400x200+600+200")
                            xxxx1 = StringVar()
                            l3 = Label(top3, text="Student DataBase Management System", fg='skyblue',
                                       font=f1).place(
                                x=50, y=15)
                            LLL1 = Label(top3, text='Enter Roll Number:', font=f6, fg='red').place(x=40, y=50)
                            EEE1 = Entry(top3, textvariable=xxxx1, width=14, font=f7).place(x=240, y=53)
                            BBB1 = Button(top3, text='Generate ID', bg='Green', fg='white', width=25, font=f4,
                                          command=gen).place(x=70, y=110)


                        c2 = Canvas(top1, width=200, height=100)
                        c2.place(x=870, y=70)
                        c2.create_image(0, 0, image=p1, anchor=NW)

                        c3 = Canvas(top1, width=200, height=70)
                        c3.place(x=870, y=215)
                        c3.create_image(0, 0, image=p3, anchor=NW)

                        c4 = Canvas(top1, width=150, height=270)
                        c4.place(x=5, y=70)
                        c4.create_image(0, 0, image=p2, anchor=NW)

                        BB1 = Button(top1, text='Add ', bg='Green', fg='white', width=15, font=f4,
                                     command=add_record).place(x=70, y=90)
                        BB2 = Button(top1, text='Display ', bg='Skyblue', fg='white', width=15, font=f4,
                                     command=display).place(x=70, y=130)
                        BB3 = Button(top1, text='Search', bg='white', fg='black', width=15, font=f4,
                                     command=Search_record).place(x=70, y=170)
                        BB5 = Button(top1, text='Update ', bg='black', fg='white', width=15, font=f4,
                                     command=update_record).place(x=70, y=210)
                        BB4 = Button(top1, text='Delete', bg='orange', fg='white', width=15, font=f4,
                                     command=delete_record).place(x=70, y=250)
                        BB5 = Button(top1, text='Close', bg='Red', fg='white', width=15, font=f4,
                                     command=top1.destroy).place(x=70, y=330)
                        BB6 = Button(top1, text='Clear', bg='White', fg='black', width=10, font=f3,
                                     command=clear ).place(x=370, y=360)
                        BB7 = Button(top1, text='Upload Image', bg='White', fg='black', width=20, font=f3,
                                     command= image_upload).place(x=890, y=180)
                        BB8 = Button(top1, text='Upload Signature', bg='White', fg='black', width=20, font=f3,
                                     command=sign_upload ).place(x=890, y=300)
                        BB8 = Button(top1, text='Generate ID', bg='Pink', fg='black', width=19, font=f3,
                                     command=ID_Ge).place(x=70, y=290)

                        top1.geometry("1150x400+300+100")
                        c1 = Canvas(top1, width=20, height=400, bg='White')
                        c1.pack(side=RIGHT)
                        c1 = Canvas(top1, width=10, height=400, bg='orange')
                        c1.pack(side=RIGHT)
                        #top1.mainloop()
                class th4(Thread):
                    def run(self):
                        playsound('login2.mp3')

                t3=th3()
                t4=th4()
                t3.start()
                sleep(.2)
                t4.start()

            elif s1 == '' and s2 == '':

                o1="Message: Please Enter Username and Password"

                playsound('sound3.mp3')
                L1=Label(root,text=o1,font=f3).place(x=130,y=320)
            else:
                o2="Please Enter Invalid Username Or Password"
                L2 = Label(root, text=o2, font=f3).place(x=130, y=320)
                playsound('sound4.mp3')
        def win():
            ans1 = messagebox.askyesno("Exit", "DO You Want to Exit")
            if ans1 == True:
                root.quit()

        p, k = 0, 0
        root = Tk()
        try:
            mkdir('D:\\student DataBase Management\\ID\\')
        except:
            pass
        f1 = Font(family="Time New Roman", size=13, weight="bold",underline=1)
        f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
        f3 = Font(family="Time New Roman", size=10, weight="bold")
        c1 = Canvas(root,width=100, height=550)
        c1.pack(side=LEFT)

        p2 = PhotoImage(file="1.png")
        xxX14 = "photo_upload.png"
        xxX15 = "sign.png"
        p1 = PhotoImage(file=xxX14)
        p3 = PhotoImage(file=xxX15)

        c1.create_image(0, 0, image=p2)

        root.title("Student DataBase Management System")
        l3 = Label(root, text="Student DataBase Management System", fg='red', font=f1).place(x=120,y=30)
        l3 = Label(root, text=" Welcome To DataBase", fg='blue', font=f1).place(x=170, y=60)
        l3 = Label(root, text="Enter Username and Password", fg='red', font=f1).place(x=140,y=120)
        l3 = Label(root, text="Copyright @ Kundan Kumar & Team", fg='Blue').place(x=250, y=380)

        l1 = Label(root, text='Username', fg='Blue',font=f1).place(x=120,y=160)
        l2 = Label(root, text='Password', fg='Blue',font=f1).place(x=120,y=200)
        ss1=StringVar()
        ss2 = StringVar()
        e1 = Entry(root,textvariable=ss1).place(x=220,y=160)
        e2 = Entry(root,textvariable=ss2, show='*').place(x=220,y=200)
        b1 = Button(root, text='Login', command=login, width=30, height=1, bg='green', fg='white',font=f3).place(x=150,y=250)
        b3 = Button(root, text='Exit', command=win, width=30, height=1,font=f3).place(x=150,y=280)
        c1 = Canvas(root, width=20, height=400, bg='White')
        c1.pack(side=RIGHT)
        c1 = Canvas(root, width=10, height=400, bg='orange')
        c1.pack(side=RIGHT)
        root.geometry("500x400+500+100")
        root.mainloop()

class th2(Thread):
    def run(self):
        playsound('rdbms1.mp3')

t1=th1()
t2=th2()
t1.start()
sleep(0.01)
t2.start()
