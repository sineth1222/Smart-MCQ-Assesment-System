from tkinter import *
from tkinter.messagebox import askyesno

import tkinter as tk

from tkinter import StringVar

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os


APP = Tk()
APP.geometry('1920x1080+0+0')
APP.configure(bg="#fff")
APP.title('M C Q  Master APP Student Side')
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

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                         y=100)

    Label(mainF, text="C Q", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                                                  y=100)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,
                                                                                        y=200)
    Label(mainF, text="Choose the right theme for education.", fg='#154360', bg='white', font=('SimSun', 35, 'bold')).place(x=50,
                                                                                           y=400)

    Label(mainF, text="Any successful career starts with good education. Together with us you will have deeper  ", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=500)
    Label(mainF, text="knowledge of the subjects that will be espectally useful for you when climbing the", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=530)
    Label(mainF, text="career ladder. joing with MCQ master.", fg='#5499C7', bg='white', font=('SimSun', 15, 'bold')).place(x=50,
                                                                                         y=560)

    Button(mainF, text='Available Courses',command=av_cours , fg='white', bg='#EF930C', border=0, activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=200, y=750, height=50, width=500)

    Button(mainF, text='Sign in',command=signin, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1200, y=700, height=50, width=500)
    Button(mainF, text='Register',command=register, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=1200, y=800, height=50, width=500)

    Button(mainF, text='☰',command=toggle_win_menu, fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)



def exit():
    ans = askyesno(title='Exit', message='Do You Want Exit ?')
    if ans:
        APP.destroy()

#menubar
def toggle_win_menu():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',None)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #


