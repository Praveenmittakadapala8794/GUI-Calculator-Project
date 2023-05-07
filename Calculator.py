import tkinter
from tkinter import *
x = tkinter.Tk()
x.geometry('450x450+300+100')
x.resizable(0,0)
x.title("Calculator")
#x.mainloop()

Label_data = Label(x)
Label_data.pack(expand = True,fill = 'both')

data = StringVar()
Label_data = Label(x,textvariable=data)
Label_data.pack(expand = True,fill ='both')

val=""
def btn1_is_clicked():
    global val
    val=val+"1"
    data.set(val)



def btn2_is_clicked():
    global val
    val=val+"2"
    data.set(val)


def btn3_is_clicked():
    global val
    val=val+"3"
    data.set(val)


def btn4_is_clicked():
    global val
    val=val+"4"
    data.set(val)


def btn5_is_clicked():
    global val
    val=val+"5"
    data.set(val)


def btn6_is_clicked():
    global val
    val=val+"6"
    data.set(val)

def btn7_is_clicked():
    global val
    val=val+"7"
    data.set(val)


def btn8_is_clicked():
    global val
    val=val+"8"
    data.set(val)


def btn9_is_clicked():
    global val
    val=val+"9"
    data.set(val)


def btn0_is_clicked():
    global val
    val=val+"0"
    data.set(val)


def btnplus_is_clicked():
    global val
    val=val+"+"
    data.set(val)


def btnminus_is_clicked():
    global val
    val=val+"-"
    data.set(val)


def btnmul_is_clicked():
    global val
    val=val+"*"
    data.set(val)


def btndiv_is_clicked():
    global val
    val=val+"/"
    data.set(val)


def btnC_is_clicked():
    global val
    val=""
    data.set(val)


def btnequal_is_clicked():
    global val
    val=eval(val)
    val=str(val)
    data.set(val)


frame1=Frame(x,bg='white')
frame1.pack(expand=True,fill='both')


frame2=Frame(x,bg='white')
frame2.pack(expand=True,fill='both')


frame3=Frame(x,bg='white')
frame3.pack(expand=True,fill='both')


frame4=Frame(x,bg='white')
frame4.pack(expand=True,fill='both')

btn1 = Button(frame1,text='1',font =("verdana",20),border=0,command=btn1_is_clicked)
btn1.pack(side=LEFT,expand=True,fill='both')



btn2 = Button(frame1,text='2',font =("verdana",20),border=0,command=btn2_is_clicked)
btn2.pack(side=LEFT,expand=True,fill='both')


btn3 = Button(frame1,text='3',font =("verdana",20),border=0,command=btn3_is_clicked)
btn3.pack(side=LEFT,expand=True,fill='both')


btnplus = Button(frame1,text='+',font =("verdana",20),border=0,command=btnplus_is_clicked)
btnplus.pack(side=LEFT,expand=True,fill='both')


btn4 = Button(frame2,text='4',font =("verdana",20),border=0,command=btn4_is_clicked)
btn4.pack(side=LEFT,expand=True,fill='both')


btn5 = Button(frame2,text='5',font =("verdana",20),border=0,command=btn5_is_clicked)
btn5.pack(side=LEFT,expand=True,fill='both')


btn6 = Button(frame2,text='6',font =("verdana",20),border=0,command=btn6_is_clicked)
btn6.pack(side=LEFT,expand=True,fill='both')


btnminus = Button(frame2,text='-',font =("verdana",20),border=0,command=btnminus_is_clicked)
btnminus.pack(side=LEFT,expand=True,fill='both')


btn7 = Button(frame3,text='7',font =("verdana",20),border=0,command=btn7_is_clicked)
btn7.pack(side=LEFT,expand=True,fill='both')


btn8 = Button(frame3,text='8',font =("verdana",20),border=0,command=btn8_is_clicked)
btn8.pack(side=LEFT,expand=True,fill='both')


btn9 = Button(frame3,text='9',font =("verdana",20),border=0,command=btn9_is_clicked)
btn9.pack(side=LEFT,expand=True,fill='both')


btnmul = Button(frame3,text='*',font =("verdana",20),border=0,command=btnmul_is_clicked)
btnmul.pack(side=LEFT,expand=True,fill='both')


btnC = Button(frame4,text='C',font =("verdana",20),border=0,command=btnC_is_clicked)
btnC.pack(side=LEFT,expand=True,fill='both')



btn0 = Button(frame4,text='0',font =("verdana",20),border=0,command=btn0_is_clicked)
btn0.pack(side=LEFT,expand=True,fill='both')


btnequal = Button(frame4,text='=',font =("verdana",20),border=0,command=btnequal_is_clicked)
btnequal.pack(side=LEFT,expand=True,fill='both')


btndiv = Button(frame4,text='/',font =("verdana",20),border=0,command=btndiv_is_clicked)
btndiv.pack(side=LEFT,expand=True,fill='both')

x.mainloop()



