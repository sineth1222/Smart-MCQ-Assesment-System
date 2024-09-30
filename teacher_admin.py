from tkinter import  *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
import mysql.connector

def teacher_side():
    root.destroy()
    import teacher



def show():
    # Create a connection to the MySQL database
    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="teachermanagementsystem")

    # Create a cursor object
    cursor = conn.cursor()


    def search_data():
        query = 'select * from student where id=%s'
        cursor.execute(query, (
            idEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = cursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
    search_window.geometry('500x540+100+500')
    search_window.title('Search Teacher')
    search_window.resizable(0, 0)

    # idLable = Label(search_window,text='Id',font=(''))
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH', width=20, command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)



    # right Frame
    rightFrame = Frame(root)
    rightFrame.place(x=700, y=130, width=1200, height=900)

    scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
    scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

    studentTable = ttk.Treeview(rightFrame, columns=(
    'Id', 'Name', 'Email', 'Mobile No', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                                xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

    scrollBarX.config(command=studentTable.xview)
    scrollBarY.config(command=studentTable.yview)

    scrollBarX.pack(side=BOTTOM, fill=X)
    scrollBarY.pack(side=RIGHT, fill=Y)

    studentTable.pack(fill=BOTH, expand=1)

    # Create a connection to the MySQL database
    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="teachermanagementsystem")

    # Create a cursor object
    cursor = conn.cursor()




def update_student():

    def update_data():
        query = 'update student set name=%s,subject=%s,email=%s,subcategory=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                                 genderEntry.get(), dobEntry.get(), date, currenttime, idEntry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
    update_window.geometry('500x540+100+30')
    update_window.title('Update Teacher')
    update_window.resizable(0, 0)

    # idLable = Label(update_window,text='Id',font=(''))
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Subject', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Sub Categary', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='Special Note', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(update_window, text='UPDATE', width=20,command=update_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)

    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    phoneEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addressEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])


def show_student():
    query = 'select * from student'
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
    query = 'delete from student where id=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted succesfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def search_student():

    def search_data():
        query = 'select * from student where id=%s or name=%s or email=%s or subject=%s or subcategory=%s or gender=%s or dob=%s'
        mycursor.execute(query, (
        idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), addressEntry.get(), genderEntry.get(),
        dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)



    search_window = Toplevel()
    search_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
    search_window.geometry('500x540+100+500')
    search_window.title('Search Teacher')
    search_window.resizable(0, 0)

    # idLable = Label(search_window,text='Id',font=(''))
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Subject', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Sub categary', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='Special Note', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH', width=20,command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All Feilds are required', parent=search_window)

        else:
            currentdate = time.strftime('%d/%m/%y')
            currenttime = time.strftime('%H:%M:%S')
            try:

                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                genderEntry.get(), dobEntry.get(), currentdate, currenttime))

                con.commit()
                result = messagebox.askyesno('Confirm', 'Data Added Successfully. Do You Want To Clean The Form?',
                                             parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    phoneEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)

                else:
                    pass

            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
                return


            #show data student managemnet system window
            query = 'select *from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete((*studentTable.get_children()))
            for data in fetched_data:
                datalist = list(data)
                studentTable.insert('',END,values=datalist)


    add_window = Toplevel()
    add_window.grab_set()#other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
    add_window.geometry('500x550+100+410')
    add_window.title('Add New Teacher')
    add_window.resizable(0, 0)

    #idLable = Label(add_window,text='Id',font=(''))
    idLabel = Label(add_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Subject', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Sub Categary', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='Special Note', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button = ttk.Button(add_window, text='ADD Teacher',width=20,command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)


#database button connect
def connect_database():

    def connect():
        global mycursor,con
        try:
            #con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            messagebox.showinfo('Success','Database Connection is Success')
            #hostname=localhost

        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return


        try:
            # create database
            query = 'create database teachermanagementsystem'
            mycursor.execute(query)

            query = 'use teachermanagementsystem'
            mycursor.execute(query)

            # create table
            # query = 'create table student(id int not null primary key,name varchar(30),mobile v'
            query = 'create table student(id int not null primary key, name varchar(30),subject varchar(100),email varchar(50),' \
                    'subcategory varchar(50),gender varchar(20),dob varchar(30),date varchar(50), time varchar(50))'
            mycursor.execute(query)

        except:
            query = 'use teachermanagementsystem'
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
    connectWindow.resizable(0,0)

    #hostnameLabale = Label(connectWindow,text='Host Name',font=('times new roman',20,'bold'))
    #hostnameLabale.grid(row=0,column=0)
    # 717D7E

    hostnameLabel = Label(connectWindow, text='Host Name',fg='#B1B0B0', font=('arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(connectWindow,fg='#717D7E', font=('roman', 15, 'bold'), bd=0)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text='User Name',fg='#B1B0B0', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow,fg='#717D7E', font=('roman', 15, 'bold'), bd=0)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password',fg='#B1B0B0', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow,fg='#F1EAEA', font=('roman', 15, 'bold'), bd=0)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT',width=20,command=connect)
    connectButton.grid(row=3, columnspan=2)


#@Animation
count=0
text=''
def slider():
    global text,count

    if count == len(s):
        count = 0
        text = ''

    text = text+s[count]  #s
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(500,slider)#every 100s call slider()



#@date time show
def clock():

    global date,currenttime

    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date : {date}\nTime : {currenttime}')
    datetimeLabel.after(1000,clock)#every 1000 second call clock function again again


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('elegance')

root.geometry('1920x1080+0+0')
root.title('Teacher Admin')
root.resizable(0,0)

#date time show
datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=20,y=30)
clock()


#Animation
s='Teacher Admin'
sliderLabel = Label(root,font=('times new roman',28,'bold'),width=30)
sliderLabel.place(x=650,y=50)
#slider()


connectButton = ttk.Button(root,text='Connect Database',width=30,command=connect_database)#,bd=0,bg='blue',fg='white',font=('times new roman',18,'bold'))
connectButton.place(x=1650,y=50)


#left Frame
leftFrame = Frame(root)
leftFrame.place(x=50,y=130,width=500,height=900)


#logo_image = PhotoImage(file='student (1).png')
#logo_Label = Label(leftFrame,image=logo_image)
#logo_Label.grid(row=0,column=0,padx=120,pady=50)

addstudentButton = ttk.Button(leftFrame,text='Add Teacher',width=50,state=DISABLED,command=add_student)#state=DISABLED
addstudentButton.grid(row=1,column=0,pady=25,padx=120)

searchstudentButton = ttk.Button(leftFrame,text='Search Teacher',width=50,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=25,padx=120)

deletstudentButton = ttk.Button(leftFrame,text='Delete Teacher',width=50,state=DISABLED,command=delet_student)
deletstudentButton.grid(row=3,column=0,pady=25,padx=120)

updatestudentButton = ttk.Button(leftFrame,text='Update Teacher',width=50,command=update_student,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=25,padx=120)

showstudentButton = ttk.Button(leftFrame,text='Show Teacher',width=50,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=25,padx=120)

exportstudentButton = ttk.Button(leftFrame,text='Export Data',width=50,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=25,padx=120)

exitButton = ttk.Button(leftFrame,text='Exit',width=50)
exitButton.grid(row=7,column=0,pady=25,padx=120)

teacherButton = Button(leftFrame,command=teacher_side, text="Teacher's Side", fg='white', bg='#131313', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=70, y=650, height=40, width=400)
#teacherButton.grid(row=8,column=0,pady=25,padx=120)

#right Frame
rightFrame = Frame(root)
rightFrame.place(x=700,y=130,width=1200,height=900)

scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,columns=('Id','Name','Email','Mobile No','Address','Gender','D.O.B','Added Date','Added Time'),
                            xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)


#student table heding
studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Subject Name')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Subject Categary')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='Specical Note')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

#student table heading font size and bolt

studentTable.column('Id',width=200,anchor=CENTER)
studentTable.column('Name',width=350,anchor=CENTER)
studentTable.column('Email',width=400,anchor=CENTER)
studentTable.column('Mobile No',width=450,anchor=CENTER)
studentTable.column('Address',width=350,anchor=CENTER)
studentTable.column('Gender',width=120,anchor=CENTER)
studentTable.column('D.O.B',width=200,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='blue')

#heding show
studentTable.config(show='headings')


root.mainloop()