def av_cours():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1200, y=80)

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
    Label(mainF, text='Available Courses', fg='white', bg='#EF930C', border=0,
           font=('SimSun', 18, 'bold')).place(x=10, y=250, height=30, width=960)


    Label(mainF, text="For O\L Student.", fg='#154360', bg='white',
          font=('SimSun', 18, 'bold')).place(x=50,
                                             y=300)
    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=205, height=1,x=50, y=328)
    Label(mainF, text="1.Sinhala", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=335)
    Label(mainF, text="2.Mathamatics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=365)
    Label(mainF, text="3.English", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=395)
    Label(mainF, text="4.ICT", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=425)
    Label(mainF, text="5.Tamil", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=455)
    Label(mainF, text="6.Science", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=485)
    Label(mainF, text="7.History", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=515)

    Label(mainF, text="For A\L Student.", fg='#154360', bg='white',
          font=('SimSun', 18, 'bold')).place(x=50,
                                             y=550)
    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=205, height=1, x=50, y=578)
    Label(mainF, text="1.Chemistry", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=585)
    Label(mainF, text="2.Physics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=615)
    Label(mainF, text="3.Combine Mathamatics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=645)
    Label(mainF, text="4.Biology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=675)
    Label(mainF, text="5.Agriculture", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=705)
    Label(mainF, text="6.Bio Systerm Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=735)
    Label(mainF, text="7.Science for Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=765)
    Label(mainF, text="8.Agro Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=795)
    Label(mainF, text="9.Engineering Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=825)
    Label(mainF, text="10.Information & Communication", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=855)
    Label(mainF, text="Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=885)
    Label(mainF, text="11.Accounting", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=300)
    Label(mainF, text="12.Business", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=330)
    Label(mainF, text="13.Economics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=360)
    Label(mainF, text="14.Sinhala", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=390)
    Label(mainF, text="15.Tamil", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=420)
    Label(mainF, text="16.History", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=450)
    Label(mainF, text="17.Art", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=480)
    Label(mainF, text="18.Dance", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=510)
    Label(mainF, text="19.Music", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=540)
    Label(mainF, text="20.Communication & Media", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=570)

    Label(mainF, text="For Uni Student.", fg='#154360', bg='white',
          font=('SimSun', 18, 'bold')).place(x=600,
                                             y=605)
    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=205, height=1, x=600, y=633)
    Label(mainF, text="1.Advance Mathamatics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=645)
    Label(mainF, text="2.Phython Language", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=675)
    Label(mainF, text="3.Java Language", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=705)
    Label(mainF, text="4.C Language", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=735)
    Label(mainF, text="5.C++ Language", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=765)
    Label(mainF, text="6.C# Language", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=795)
    Label(mainF, text="7.Web Development (HTML , CSS & java Script)", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=825)
    Label(mainF, text="8.Information System", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=855)
    Label(mainF, text="9.OOP Concept", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=885)

    Button(mainF, text='previous',command=menu, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1200, y=700, height=50, width=500)
    Button(mainF, text='Next',command=av_cours_next, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1200, y=800, height=50, width=500)

    Button(mainF, text='☰',command=toggle_win_av_cors,  fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)


def toggle_win_av_cors():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=av_cours, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=av_cours, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',None)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #


def av_cours_next():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1200, y=80)

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
    Label(mainF, text='Available Courses', fg='white', bg='#EF930C', border=0,
           font=('SimSun', 18, 'bold')).place(x=10, y=250, height=30, width=960)

    Label(mainF, text="For Uni Student.", fg='#154360', bg='white',
          font=('SimSun', 18, 'bold')).place(x=50,
                                             y=300)
    Label(mainF, fg='#524F4E', bg='#524F4E').place(width=205, height=1, x=50, y=328)
    Label(mainF, text="10.APP Development", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=335)
    Label(mainF, text="11.Higher Mathamatics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=365)
    Label(mainF, text="12.Advance English", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=395)
    Label(mainF, text="13.Information Security", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=425)
    Label(mainF, text="14.Tamil for Beginer", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=455)
    Label(mainF, text="15.Science ", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=485)
    Label(mainF, text="16.Computer History", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=515)
    Label(mainF, text="17.Biology for Life", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=545)
    Label(mainF, text="18.Agriculture", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=575)
    Label(mainF, text="19.Robbot Systerm Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=605)
    Label(mainF, text="20.Macanic Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=635)
    Label(mainF, text="21.Biology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=675)
    Label(mainF, text="22.Agriculture", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=705)
    Label(mainF, text="23.Bio Systerm Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=735)
    Label(mainF, text="24.Science for Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=765)
    Label(mainF, text="25.Agro Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=795)
    Label(mainF, text="26.Engineering Technology", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=825)
    Label(mainF, text="27.Information & Communication", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=80,
                                             y=855)
    Label(mainF, text="28.Accounting", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=300)
    Label(mainF, text="29.Business", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=330)
    Label(mainF, text="30.Economics", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=360)
    Label(mainF, text="31.Sinhala", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=390)
    Label(mainF, text="32.Tamil", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=420)
    Label(mainF, text="33.History", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=450)
    Label(mainF, text="34.Art", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=480)
    Label(mainF, text="35.Dance", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=510)
    Label(mainF, text="36.Music", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=540)
    Label(mainF, text="37.Communication & Media", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=650,
                                             y=570)

    Button(mainF, text='previous', command=av_cours, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1200, y=700, height=50, width=500)
    Button(mainF, text='Loging', command=menu, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=1200, y=800, height=50, width=500)

    Button(mainF, text='☰',command=toggle_win_av_cors_next,  fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)

def toggle_win_av_cors_next():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=av_cours_next, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=av_cours_next, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',None)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #


def login():

    if e_1.get() == '' or e_2.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif e_1.get() == 'sineth' and e_2.get() == '201222':
        messagebox.showinfo('Success', 'Welcome')
        #APP.destroy()
        page1()

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

    Frame(mainF, width=750, height=600, highlightbackground='blue', highlightcolor='yellow', background='white',
          highlightthickness=3).place(x=100,
                                      y=300)

    #Label(mainF, text="M C Q", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,y=100)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                         y=50)

    Label(mainF, text="C Q", fg='black',bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                                                  y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                        y=150)
    Label(mainF, text="Student Loging Site", fg='white', bg='#0B4DA0',
          font=('SimSun', 15, 'bold')).place(x=1000, y=250,width=700,height=30)
    Label(mainF, text="Sign in", fg='blue',bg='white', border=0,
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

    Button(mainF, text='Sign in',command=login, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=650, height=50, width=550)

    Checkbutton(mainF, text='Remember Password', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=580, height=50, width=550)

    Label(mainF, text="Don't you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=280, y=750)
    Button(mainF, text='Sign up',command=register, fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=750)

    Button(mainF, text='☰', command=toggle_win_singin, fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)


def toggle_win_singin():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=signin, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',menu)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #



def register():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("login.png").resize((500, 500)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=500, width=500, x=1100, y=380)





    Frame(mainF,width=750,height=650,highlightbackground='blue',highlightcolor='yellow',background='white',highlightthickness=3).place(x=100,
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
    Label(mainF, text="Student Loging Site", fg='white', bg='#0B4DA0',
          font=('SimSun', 15, 'bold')).place(x=1000, y=250, width=700, height=30)

    Label(mainF, text="Register", fg='blue',bg='white', border=0,
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

    Button(mainF, text='Register',command=signin, fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 18, 'bold')).place(x=200, y=725, height=50, width=550)

    Checkbutton(mainF, text='Agree our term and conditions', fg='black', bg='white', border=0, activebackground='white',
           font=('SimSun', 15)).place(x=200, y=655, height=50, width=550)

    Label(mainF, text="Do you have an account ?", fg='black', bg='white', border=0,
          font=('SimSun', 15)).place(x=300, y=825)
    Button(mainF, text='Login Here',command=signin , fg='blue', bg='white', border=0,activebackground='white',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=550, y=825)

    Button(mainF, text='☰',command=toggle_win_register, fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)


def toggle_win_register():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=register, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',menu)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #


def page1():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("png-transparent-abstract-background-technology-hexagonal-pattern.png").resize((850,1080)))
    l = Label(mainF, image=img )
    l.img = img
    l.place(height=1080, width=850, x=0, y=0)

    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                     y=50)

    Label(mainF, text="C Q", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                        y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                       y=150)

    borderFrame = Frame(mainF, width=600, height=580, highlightbackground='gold', highlightcolor='yellow',
                        background='#131313',
                        highlightthickness=3)
    borderFrame.place(x=100, y=350)

    #l1 = Label(window, text="M", fg='blue', bg='#131313', font=('SimSun', 65, 'bold'))
    #l1.place(x=1200, y=100)

    Label(mainF, text="O", fg='white', bg='#131313', font=('SimSun', 45, 'bold')).place(x=190,
                                                                                     y=400)

    Label(mainF, text="nline", fg='white', bg='#131313', font=('SimSun', 35, 'bold')).place(x=230,
                                                                                           y=410)
    Label(mainF, text="School", fg='white', bg='#131313', font=('SimSun', 35, 'bold')).place(x=400,
                                                                                              y=410)

    Label(mainF, text="This will enable you to carry out the activities ", fg='#5499C7', bg='#131313',font=('SimSun', 15, 'bold')).place(x=120,y=510)
    Label(mainF, text="assigned by your teacher. understand the difference", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=120, y=540)
    Label(mainF, text="together with the ", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=120, y=570)
    Label(mainF, text="Online School", fg='white', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=320, y=570)
    Label(mainF, text="Created using ", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=480, y=570)
    Label(mainF, text="the modern education System The online learning ", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=120, y=600)
    Label(mainF, text="platform.", fg='#5499C7', bg='#131313',
          font=('SimSun', 15, 'bold')).place(x=120, y=630)

    Button(mainF,  text="Meet Your Teacher's ",command=online_school, fg='white', bg='#EF930C', border=0,
           activebackground='#F3F7D7',
           activeforeground='#F85511', font=('SimSun', 18, 'bold')).place(x=150, y=750, height=50, width=500)


    Label(mainF, text="Select your subject category and provide competitive MCQ questions ", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=1000, y=130)
    Label(mainF, text="required for the relevent subject. Check whether the answers are ", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=1000, y=160)
    Label(mainF, text="correct and cover all the points related to the subject by giving marks.", fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=1000, y=190)
    Label(mainF,
          text="Our current courses are listed on the first page.",
          fg='#5499C7', bg='white',
          font=('SimSun', 15, 'bold')).place(x=1000, y=220)



    Label(mainF, text="  Choose Your Gread  ",
          fg='black', bg='white', font=('SimSun', 30, 'bold')).place(x=1150,
                                                                       y=320)


    Button(mainF, text='O\L Student', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=1150, y=450, height=50, width=500)
    Button(mainF, text='A\L Student', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=1150, y=550, height=50, width=500)
    Button(mainF, text='Univercity Student', command=uni_student,fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=1150, y=650, height=50, width=500)
    Button(mainF, text='Others', fg='white', bg='blue', border=0, activebackground='#AED6F1',
           activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=1150, y=750, height=50, width=500)

    Button(mainF, text='☰',command=toggle_win_page1,  fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)



def toggle_win_page1():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=page1, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',menu)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #


def uni_student():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("png-transparent-abstract-background-technology-hexagonal-pattern.png").resize((850,1080)))
    l = Label(mainF, image=img )
    l.img = img
    l.place(height=1080, width=850, x=0, y=0)



    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                     y=50)

    Label(mainF, text="C Q", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                        y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                       y=150)

    Label(mainF, text="  Choose Your Courses  ",
          fg='black', bg='white', font=('SimSun', 20, 'bold')).place(x=1050,
                                                                       y=100)

    Button(mainF, text="1.Phython Language",command=python, fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
          font=('SimSun', 15, 'bold')).place(x=900,
                                             y=200)
    Button(mainF, text="2.Java Language", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=230)
    Button(mainF, text="3.C Language", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=260)
    Button(mainF, text="4.C++ Language", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=290)
    Button(mainF, text="5.C# Language", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=320)

    Button(mainF, text="6.Web Development ( HTML , ", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=350)
    Button(mainF, text="CSS & Java Script )", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=380)
    Button(mainF, text="7.Information System", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=410)
    Button(mainF, text="8.OOP Concept", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=440)
    Button(mainF, text="9.Advance Mathamatics", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=470)

    Button(mainF, text="10.Higher Mathamatics", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=500)
    Button(mainF, text="11.Advance English", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=530)
    Button(mainF, text="12.Information Security", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=560)
    Button(mainF, text="13.Tamil for Beginer", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=590)
    Button(mainF, text="14.Science", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=620)

    Button(mainF, text="15.Computer History", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=650)
    Button(mainF, text="16.Biology ", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=680)
    Button(mainF, text="17.Agriculture", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=710)
    Button(mainF, text="18.Sinhala", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=740)
    Button(mainF, text="19.Robbot System Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=770)

    Button(mainF, text="20.Macanic Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=800)

    Button(mainF, text="21.Bio Systerm Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=830)
    Button(mainF, text="22.Science for Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=860)
    Button(mainF, text="23.Agro Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=890)
    Button(mainF, text="24.Engineering Technology", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=920)
    Button(mainF, text="25.Information & Communication", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=200)

    Button(mainF, text="26.Accounting", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=230)
    Button(mainF, text="27.Business", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=260)
    Button(mainF, text="28.Information System", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=290)
    Button(mainF, text="29.Tamil", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=320)
    Button(mainF, text="30.Advance Sinhala", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=350)

    Button(mainF, text="31.History", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=380)
    Button(mainF, text="32.Art", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=410)
    Button(mainF, text="33.Dance", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=440)
    Button(mainF, text="34.Western Music", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=470)
    Button(mainF, text="35.Music", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=500)

    #Button(mainF, text='IT Facalty', fg='white', bg='blue', border=0, activebackground='#AED6F1',
          # activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=950, y=200, height=50, width=350)
   # Button(mainF, text='Engeneering Facalty', fg='white', bg='blue', border=0, activebackground='#AED6F1',
          # activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=950, y=300, height=50, width=350)



    Button(mainF, text='☰',command=toggle_win_uni_std,  fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)

    #☰  c



def toggle_win_uni_std():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=uni_student, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',menu)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #



def python():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)

    img = ImageTk.PhotoImage(Image.open("png-transparent-abstract-background-technology-hexagonal-pattern.png").resize((850,1080)))
    l = Label(mainF, image=img )
    l.img = img
    l.place(height=1080, width=850, x=0, y=0)



    Label(mainF, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=100,
                                                                                     y=50)

    Label(mainF, text="C Q", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=190,
                                                                                        y=50)
    Label(mainF, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=260,

                                                                                       y=150)


    Label(mainF, text='Python Language', fg='white', bg='#EF930C', border=0,
          font=('SimSun', 18, 'bold')).place(x=950, y=100, height=30, width=800)

    Button(mainF, text="1.Python - Home",command=py_home, fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
          font=('SimSun', 15, 'bold')).place(x=900,
                                             y=200)
    Button(mainF, text="2.Python - Overview",command=py_over, fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=230)
    Button(mainF, text="3.Python - Environment Setup", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=260)
    Button(mainF, text="4.Python - Basic Syntax", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=290)
    Button(mainF, text="5.Python - Comments", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=320)

    Button(mainF, text="6.Python - Variables", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=350)
    Button(mainF, text="7.Python - Data Types)", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=380)
    Button(mainF, text="8.Python - Operators", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=410)
    Button(mainF, text="9.Python - Decision making", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=440)
    Button(mainF, text="10.Python - Loops", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=470)

    Button(mainF, text="11.Python - Numbers", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=500)
    Button(mainF, text="12.python - Strings", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=530)
    Button(mainF, text="13.python - Lists", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=560)
    Button(mainF, text="14.Python - Tuples", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=590)
    Button(mainF, text="15.Python - Dictionary", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=620)

    Button(mainF, text="16.Python - Date & Time", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=650)
    Button(mainF, text="17.Python - Functions ", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=680)
    Button(mainF, text="18.Python - Modules", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=710)
    Button(mainF, text="19.Python - Fiels I/O", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=740)
    Button(mainF, text="20.Python - Exceptions", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=770)

    Button(mainF, text="21.Python - Classes/Objects", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=800)

    Button(mainF, text="22.Python - Reg Expressions", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=830)
    Button(mainF, text="23.Python - CGI Programming", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=860)
    Button(mainF, text="24.Python - Database Access", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=890)
    Button(mainF, text="25.Python - Networking", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=900,
                                              y=920)
    Button(mainF, text="26.Python - Sending Email", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=200)

    Button(mainF, text="27.Python - Multitheading", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=230)
    Button(mainF, text="28.Python - XML Processing", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=260)
    Button(mainF, text="29.Python - GUI Programming", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=290)
    Button(mainF, text="30.Python - Further Extensions", fg='#5499C7', bg='white', border=0, activebackground='white',
           activeforeground='#EF930C',
           font=('SimSun', 15, 'bold')).place(x=1350,
                                              y=320)

    #Button(mainF, text='IT Facalty', fg='white', bg='blue', border=0, activebackground='#AED6F1',
          # activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=950, y=200, height=50, width=350)
   # Button(mainF, text='Engeneering Facalty', fg='white', bg='blue', border=0, activebackground='#AED6F1',
          # activeforeground='#76448A', font=('SimSun', 15, 'bold')).place(x=950, y=300, height=50, width=350)



    Button(mainF, text='☰', command=toggle_win_python, fg='black', bg='white', border=0, activebackground='white',
           activeforeground='#76448A', font=('SimSun', 20, 'bold')).place(x=1820, y=20, height=50, width=50)
    img = ImageTk.PhotoImage(Image.open("AdobeStock_289595573_Preview.jpeg").resize((50, 50)))
    l = Label(mainF, image=img)
    l.img = img
    l.place(height=50, width=50, x=1860, y=19)

    #☰  c


def toggle_win_python():
    global f1
    f1 = Frame(APP, width=400, height=1070, bg='#12c4c0')
    f1.place(x=1500, y=10)

    Button(APP, text='X', command=python, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 25, 'bold')).place(x=1850, y=20, height=50, width=50)

    Button(APP, text='| | |', command=menu, fg='black', bg='#12c4c0', border=0, activebackground='#12c4c0',
           activeforeground='#76448A', font=('Time New Roman', 20, 'bold')).place(x=1810, y=20, height=50, width=50)



    # buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=56,
                           height=2,
                           fg='#262626',
                           border=0,
                           command=cmd,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'H O M E', '#0f9d9a', '#12c4c0',menu)
    bttn(0, 117, 'N O T I F I C A T I O N', '#0f9d9a', '#12c4c0',None)
    bttn(0, 154, 'S E T T I N G', '#0f9d9a', '#12c4c0', None)
    bttn(0, 191, 'A B O U T   U S', '#0f9d9a', '#12c4c0', None)
    bttn(0, 228, 'E X I T', '#0f9d9a', '#12c4c0', exit)
    bttn(0, 930, 'P O W E R D   B Y  P Y C H A R M  P R O J E C T S', 'yellow', '#12c4c0', None)
    bttn(0, 965, 'P Y T H O N   P R O J E C T  1 . 1', '#0f9d9a', '#12c4c0', None)

    #



index = 0
correct = 0
questions = ["Who developed Python Programming Language?",
             "Which type of Programming does Python support?",
             "Which of the following is the correct extension of the Python file?",
             "Is Python code compiled or interpreted?",
             "All keywords in Python are in _____________"]
options = [['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum', 'Niene Stom', 'Guido van Rossum'],
           ['object-oriented programming', 'structured programming', 'functional programming', 'all of the mentioned', 'all of the mentioned'],
           ['.python', '.pl', '.py', '.p', '.py'],
           ['Python code is both compiled and interpreted', 'Python code is neither compiled nor interpreted', 'Python code is only compiled', 'Python code is only interpreted', 'Python code is both compiled and interpreted'],
           ['Capitalized', 'lower case', 'UPPER CASE', 'None of the mentioned', 'None of the mentioned']]



def displayNextquiz():
    pass


def py_home():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)



    #index = 0
    #correct = 0

    #APP = tk.Tk()
    #APP.geometry("1750x950")

    #questions = ["1 + 1 = ?", "2 + 2 = ?", "3 + 3 = ?", "4 + 4 = ?", "5 + 5 = ?"]
    #options = [['A', 'B', '2', 'C', '2'], ['A', '4', 'V', 'C', '4'], ['A', 'B', '2', '6', '6'],
               #['8', 'B', 'D', 'C', '8'], ['D', '10', 'A', 'C', '10']]
#tk.
    frame = Frame(mainF, padx=350, pady=150, bg="#fff")

    Label(mainF, text='Python - Home Questions', fg='white', bg='#EF930C', border=0,
          font=('SimSun', 18, 'bold')).place(x=350, y=50, height=30, width=1283)

    Label(frame, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=500,
                                                                                     y=550)

    Label(frame, text="C Q", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=590,
                                                                                        y=550)
    Label(frame, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=660,

                                                                                           y=650)


    qz_lable = Label(frame, height=10, width=85, bg="#ddd", font=('SimSun', 20, 'bold'), wraplength=500)

    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)
    v4 = StringVar(frame)

    option1 = Radiobutton(frame, bg="#fff", variable=v1, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option1))
    option2 = Radiobutton(frame, bg="#fff", variable=v2, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option2))
    option3 = Radiobutton(frame, bg="#fff", variable=v3, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option3))
    option4 = Radiobutton(frame, bg="#fff", variable=v4, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option4))

    button_next = Button(frame, text='Next', bg='orange', font=('SimSun', 20, 'bold'),
                            command=lambda: displayNextquiz())

    frame.pack(fill="both", expand="true")
    qz_lable.grid(row=0, column=0)

    option1.grid(sticky='W', row=4, column=0)
    option2.grid(sticky='W', row=6, column=0)
    option3.grid(sticky='W', row=8, column=0)
    option4.grid(sticky='W', row=10, column=0)

    button_next.grid(row=15, column=0)



    # create function  to disable radiobutton

    def disableButtons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state
        option4['state'] = state

    # create a function to check the selected answer

    def checkAnswer(radio):
        global correct, index

        # 4th answer is correct answer
        # we will check the user selected answer with the 4th answer
        if radio['text'] == options[index][4]:
            correct += 1

        index += 1
        disableButtons('disable')

    # create a function display a next quiz


    def displayNextquiz():
        global index, correct

        if button_next['text'] == 'Restart The Quiz':
            correct = 0
            index = 0
            qz_lable['bg'] = 'grey'
            button_next['text'] = 'Next'

        if button_next['text'] == 'Get The Next Quiz':
            py_over()

        if index == len(options):
            qz_lable['text'] = str(correct) + " / " + str(len(options))
            #button_next['text'] = 'Restart The Quiz'
            if correct >= len(options) / 2:
                qz_lable['bg'] = '#A4902A'
                button_next['text'] = 'Get The Next Quiz'
                #python()
                # F2CF22 #E7C41C #D3B526


            else:
                qz_lable['bg'] = 'red'
                button_next['text'] = 'Restart The Quiz'

        #elif correct == len(options) :
            #button_next['text'] = 'Get The Next Quiz'
            #python()


        else:

            qz_lable['text'] = questions[index]

            disableButtons('normal')

            opts = options[index]
            option1['text'] = opts[0]
            option2['text'] = opts[1]
            option3['text'] = opts[2]
            option4['text'] = opts[3]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])
            v4.set(opts[3])

            if index == len(options) - 1:
                button_next['text'] = 'Check the Results'

            elif correct == len(options):
                button_next['text'] == 'Get The Next Quiz'
                #python()

    displayNextquiz()


index1 = 0
correct1 = 0
questions1 = ["Which of the following is used to define a block of code in Python language?",
             "Which keyword is used for function in Python language?",
             "Which of the following character is used to give single-line comments in Python?",
             "Python supports the creation of anonymous functions at runtime, using a construct called __________",
             "What is the order of precedence in python?"]
options1 = [['Indentation', 'Key', 'Brackets', 'All of the mentioned', 'Indentation'],
           ['Function', 'def', 'Fun', 'Define', 'def'],
           ['//', '#', '!', '/*', '#'],
           ['pi', 'anonymous', 'lambda', 'none of the mentioned', 'lambda'],
           ['Exponential, Parentheses, Multiplication, Division, Addition, Subtraction', 'Exponential, Parentheses, Division, Multiplication, Addition, Subtraction',
           'Parentheses, Exponential, Multiplication, Division, Subtraction, Addition', 'Parentheses, Exponential, Multiplication, Division, Addition, Subtraction', 'Parentheses, Exponential, Multiplication, Division, Addition, Subtraction']]


def displayNextquiz1():
    pass


def py_over():
    mainF = Frame(APP, bg='#fff')
    mainF.place(width=1920, height=1080)



    #index = 0
    #correct = 0

    #APP = tk.Tk()
    #APP.geometry("1750x950")

    #questions = ["1 + 1 = ?", "2 + 2 = ?", "3 + 3 = ?", "4 + 4 = ?", "5 + 5 = ?"]
    #options = [['A', 'B', '2', 'C', '2'], ['A', '4', 'V', 'C', '4'], ['A', 'B', '2', '6', '6'],
               #['8', 'B', 'D', 'C', '8'], ['D', '10', 'A', 'C', '10']]
#tk.
    frame = Frame(mainF, padx=350, pady=150, bg="#fff")

    Label(mainF, text='Python - Overview Questions', fg='white', bg='#EF930C', border=0,
          font=('SimSun', 18, 'bold')).place(x=350, y=50, height=30, width=1283)

    Label(frame, text="M", fg='blue', bg='white', font=('SimSun', 65, 'bold')).place(x=500,
                                                                                     y=550)

    Label(frame, text="C Q", fg='black', bg='white', font=('SimSun', 65, 'bold')).place(x=590,
                                                                                        y=550)
    Label(frame, text="Master", fg='black', bg='white', font=('SimSun', 50, 'bold')).place(x=660,

                                                                                           y=650)


    qz_lable = Label(frame, height=10, width=85, bg="#ddd", font=('SimSun', 20, 'bold'), wraplength=500)

    v1 = StringVar(frame)
    v2 = StringVar(frame)
    v3 = StringVar(frame)
    v4 = StringVar(frame)

    option1 = Radiobutton(frame, bg="#fff", variable=v1, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option1))
    option2 = Radiobutton(frame, bg="#fff", variable=v2, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option2))
    option3 = Radiobutton(frame, bg="#fff", variable=v3, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option3))
    option4 = Radiobutton(frame, bg="#fff", variable=v4, font=('SimSun', 20, 'bold'),
                             command=lambda: checkAnswer(option4))

    button_next = Button(frame, text='Next', bg='orange', font=('SimSun', 20, 'bold'),
                            command=lambda: displayNextquiz1())

    frame.pack(fill="both", expand="true")
    qz_lable.grid(row=0, column=0)

    option1.grid(sticky='W', row=4, column=0)
    option2.grid(sticky='W', row=6, column=0)
    option3.grid(sticky='W', row=8, column=0)
    option4.grid(sticky='W', row=10, column=0)

    button_next.grid(row=15, column=0)



    # create function  to disable radiobutton

    def disableButtons(state):
        option1['state'] = state
        option2['state'] = state
        option3['state'] = state
        option4['state'] = state

    # create a function to check the selected answer

    def checkAnswer(radio):
        global correct1, index1

        # 4th answer is correct answer
        # we will check the user selected answer with the 4th answer
        if radio['text'] == options1[index1][4]:
            correct1 += 1

        index1 += 1
        disableButtons('disable')

    # create a function display a next quiz


    def displayNextquiz1():
        global index1, correct1

        if button_next['text'] == 'Restart The Quiz':
            correct1 = 0
            index1 = 0
            qz_lable['bg'] = 'grey'
            button_next['text'] = 'Next'

        if button_next['text'] == 'Get The Next Quiz':
            python()

        if index1 == len(options1):
            qz_lable['text'] = str(correct1) + " / " + str(len(options1))
            #button_next['text'] = 'Restart The Quiz'
            if correct1 >= len(options1) / 2:
                qz_lable['bg'] = '#A4902A'
                button_next['text'] = 'Get The Next Quiz'
                #python()
                # F2CF22 #E7C41C #D3B526


            else:
                qz_lable['bg'] = 'red'
                button_next['text'] = 'Restart The Quiz'

        #elif correct == len(options) :
            #button_next['text'] = 'Get The Next Quiz'
            #python()


        else:

            qz_lable['text'] = questions1[index1]

            disableButtons('normal')

            opts = options1[index1]
            option1['text'] = opts[0]
            option2['text'] = opts[1]
            option3['text'] = opts[2]
            option4['text'] = opts[3]
            v1.set(opts[0])
            v2.set(opts[1])
            v3.set(opts[2])
            v4.set(opts[3])

            if index1 == len(options1) - 1:
                button_next['text'] = 'Check the Results'

            elif correct1 == len(options1):
                button_next['text'] == 'Get The Next Quiz'
                #python()

    displayNextquiz1()



menu()
APP.mainloop()