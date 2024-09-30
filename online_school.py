from tkinter import *
from tkinter.messagebox import askyesno

import tkinter as tk

from tkinter import StringVar

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
import mysql.connector


window = Tk()

window.geometry('1920x1080+0+0')
window.title('M C Q  Master APP Online School')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='teacher_home.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0,height=1080,width=1920)


def menu():
    #loginFrame = Frame(window, bg='#131313', bd=0)
    #loginFrame.place(x=1050,y=50, width=800, height=950)  # 1300x,550y

    borderFrame=Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow', background='#131313',
          highlightthickness=3)
    borderFrame.place(x=710,y=50)

    l1 = Label(window, text="M", fg='blue', bg='#131313', font=('SimSun', 65, 'bold'))
    l1.place(x=860, y=100)

    Label(window, text="C Q", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=950,
                                                                                             y=100)
    Label(window, text="Master", fg='white', bg='#131313', font=('SimSun', 50, 'bold')).place(x=1120,
                                                                                                y=200)

    Label(window, text="Online School Conception", fg='#5499C7', bg='#131313',
          font=('SimSun', 35, 'bold')).place(x=810,
                                             y=330)#fg='#154360'

    Label(window, text="What's Your Level ?",
          fg='white', bg='#131313', font=('SimSun', 25, 'bold')).place(x=920,
                                                                       y=470)
    #Label(window, text="us you will have deeper knowledge of the subjects that will ",
          #fg='#5499C7', bg='#131313', font=('SimSun', 15, 'bold')).place(x=1110,
                      #                                                 y=480)
   # Label(window, text="be espectally useful for you when climbing thecareer ladder.", fg='#5499C7', bg='#131313',
          #font=('SimSun', 15, 'bold')).place(x=1110,
                       #                      y=510)


    Button(window, text="Ordinary Level", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=600, height=50, width=600)

    Button(window,text="Advance Level", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=700, height=50, width=600)

    Button(window, text="University Level",command=university, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=800, height=50, width=600)

    Button(window, text="Others", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=900, height=50, width=600)



def university():

    borderFrame = Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow',
                        background='#131313',
                        highlightthickness=3)
    borderFrame.place(x=710, y=50)

    l1 = Label(window, text="M", fg='blue', bg='#131313', font=('SimSun', 65, 'bold'))
    l1.place(x=860, y=100)

    Label(window, text="C Q", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=950,
                                                                                           y=100)
    Label(window, text="Master", fg='white', bg='#131313', font=('SimSun', 50, 'bold')).place(x=1120,
                                                                                              y=200)

    Label(window, text="Online School Conception", fg='#5499C7', bg='#131313',
          font=('SimSun', 35, 'bold')).place(x=810,
                                             y=330)  # fg='#154360'

    Label(window, text="Which Course Do You Choose ?",
          fg='white', bg='#131313', font=('SimSun', 25, 'bold')).place(x=860,
                                                                       y=470)

    Button(window, text="Python Language",command=python, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=600, height=50, width=600)

    Button(window, text="Java Language", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=700, height=50, width=600)

    Button(window, text="Web Development", command=university, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=800, height=50, width=600)

    Button(window, text="Next Slide",command=next_slide, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=900, height=50, width=600)




def next_slide():

    borderFrame = Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow',
                        background='#131313',
                        highlightthickness=3)
    borderFrame.place(x=710, y=50)

    Button(window, text="C Language", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=100, height=50, width=600)

    Button(window, text="C++ Language", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=200, height=50, width=600)

    Button(window, text="C# language", command=university, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=300, height=50, width=600)

    Button(window, text="Information System", command=next_slide, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=400, height=50, width=600)

    Button(window, text="OOP Concept", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=500, height=50, width=600)

    Button(window, text="Advance Mathamatics", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=600, height=50, width=600)

    Button(window, text="Computer History",  fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=700, height=50, width=600)

    Button(window, text="Agro Technology",  fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=800, height=50, width=600)
    Button(window, text="Previous Slide", command=university, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=900, height=50, width=600)


