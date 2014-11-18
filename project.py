import sys
from Tkinter import *
import tkMessageBox
def bmr():
    your_height = float(height.get())
    your_weight = float(weight.get())
    your_old = int(old.get())
    if men:
        your_bmr = 66 + (13.7*your_weight) + (5*your_height) - (6.8*your_old)
        bmr_label = Label(text="Your BMR is " + str(your_bmr), fg ='#FF3366').pack()
    else:
        your_bmr = 665 + (9.6*your_weight) + (1.8*your_height) - (4.7*your_old)
        bmr_label = Label(text="Your BMR is " + str(your_bmr), fg ='#FF3366').pack()
def mAbout():
    tkMessageBox.showinfo(title='About',message='This is project of freshy of ITKMITL in PSIT subject')
    return

nGui = Tk() #makewindow


nGui.geometry('450x450+500+300') #windowsize
nGui.title('Fit & Firm')

#make label for this application
mlabel = Label(text='BMR AND TDEE Calculator Program', fg='#FF6666', bg='#CCFFFF').pack()
mlabel2 = Label(text='Please input your height weight and old :)', fg='#CC99FF', bg='#CCFFFF').pack()

#Creat gender botton
message = Message(nGui,text = 'Please select your gender', fg='#3399FF', width=225).pack(anchor=W)
men=Radiobutton(nGui,text='Men',command=bmr,value = 1, variable = 1).pack(anchor=W)
women=Radiobutton(nGui,text='Women',command=bmr,value = 2, variable = 1).pack(anchor=W)

#Creat input height weight and old
input_frame = Frame()
input_frame.pack()
height_label = Label(input_frame, text="Your height(Cm.)", fg='#3399FF').grid(row=0, column=0)
height = StringVar()
your_height = Entry(input_frame, textvariable=height)
your_height.grid(row=0, column=1)


weight_label = Label(input_frame, text="Your weight (Kg.)", fg='#3399FF').grid(row=1, column=0)
weight = StringVar()
your_weight = Entry(input_frame, textvariable=weight)
your_weight.grid(row=1, column=1)


old_label = Label(input_frame, text="Your old (year)", fg='#3399FF').grid(row=2, column=0)
old = StringVar()
your_old = Entry(input_frame, textvariable=old)
your_old.grid(row=2, column=1)

#make botton to calculate bmr TDEE
calculate = Button(text="Calculate",command=bmr, fg="#FF0066", bg="#FFFF99").pack()

# Creator Menu
menubar=Menu(nGui)
filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label='ICE 57070119')
filemenu.add_command(label='KIING 57070136')
filemenu.add_command(label='Thanks')
menubar.add_cascade(label='Creator',menu=filemenu)
# Help Menu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label='Help Docs')
helpmenu.add_command(label='About',command = mAbout)
menubar.add_cascade(label='Help',menu=helpmenu)

nGui.config(menu=menubar)
nGui.mainloop()


