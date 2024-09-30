from tkinter import  *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector



APP = Tk()
APP.geometry('1920x1080+0+0')
APP.configure(bg="#fff")
APP.title('M C Q  Master APP Teachers Side')
APP.resizable(False,False)


def online_school():
    APP.destroy()
    import online_school

def menu():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1200, y=80)

    Label(mainF, text="Teacher's  Side", fg='white', bg='black', font=('SimSun', 15, 'bold')).place(x=2,y=20,width=1908,height=30)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                         y=250)

    Label(mainF, text="C Q", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                                                  y=250)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,
                                                                                        y=350)
    Label(mainF, text="Choose the right theme for education.", fg='#154360', bg='white', font=('SimSun', 35, 'bold')).place(x=50,
                                                                                           y=600)

    Label(mainF, text="Any successful career starts with good education. Together with us you will have deeper  ", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=700)
    Label(mainF, text="knowledge of the subjects that will be espectally useful for you when climbing the", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=730)
    Label(mainF, text="career ladder. joing with MCQ master.", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=760)



    Button(mainF, text='Sign in',command=signin, fg='white', bg='black', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1200, y=700, height=50, width=500)
    Button(mainF, text='Register',command=register,fg='white', bg='black', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1200, y=800, height=50, width=500)

    #Button(mainF, text='☰', fg='black', bg='white', border=0, activebackground='white',
           #activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    #img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    #l = Label(mainF, image=img)
    #l.img = img
    #l.place(height=50, width=50, x=1860, y=19)



def login():

    if e_1.get() == '' or e_2.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif e_1.get() == 'sineth' and e_2.get() == '201222':
        messagebox.showinfo('Success', 'Welcome')
        #APP.destroy()
        online_school()

    else:
        messagebox.showerror('Error', 'Please enter correct credentials')






