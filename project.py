import sys
from Tkinter import *
import tkMessageBox
import tkFont
import ttk

class Apps:
    def __init__(self, master):
        self.v = IntVar()

        #make label for this application
        mlabel = Label(text='BMR AND TDEE Calculator Program', fg='#FF6666', bg="#FFFFFF",  font = tkFont.Font(family = "Fantasy", size = 50, weight=tkFont.BOLD)).pack()
        
        #Creat gender botton
        message = Message(nGui,text = 'What is your gender ?', fg='#00CC66', bg="#FFFFFF", width=225, font = tkFont.Font(family = "Calibri", size = 16)).pack(anchor=W)
        men=Radiobutton(nGui,text='Men',value = 0, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)
        women=Radiobutton(nGui,text='Women',value = 1, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)

          
        # combobox select always sometime never
        message = Message(nGui,text = 'How often do you work out ?', fg='#00CC66', width=225, font = tkFont.Font(family = "Calibri", size = 14), bg="#FFFFFF").pack(anchor=W)
        self.values = StringVar()
        box = ttk.Combobox(master, textvariable=self.values, state='readonly')
        box['values'] = ('Always', 'Sometimes', 'Never')
        box.current(0)
        box.pack(anchor=W, pady = 10)

        #Creat input height weight and old
        mlabel2 = Label(text='Please input your height weight and old :)', fg='#00CC66', font = tkFont.Font(family = "Calibri", size = 16), bg="#FFFFFF").pack(pady = 20)
        input_frame = Frame()
        input_frame.pack()
        height_label = Label(input_frame, text="Your height (Cm.)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=0, column=0)
        self.height = StringVar()
        your_height = Entry(input_frame, textvariable=self.height)
        your_height.grid(row=0, column=1)

        weight_label = Label(input_frame, text="Your weight (Kg.)", fg='#000000',  font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=1, column=0)
        self.weight = StringVar()
        your_weight = Entry(input_frame, textvariable=self.weight)
        your_weight.grid(row=1, column=1)

        old_label = Label(input_frame, text="Your old (year)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=2, column=0)
        self.old = StringVar()
        your_old = Entry(input_frame, textvariable=self.old)
        your_old.grid(row=2, column=1)
      

        #make botton to calculate bmr TDEE
        self.calculate = Button(text="Calculate",command=self.bmr, fg="#FF0066", bg="#FFFF99", font = tkFont.Font(family = "Latha", size = 12))
        self.calculate.pack(pady = 20)

        # Creator Menu
        self.menubar=Menu(nGui)
        self.filemenu = Menu(self.menubar ,tearoff = 0)
        self.filemenu.add_command(label='ICE 57070119', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='KIING 57070136', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='Thanks', font = tkFont.Font(family = "Latha", size = 8))
        self.menubar.add_cascade(label='Creator', font = tkFont.Font(family = "Latha", size = 8),menu=self.filemenu)
        # Help Menu
        self.helpmenu = Menu(self.menubar,tearoff = 0)
        self.helpmenu.add_command(label='Help Docs', font = tkFont.Font(family = "Latha", size = 8))
        self.helpmenu.add_command(label='About', font = tkFont.Font(family = "Latha", size = 8),command = self.mAbout)
        self.menubar.add_cascade(label='Help', font = tkFont.Font(family = "Latha", size = 8),menu=self.helpmenu)



        
    def bmr(self):
        your_sex = int(self.v.get())
        your_height = float(self.height.get())
        your_weight = float(self.weight.get())
        your_old = int(self.old.get())
        if your_sex == 0:
            your_bmr = 66 + (13.7*your_weight) + (5*your_height) - (6.8*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()
        elif your_sex == 1:
            your_bmr = 665 + (9.6*your_weight) + (1.8*your_height) - (4.7*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()

  import sys
from Tkinter import *
import tkMessageBox
import tkFont
import ttk

class Apps:
    def __init__(self, master):
        self.v = IntVar()

        #make label for this application
        mlabel = Label(text='BMR AND TDEE Calculator Program', fg='#FF6666', bg="#FFFFFF",  font = tkFont.Font(family = "Fantasy", size = 50, weight=tkFont.BOLD)).pack()
        
        #Creat gender botton
        message = Message(nGui,text = 'What is your gender ?', fg='#00CC66', bg="#FFFFFF", width=225, font = tkFont.Font(family = "Calibri", size = 16)).pack(anchor=W)
        men=Radiobutton(nGui,text='Men',value = 0, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)
        women=Radiobutton(nGui,text='Women',value = 1, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)

          
        # combobox select always sometime never
        message = Message(nGui,text = 'How often do you work out ?', fg='#00CC66', width=225, font = tkFont.Font(family = "Calibri", size = 14), bg="#FFFFFF").pack(anchor=W)
        self.values = StringVar()
        box = ttk.Combobox(master, textvariable=self.values, state='readonly')
        box['values'] = ('Always', 'Sometimes', 'Never')
        box.current(0)
        box.pack(anchor=W, pady = 10)

        #Creat input height weight and old
        mlabel2 = Label(text='Please input your height weight and old :)', fg='#00CC66', font = tkFont.Font(family = "Calibri", size = 16), bg="#FFFFFF").pack(pady = 20)
        input_frame = Frame()
        input_frame.pack()
        height_label = Label(input_frame, text="Your height (Cm.)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=0, column=0)
        self.height = StringVar()
        your_height = Entry(input_frame, textvariable=self.height)
        your_height.grid(row=0, column=1)

        weight_label = Label(input_frame, text="Your weight (Kg.)", fg='#000000',  font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=1, column=0)
        self.weight = StringVar()
        your_weight = Entry(input_frame, textvariable=self.weight)
        your_weight.grid(row=1, column=1)

        old_label = Label(input_frame, text="Your old (year)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=2, column=0)
        self.old = StringVar()
        your_old = Entry(input_frame, textvariable=self.old)
        your_old.grid(row=2, column=1)
      

        #make botton to calculate bmr TDEE
        self.calculate = Button(text="Calculate",command=self.bmr, fg="#FF0066", bg="#FFFF99", font = tkFont.Font(family = "Latha", size = 12))
        self.calculate.pack(pady = 20)

        # Creator Menu
        self.menubar=Menu(nGui)
        self.filemenu = Menu(self.menubar ,tearoff = 0)
        self.filemenu.add_command(label='ICE 57070119', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='KIING 57070136', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='Thanks', font = tkFont.Font(family = "Latha", size = 8))
        self.menubar.add_cascade(label='Creator', font = tkFont.Font(family = "Latha", size = 8),menu=self.filemenu)
        # Help Menu
        self.helpmenu = Menu(self.menubar,tearoff = 0)
        self.helpmenu.add_command(label='Help Docs', font = tkFont.Font(family = "Latha", size = 8))
        self.helpmenu.add_command(label='About', font = tkFont.Font(family = "Latha", size = 8),command = self.mAbout)
        self.menubar.add_cascade(label='Help', font = tkFont.Font(family = "Latha", size = 8),menu=self.helpmenu)



        
    def bmr(self):
        your_sex = int(self.v.get())
        your_height = float(self.height.get())
        your_weight = float(self.weight.get())
        your_old = int(self.old.get())
        if your_sex == 0:
            your_bmr = 66 + (13.7*your_weight) + (5*your_height) - (6.8*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()
        elif your_sex == 1:
            your_bmr = 665 + (9.6*your_weight) + (1.8*your_height) - (4.7*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()

        if self.values.get() == 'Always':
            your_tdee = your_bmr * 1.2
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Sometimes':
            your_tdee = your_bmr * 1.55
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Never':
            your_tdee = your_bmr * 1.9
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()

        self.calculate.config(state='disabled')
        
   
    def mAbout(self):
        tkMessageBox.showinfo(title='About',message='This is project of freshy of ITKMITL in PSIT subject')
        return


nGui = Tk() #makewindow

app = Apps(nGui)

nGui.geometry('500x500+500+300') #windowsize
nGui.title('Fit & Firm')

nGui.config(menu=app.menubar,background = '#FFFFFF')
nGui.mainloop()
      if self.values.get() == 'Always':
            your_tdee = your_bmr * 1.2
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Sometimes':
            your_tdee = your_bmr * 1.55
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Never':
            your_tdee = your_bmr * 1.9
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()

        self.calculate.config(state='disabled')
        
   
    def mAbout(self):
        tkMessageBox.showinfo(title='About',message='This is project of freshy of ITKMITL in PSIT subject')
        return


nGui = Tk() #makewindow

app = Apps(nGui)

nGui.geometry('500x500+500+300') #windowsize
nGui.title('Fit & Firm')

nGui.config(menu=app.menubar,background = '#FFFFFF')
nGui.mainloop()
import sys
from Tkinter import *
import tkMessageBox
import tkFont
import ttk

class Apps:
    def __init__(self, master):
        self.v = IntVar()

        #make label for this application
        mlabel = Label(text='BMR AND TDEE Calculator Program', fg='#FF6666', bg="#FFFFFF",  font = tkFont.Font(family = "Fantasy", size = 50, weight=tkFont.BOLD)).pack()
        
        #Creat gender botton
        message = Message(nGui,text = 'What is your gender ?', fg='#00CC66', bg="#FFFFFF", width=225, font = tkFont.Font(family = "Calibri", size = 16)).pack(anchor=W)
        men=Radiobutton(nGui,text='Men',value = 0, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)
        women=Radiobutton(nGui,text='Women',value = 1, variable = self.v, font = tkFont.Font(family = "Tw Cen MT", size = 12), bg="#FFFFFF").pack(anchor=W)

          
        # combobox select always sometime never
        message = Message(nGui,text = 'How often do you work out ?', fg='#00CC66', width=225, font = tkFont.Font(family = "Calibri", size = 14), bg="#FFFFFF").pack(anchor=W)
        self.values = StringVar()
        box = ttk.Combobox(master, textvariable=self.values, state='readonly')
        box['values'] = ('Always', 'Sometimes', 'Never')
        box.current(0)
        box.pack(anchor=W, pady = 10)

        #Creat input height weight and old
        mlabel2 = Label(text='Please input your height weight and old :)', fg='#00CC66', font = tkFont.Font(family = "Calibri", size = 16), bg="#FFFFFF").pack(pady = 20)
        input_frame = Frame()
        input_frame.pack()
        height_label = Label(input_frame, text="Your height (Cm.)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=0, column=0)
        self.height = StringVar()
        your_height = Entry(input_frame, textvariable=self.height)
        your_height.grid(row=0, column=1)

        weight_label = Label(input_frame, text="Your weight (Kg.)", fg='#000000',  font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=1, column=0)
        self.weight = StringVar()
        your_weight = Entry(input_frame, textvariable=self.weight)
        your_weight.grid(row=1, column=1)

        old_label = Label(input_frame, text="Your old (year)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), bg="#FFFFFF").grid(row=2, column=0)
        self.old = StringVar()
        your_old = Entry(input_frame, textvariable=self.old)
        your_old.grid(row=2, column=1)
      

        #make botton to calculate bmr TDEE
        self.calculate = Button(text="Calculate",command=self.bmr, fg="#FF0066", bg="#FFFF99", font = tkFont.Font(family = "Latha", size = 12))
        self.calculate.pack(pady = 20)

        # Creator Menu
        self.menubar=Menu(nGui)
        self.filemenu = Menu(self.menubar ,tearoff = 0)
        self.filemenu.add_command(label='ICE 57070119', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='KIING 57070136', font = tkFont.Font(family = "Latha", size = 8))
        self.filemenu.add_command(label='Thanks', font = tkFont.Font(family = "Latha", size = 8))
        self.menubar.add_cascade(label='Creator', font = tkFont.Font(family = "Latha", size = 8),menu=self.filemenu)
        # Help Menu
        self.helpmenu = Menu(self.menubar,tearoff = 0)
        self.helpmenu.add_command(label='Help Docs', font = tkFont.Font(family = "Latha", size = 8))
        self.helpmenu.add_command(label='About', font = tkFont.Font(family = "Latha", size = 8),command = self.mAbout)
        self.menubar.add_cascade(label='Help', font = tkFont.Font(family = "Latha", size = 8),menu=self.helpmenu)



        
    def bmr(self):
        your_sex = int(self.v.get())
        your_height = float(self.height.get())
        your_weight = float(self.weight.get())
        your_old = int(self.old.get())
        if your_sex == 0:
            your_bmr = 66 + (13.7*your_weight) + (5*your_height) - (6.8*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()
        elif your_sex == 1:
            your_bmr = 665 + (9.6*your_weight) + (1.8*your_height) - (4.7*your_old)
            bmr_label = Label(text="Your BMR is " + str(your_bmr)+" kilocalorie. ", fg ='#FF3366').pack()

        if self.values.get() == 'Always':
            your_tdee = your_bmr * 1.2
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Sometimes':
            your_tdee = your_bmr * 1.55
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()
        elif self.values.get() == 'Never':
            your_tdee = your_bmr * 1.9
            tdee_label =Label(text="Your TDEE is " + str(your_tdee)+" kilocalorie. ", fg ='#FF3366').pack()

        self.calculate.config(state='disabled')
        
   
    def mAbout(self):
        tkMessageBox.showinfo(title='About',message='This is project of freshy of ITKMITL in PSIT subject')
        return


nGui = Tk() #makewindow

app = Apps(nGui)

nGui.geometry('500x500+500+300') #windowsize
nGui.title('Fit & Firm')

nGui.config(menu=app.menubar,background = '#FFFFFF')
nGui.mainloop()



