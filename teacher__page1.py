from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import ImageTk




def teacherSide():
        window.destroy()
        import teacher


def teacherAdmin():
    window.destroy()
    import teacher_admin



window = Tk()

window.geometry('1920x1080+0+0')
window.title('M C Q  Master APP Teacher Side')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='teacher_home.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0,height=1080,width=1920)


def menu():
    #loginFrame = Frame(window, bg='#131313', bd=0)
    #loginFrame.place(x=1050,y=50, width=800, height=950)  # 1300x,550y

    borderFrame=Frame(window, width=800, height=950, highlightbackground='gold', highlightcolor='yellow', background='#131313',
          highlightthickness=3)
    borderFrame.place(x=1050,y=50)

    l1 = Label(window, text="M", fg='blue', bg='#131313', font=('SimSun', 65, 'bold'))
    l1.place(x=1200, y=100)

    Label(window, text="C Q", fg='white', bg='#131313', font=('SimSun', 65, 'bold')).place(x=1290,
                                                                                             y=100)
    Label(window, text="Master", fg='white', bg='#131313', font=('SimSun', 50, 'bold')).place(x=1460,
                                                                                                y=200)

    Label(window, text="Choose the right theme for education.", fg='white', bg='#131313',
          font=('SimSun', 25, 'bold')).place(x=1110,
                                             y=350)#fg='#154360'

    Label(window, text="Any successful career starts with good education. Together with ",
          fg='#5499C7', bg='#131313', font=('SimSun', 15, 'bold')).place(x=1110,
                                                                       y=450)
    Label(window, text="us you will have deeper knowledge of the subjects that will ",
          fg='#5499C7', bg='#131313', font=('SimSun', 15, 'bold')).place(x=1110,
                                                                       y=480)
    Label(window, text="be espectally useful for you when climbing thecareer ladder.", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=1110,
                                             y=510)

    Label(window, text="joing with MCQ master.",
          fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=1110,
                                             y=540)

    Button(window,command=teacherAdmin, text="Teacher's Admin", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1150, y=700, height=50, width=600)

    Button(window,command=teacherSide, text="Teachers's Side", fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1150, y=800, height=50, width=600)

menu()
window.mainloop()