def signin():
    global e_1,e_2
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1100, y=380)

    Frame(mainF, width=750, height=600, highlightbackground='black', highlightcolor='yellow', background='white',
          highlightthickness=3).place(x=100,
                                      y=300)

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                         y=50)

    Label(mainF, text="C Q", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                                                  y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                        y=150)
    Label(mainF, text="teacher's  Loging Site", fg='white', bg='black',#0B4DA0
          font=('SimSun', 15, 'bold')).place(x=1000, y=250,width=700,height=30)
    Label(mainF, text="Sign in", fg='black',bg='white', border=0,
           font=('SimSun', 25, 'bold')).place(x=400, y=350)


    def on_enter(e):
        e_1.delete(0,'end')

    def on_leave(e):
        name=e_1.get()
        if name=='' :
            e_1.insert(0,'User Name')

    e_1 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_1.place(width=550, height=50, x=200, y=425)
    e_1.insert(0, 'User Name')
    e_1.bind('<FocusIn>',on_enter)
    e_1.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_2.delete(0,'end')

    def on_leave(e):
        password=e_2.get()
        if password=='' :
            e_2.insert(0,'Password')

    e_2 = Entry(mainF,  border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_2.place(width=550, height=50, x=200, y=500)
    e_2.insert(0, 'Password')
    e_2.bind('<FocusIn>', on_enter)
    e_2.bind('<FocusOut>', on_leave)

    Button(mainF, text='Sign in',command=login, fg='white', bg='black', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=650, height=50, width=550)

    Checkbutton(mainF, text='Remember Password', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=580, height=50, width=550)

    Label(mainF, text="Don't you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=280, y=750)
    Button(mainF, text='Sign up',command=register, fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=750)


def register():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1100, y=380)





    Frame(mainF,width=750,height=650,highlightbackground='black',highlightcolor='yellow',background='white',highlightthickness=3).place(x=100,
                                                                                         y=250)

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                         y=50)

    Label(mainF, text="C Q", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                                                  y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                        y=150)
    #Label(mainF, text="Available Courses", fg='#EF930C', bg='white',
          #font=('SimSun', 20, 'bold')).place(x=300,

                                             #y=250)
    Label(mainF, text="Teacher's  Loging Site", fg='white', bg='black',
          font=('SimSun', 15, 'bold')).place(x=1000, y=250, width=700, height=30)

    Label(mainF, text="Register", fg='black',bg='white', border=0,
           font=('SimSun', 25, 'bold')).place(x=400, y=275)


    def on_enter(e):
        e_1.delete(0,'end')

    def on_leave(e):
        name=e_1.get()
        if name=='' :
            e_1.insert(0,'User Name')

    e_1 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_1.place(width=550, height=50, x=200, y=350)
    e_1.insert(0, 'User Name')
    e_1.bind('<FocusIn>',on_enter)
    e_1.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_3.delete(0,'end')

    def on_leave(e):
        email=e_3.get()
        if email=='' :
            e_3.insert(0,'Email')

    e_3 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_3.place(width=550, height=50, x=200, y=425)
    e_3.insert(0, 'Email')
    e_3.bind('<FocusIn>',on_enter)
    e_3.bind('<FocusOut>',on_leave)


    def on_enter(e):
        e_2.delete(0,'end')

    def on_leave(e):
        password=e_2.get()
        if password=='' :
            e_2.insert(0,'Password')

    e_2 = Entry(mainF,  border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_2.place(width=550, height=50, x=200, y=500)
    e_2.insert(0, 'Password')
    e_2.bind('<FocusIn>', on_enter)
    e_2.bind('<FocusOut>', on_leave)


    def on_enter(e):
        e_4.delete(0,'end')

    def on_leave(e):
        cmps=e_4.get()
        if cmps=='' :
            e_4.insert(0,'Conform Password')

    e_4 = Entry(mainF, border=0, bg='#dddddd', fg='#929292',font=('SimSun', 13))
    e_4.place(width=550, height=50, x=200, y=575)
    e_4.insert(0, 'Conform Password')
    e_4.bind('<FocusIn>',on_enter)
    e_4.bind('<FocusOut>',on_leave)

    Button(mainF, text='Register',command=signin, fg='white', bg='black', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=725, height=50, width=550)

    Checkbutton(mainF, text='Agree our term and conditions', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=655, height=50, width=550)

    Label(mainF, text="Do you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=300, y=825)
    Button(mainF, text='Login Here',command=signin , fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=825)







#def show():

   # def search_data():
        #query = 'select * from student where id=%s'
        #cursor.execute(query, (
        #idEntry.get()))
        #studentTable.delete(*studentTable.get_children())
        #fetched_data = cursor.fetchall()
        #for data in fetched_data:
         #   studentTable.insert('', END, values=data)


    #search_window = Toplevel()
    #search_window.grab_set()  # other button click but not close this window grab_set(),first close this window next we can close other windows,other buttons not working
    #search_window.geometry('500x540+100+500')
    #search_window.title('Search Teacher')
    #search_window.resizable(0, 0)

    # idLable = Label(search_window,text='Id',font=(''))
    #idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    #idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    #idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    #idEntry.grid(row=0, column=1, pady=15, padx=10)

    #search_student_button = ttk.Button(search_window, text='SEARCH', width=20, command=search_data)
    #search_student_button.grid(row=7, columnspan=2, pady=15)






    # right Frame
    #rightFrame = Frame(root)
    #rightFrame.place(x=700, y=130, width=1200, height=900)

    #scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
    #scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

    #studentTable = ttk.Treeview(rightFrame, columns=(
    #'Id', 'Name', 'Email', 'Mobile No', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
    #                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

    #scrollBarX.config(command=studentTable.xview)
    #scrollBarY.config(command=studentTable.yview)

    #scrollBarX.pack(side=BOTTOM, fill=X)
    #scrollBarY.pack(side=RIGHT, fill=Y)

    #studentTable.pack(fill=BOTH, expand=1)

    # Create a connection to the MySQL database
    #conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="questions")

    # Create a cursor object
    #cursor = conn.cursor()

    #indexing = studentTable.focus()
    #print(indexing)
    #content = studentTable.item(indexing)
    #content['values'][0]
    #query = 'select * from question'
    #cursor.execute(query)
    #fetched_data = cursor.fetchall()
    #studentTable.delete(*studentTable.get_children())
    #for data in fetched_data:
    #    studentTable.insert('', END, values=data)



# Define the function to add the question to the database
#def add_question():
 ##  question_id = questionid_entry.get()
   # question = question_entry.get()
    #answer = answer_entry.get()

    # Insert the question into the database
#    cursor.execute("INSERT INTO questions (question_id, question, answer) VALUES (%s, %s, %s)", (question_id, question, answer))
 #   conn.commit()

    # Clear the entry widgets
  #  questionid_entry.delete(0, tk.END)
   # question_entry.delete(0, tk.END)
    #answer_entry.delete(0, tk.END)



# Create a connection to the MySQL database
#conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="questions")

# Create a cursor object
#cursor = conn.cursor()

# Create a window
#root = tk.Tk()
#root.title("Questions")



# Create labels and entry widgets
#questionid_label = tk.Label(root, text="Question Id:")
#questionid_entry = tk.Entry(root)
#question_label = tk.Label(root, text="Question:")
#question_entry = tk.Entry(root)
#answer_label = tk.Label(root, text="Answer:")
#answer_entry = tk.Entry(root)

# Create a button to add the question to the database
#add_button = tk.Button(root, text="Add Question", command=add_question)
#show_button = tk.Button(root, text="show Question", command=show)

# Pack the widgets
#questionid_label.pack()
#questionid_entry.pack()
#question_label.pack()
#question_entry.pack()
#answer_label.pack()
#answer_entry.pack()
#add_button.pack()
#show_button.pack()





menu()
APP.mainloop()