def python():

    borderFrame = Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow',
                        background='#131313',
                        highlightthickness=3)
    borderFrame.place(x=710, y=50)

    l1 = Label(window, text="M", fg='blue', bg='#131313', font=('SimSun', 65, 'bold'))
    l1.place(x=860, y=100)

    Label(window, text="C Q", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=950,
                                                                                           y=100)
    Label(window, text="Master", fg='white', bg='#131313', font=('SimSun', 50, 'bold')).place(x=1120,
                                                                                              y=200)

    Label(window, text="Online School Conception", fg='#5499C7', bg='#131313',
          font=('SimSun', 35, 'bold')).place(x=810,
                                             y=330)  # fg='#154360'

    Label(window, text="Who Do You Choose ?",
          fg='white', bg='#131313', font=('SimSun', 25, 'bold')).place(x=950,
                                                                       y=470)

    Button(window, text="Teacher 1",command=teacher1_teacherside, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=600, height=50, width=600)

    Button(window, text="Teacher 2", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=700, height=50, width=600)

    Button(window, text="Teacher 3", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=800, height=50, width=600)

    Button(window, text="Previous Slide", command=university, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=810, y=900, height=50, width=600)








def teacher1_teacherside():

    def slider():
        global text, count

        if count == len(s):
            count = 0
            text = ''

        text = text + s[count]  # s
        sliderLabel.config(text=text)
        count += 1
        sliderLabel.after(500, slider)  # every 100s call slider()

    def clock():
        global date, currenttime

        date = time.strftime('%d/%m/%y')
        currenttime = time.strftime('%H:%M:%S')
        datetimeLabel.config(text=f'Date : {date}\nTime : {currenttime}')
        datetimeLabel.after(1000, clock)  # every 1000 second call clock function again again

    window.destroy()



    def update_student():

        def update_data():
            query = 'update quiz set question=%s or Answer=%s or comment=%s,date=%s,time=%s where id=%s'
            mycursor.execute(query, (questionEntry.get(), answerEntry.get(),commentEntry.get(), date, currenttime,idEntry.get()))
            con.commit()
            messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=update_window)
            update_window.destroy()
            show_student()

        update_window = Toplevel()
        update_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
        update_window.geometry('1360x900+500+130')
        update_window.title('Update Questions')
        update_window.resizable(0, 0)

        Label(update_window, text="Update Questions", fg='white', bg='black',  # 0B4DA0
              font=('SimSun', 15, 'bold')).place(x=10, y=30, width=1340, height=30)

        idLabel = Label(update_window, text='Question Number', font=('times new roman', 25, 'bold')).place(x=50, y=150)
        idEntry = Entry(update_window, font=('roman', 20, 'bold'), width=50)
        idEntry.place(x=500, y=150, width=200, height=50)

        questionLabel = Label(update_window, text='Question', font=('times new roman', 25, 'bold')).place(x=50, y=250)
        questionEntry = Entry(update_window, font=('roman', 20, 'bold'),
                              width=80)
        questionEntry.place(x=500, y=250, width=800, height=100)

        answerLabel = Label(update_window, text='Answer', font=('times new roman', 25, 'bold')).place(x=50, y=400)
        answerEntry = Entry(update_window, font=('roman', 20, 'bold'),
                            width=24)
        answerEntry.place(x=500, y=400, width=800, height=100)

        commentLabel = Label(update_window, text='Comment', font=('times new roman', 25, 'bold')).place(x=50, y=550)
        commentEntry = Entry(update_window, font=('roman', 20, 'bold'))
        commentEntry.place(x=500, y=550, width=800, height=50)

        add_student_button = Button(update_window, text='Update', fg='white', bg='black',  # 0B4DA0
                                    font=('SimSun', 15, 'bold'), command=update_data)
        add_student_button.place(x=500, y=750, width=400, height=50)



        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        questionEntry.insert(0, listdata[1])
        answerEntry.insert(0, listdata[2])
        commentEntry.insert(0, listdata[3])





    def show_student():
        query = 'select * from quiz'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)




    def delet_student():
        indexing = studentTable.focus()
        print(indexing)
        content = studentTable.item(indexing)
        content_id = content['values'][0]
        query = 'delete from quiz where id=%s'
        mycursor.execute(query, content_id)
        con.commit()
        messagebox.showinfo('Deleted', f'Id {content_id} is deleted succesfully')
        query = 'select * from quiz'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)



    def search_student():

        def search_data():
            query = 'select * from quiz where id=%s or question=%s or Answer=%s or comment=%s'
            mycursor.execute(query, (
                        idEntry.get(), questionEntry.get(), answerEntry.get(),commentEntry.get()))
            studentTable.delete(*studentTable.get_children())
            fetched_data = mycursor.fetchall()
            for data in fetched_data:
                studentTable.insert('', END, values=data)

        search_window = Toplevel()
        search_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
        search_window.geometry('1360x900+500+130')
        search_window.title('Search Questions')
        search_window.resizable(0, 0)

        Label(search_window, text="Search Your Questions", fg='white', bg='black',  # 0B4DA0
              font=('SimSun', 15, 'bold')).place(x=10, y=30, width=1340, height=30)

        idLabel = Label(search_window, text='Question Number', font=('times new roman', 25, 'bold')).place(x=50, y=150)
        idEntry = Entry(search_window, font=('roman', 20, 'bold'), width=50)
        idEntry.place(x=500, y=150, width=200, height=50)

        questionLabel = Label(search_window, text='Question', font=('times new roman', 25, 'bold')).place(x=50, y=250)
        questionEntry = Entry(search_window, font=('roman', 20, 'bold'),
                              width=80)
        questionEntry.place(x=500, y=250, width=800, height=100)

        answerLabel = Label(search_window, text='Answer', font=('times new roman', 25, 'bold')).place(x=50, y=400)
        answerEntry = Entry(search_window, font=('roman', 20, 'bold'),
                            width=24)
        answerEntry.place(x=500, y=400, width=800, height=100)

        commentLabel = Label(search_window, text='Comment', font=('times new roman', 25, 'bold')).place(x=50, y=550)
        commentEntry = Entry(search_window, font=('roman', 25, 'bold'))
        commentEntry.place(x=500, y=550, width=800, height=50)

        add_student_button = Button(search_window, text='Search', fg='white', bg='black',  # 0B4DA0
                                    font=('SimSun', 15, 'bold'), command=search_data)
        add_student_button.place(x=500, y=750, width=400, height=50)



    def add_student():
        def add_data():
            if idEntry.get() == '' or questionEntry.get() == '' or answerEntry.get() == '':
                messagebox.showerror('Error', 'All Feilds are required', parent=add_window)

            else:
                currentdate = time.strftime('%d/%m/%y')
                currenttime = time.strftime('%H:%M:%S')
                try:

                    query = 'insert into quiz values(%s,%s,%s,%s,%s,%s)'
                    mycursor.execute(query, (
                        idEntry.get(), questionEntry.get(), answerEntry.get(),commentEntry.get(), currentdate, currenttime))

                    con.commit()
                    result = messagebox.askyesno('Confirm', 'Data Added Successfully. Do You Want To Clean The Form?',
                                                 parent=add_window)
                    if result:
                        idEntry.delete(0, END)
                        questionEntry.delete(0, END)
                        answerEntry.delete(0, END)
                        commentEntry.delete(0, END)

                    else:
                        pass

                except:
                    messagebox.showerror('Error', 'Id cannot be repeated', parent=add_window)
                    return

                # show data student managemnet system window
                query = 'select *from quiz'
                mycursor.execute(query)
                fetched_data = mycursor.fetchall()
                studentTable.delete((*studentTable.get_children()))
                for data in fetched_data:
                    datalist = list(data)
                    studentTable.insert('', END, values=datalist)

        add_window = Toplevel()
        add_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
        add_window.geometry('1360x900+500+130')
        add_window.title('Add New Questions')
        add_window.resizable(0, 0)

        Label(add_window, text="Add New Questions", fg='white', bg='black',  # 0B4DA0
              font=('SimSun', 15, 'bold')).place(x=10, y=30, width=1340, height=30)

        # idLable = Label(add_window,text='Id',font=(''))
        idLabel = Label(add_window, text='Question Number', font=('times new roman', 25, 'bold')).place(x=50, y=150)
        #idLabel.grid(row=5, column=5, padx=30, pady=150, sticky=W)
        idEntry = Entry(add_window, font=('roman', 20, 'bold'), width=50)#.place(x=500, y=150, width=200, height=50)
        #idEntry.grid(row=5, column=6, pady=15, padx=10)
        idEntry.place(x=500, y=150, width=200, height=50)

        questionLabel = Label(add_window, text='Question', font=('times new roman', 25, 'bold')).place(x=50, y=250)
        #questionLabel.grid(row=6, column=5, padx=30, pady=15, sticky=W)
        questionEntry = Entry(add_window, font=('roman', 20, 'bold'), width=80)#.place(x=500, y=250, width=400, height=100)
        #questionEntry.grid(row=6, column=6, pady=15, padx=10)
        questionEntry.place(x=500, y=250, width=800, height=100)

        answerLabel = Label(add_window, text='Answer', font=('times new roman', 25, 'bold')).place(x=50, y=400)
        #answerLabel.grid(row=7, column=5, padx=30, pady=15, sticky=W)
        answerEntry = Entry(add_window, font=('roman', 20, 'bold'), width=24)#.place(x=500, y=350, width=500, height=80)
        #answerEntry.grid(row=7, column=6, pady=15, padx=10)
        answerEntry.place(x=500, y=400, width=800, height=100)

        commentLabel = Label(add_window, text='Comment', font=('times new roman', 25, 'bold')).place(x=50, y=550)
        #commentLabel.grid(row=8, column=5, padx=30, pady=15, sticky=W)
        commentEntry = Entry(add_window, font=('roman', 20, 'bold'))#.place(x=500, y=450, width=200, height=50)
        #commentEntry.grid(row=8, column=6, pady=15, padx=10)
        commentEntry.place(x=500, y=550, width=800, height=50)


        add_student_button = Button(add_window, text='ADD Question', fg='white', bg='black',  # 0B4DA0
              font=('SimSun', 15, 'bold'), command=add_data)
        add_student_button.place(x=500,y=750,width=400,height=50)



    def connect_database():

        def connect():
            global mycursor, con
            try:
                # con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
                con = pymysql.connect(host='localhost', user='root', password='1234')
                mycursor = con.cursor()
                messagebox.showinfo('Success', 'Database Connection is Success')
                # hostname=localhost

            except:
                messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
                return

            try:
                # create database
                query = 'create database questionsmanagementsystem'
                mycursor.execute(query)

                query = 'use questionsmanagementsystem'
                mycursor.execute(query)

                # create table
                # query = 'create table student(id int not null primary key,name varchar(30),mobile v'
                query = 'create table quiz(id int not null primary key, question varchar(500),Answer varchar(500),comment varchar(100),' \
                        'date varchar(50), time varchar(50))'
                mycursor.execute(query)

            except:
                query = 'use questionsmanagementsystem'
                mycursor.execute(query)

            messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
            connectWindow.destroy()
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            updatestudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            exportstudentButton.config(state=NORMAL)
            deletstudentButton.config(state=NORMAL)

        connectWindow = Toplevel()
        connectWindow.geometry('470x250+1415+125')
        connectWindow.title('Database Connection')
        connectWindow.resizable(0, 0)

        # hostnameLabale = Label(connectWindow,text='Host Name',font=('times new roman',20,'bold'))
        # hostnameLabale.grid(row=0,column=0)
        # 717D7E

        hostnameLabel = Label(connectWindow, text='Host Name', fg='#B1B0B0', font=('arial', 20, 'bold'))
        hostnameLabel.grid(row=0, column=0, padx=20)

        hostEntry = Entry(connectWindow, fg='#717D7E', font=('roman', 15, 'bold'), bd=0)
        hostEntry.grid(row=0, column=1, padx=40, pady=20)

        usernameLabel = Label(connectWindow, text='User Name', fg='#B1B0B0', font=('arial', 20, 'bold'))
        usernameLabel.grid(row=1, column=0, padx=20)

        usernameEntry = Entry(connectWindow, fg='#717D7E', font=('roman', 15, 'bold'), bd=0)
        usernameEntry.grid(row=1, column=1, padx=40, pady=20)

        passwordLabel = Label(connectWindow, text='Password', fg='#B1B0B0', font=('arial', 20, 'bold'))
        passwordLabel.grid(row=2, column=0, padx=20)

        passwordEntry = Entry(connectWindow, fg='#F1EAEA', font=('roman', 15, 'bold'), bd=0)
        passwordEntry.grid(row=2, column=1, padx=40, pady=20)

        connectButton = ttk.Button(connectWindow, text='CONNECT', width=20, command=connect)
        connectButton.grid(row=3, columnspan=2)


    root = ttkthemes.ThemedTk()
    root.get_themes()
    root.set_theme('elegance')

    root.geometry('1920x1080+0+0')
    root.title('Online School Work Board')
    root.resizable(0, 0)

    # date time show
    datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
    datetimeLabel.place(x=20, y=30)
    clock()

    # Animation
    s = 'Work Bord'
    sliderLabel = Label(root,text='Work Board', font=('times new roman', 28, 'bold'), width=30)
    sliderLabel.place(x=650, y=30)
    #slider()

    connectButton = ttk.Button(root, text='Connect Database', width=30,
                               command=connect_database)  # ,bd=0,bg='blue',fg='white',font=('times new roman',18,'bold'))
    connectButton.place(x=1650, y=50)

    # left Frame
    leftFrame = Frame(root)
    leftFrame.place(x=50, y=130, width=500, height=900)

    # logo_image = PhotoImage(file='student (1).png')
    # logo_Label = Label(leftFrame,image=logo_image)
    # logo_Label.grid(row=0,column=0,padx=120,pady=50)

    addstudentButton = ttk.Button(leftFrame, text='Add Questions', width=50, state=DISABLED,command=add_student)
                                  #command=add_student)  # state=DISABLED
    addstudentButton.grid(row=1, column=0, pady=25, padx=10)

    searchstudentButton = ttk.Button(leftFrame, text='Search Questions', width=50, state=DISABLED,command=search_student)
    searchstudentButton.grid(row=2, column=0, pady=25, padx=10)

    deletstudentButton = ttk.Button(leftFrame, text='Delete Questions', width=50, state=DISABLED,command=delet_student)
    deletstudentButton.grid(row=3, column=0, pady=25, padx=10)

    updatestudentButton = ttk.Button(leftFrame, text='Update Questions', width=50,  state=DISABLED,command=update_student)
    updatestudentButton.grid(row=4, column=0, pady=25, padx=10)

    showstudentButton = ttk.Button(leftFrame, text='Show Questions', width=50, state=DISABLED,command=show_student)
    showstudentButton.grid(row=5, column=0, pady=25, padx=10)

    exportstudentButton = ttk.Button(leftFrame, text='Export Questions', width=50, state=DISABLED)
    exportstudentButton.grid(row=6, column=0, pady=25, padx=10)

    exitButton = ttk.Button(leftFrame, text='Exit', width=50)
    exitButton.grid(row=7, column=0, pady=150, padx=10)

#padx=120
    # teacherButton.grid(row=8,column=0,pady=25,padx=120)

    # right Frame
    rightFrame = Frame(root)
    rightFrame.place(x=500, y=130, width=1360, height=900)

    scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
    scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

    studentTable = ttk.Treeview(rightFrame, columns=(
    'Question Id', 'Question', 'Answer','Comment', 'Added Date', 'Added Time'),
                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM, fill=X)
    scrollBarY.pack(side=RIGHT, fill=Y)

    studentTable.pack(fill=BOTH, expand=1)

    # student table heding
    studentTable.heading('Question Id', text='Question Num')
    studentTable.heading('Question', text='Questions')
    studentTable.heading('Answer', text='Answers')
    studentTable.heading('Comment',text='Comment')
    studentTable.heading('Added Date', text='Added Date')
    studentTable.heading('Added Time', text='Added Time')

    # student table heading font size and bolt

    studentTable.column('Question Id', width=200, anchor=CENTER)
    studentTable.column('Question', width=1140, anchor=CENTER)
    studentTable.column('Answer', width=1000, anchor=CENTER)
    studentTable.column('Comment',width=500, anchor=CENTER)
    studentTable.column('Added Date', width=200, anchor=CENTER)
    studentTable.column('Added Time', width=200, anchor=CENTER)

    style = ttk.Style()

    style.configure('Treeview', rowheight=40, font=('arial', 15, 'bold'), fieldbackground='white', background='white', )
    style.configure('Treeview.Heading', font=('arial', 18, 'bold'), foreground='blue')

    # heding show
    studentTable.config(show='headings')






menu()
window.mainloop()