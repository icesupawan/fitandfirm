import sys
from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import tkFont
import ttk

class Apps:
    def __init__(self, master):
        self.v = IntVar()
        


        #Logo Image
        self.photo = PhotoImage(file = "logo.gif")
        self.label = Label(image = self.photo, bg="#a8cf38")
        self.label.image = self.photo
        self.label.pack()
    
        #Creat gender botton
        message = Message(nGui,text = 'What is your gender ?', fg='#FFFFFF', bg="#a8cf38", width=225, font = tkFont.Font(size = 16, \
                                                                                                                         weight=tkFont.BOLD)).place(x=57, y = 130)
        men=Radiobutton(nGui,text='Men',value = 0, variable = self.v, font = tkFont.Font(size = 8), bg="#a8cf38").place(x=80, y = 167)
        women=Radiobutton(nGui,text='Women',value = 1, variable = self.v, font = tkFont.Font(size = 8), bg="#a8cf38").place(x=80, y = 204)

          
        # combobox select always sometime never
        mlabel2 = Label(text='How often do you work out ?', fg='#FFFFFF', font = tkFont.Font(family = "Calibri", size = 16, weight=tkFont.BOLD),\
                        bg="#a8cf38").place(x=60,y = 241)
        self.values = StringVar()
        box = ttk.Combobox(master, textvariable=self.values, state='readonly')
        box['values'] = ('Always', 'Sometimes', 'Never')
        box.current(0)
        box.place(x=80,y = 278)

        #Creat input height weight and old
        mlabel2 = Label(text='Please input your height weight and old :)', fg='#FFFFFF', font = tkFont.Font(family = "Calibri", size = 16, weight=tkFont.BOLD),\
                        bg="#a8cf38").place(x=60, y=315)
        input_frame = Frame(bg="#a8cf38")
        input_frame.place(x=130, y=360)
        height_label = Label(input_frame, text="Your height (Cm.)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10),\
                             bg="#a8cf38").grid(row=0, column=0)
        self.height = StringVar()
        self.your_height = Entry(input_frame, textvariable=self.height)
        self.your_height.grid(row=0, column=1)

        weight_label = Label(input_frame, text="Your weight (Kg.)", fg='#000000',  font = tkFont.Font(family = "Cursive", size = 10),\
                             bg="#a8cf38").grid(row=1, column=0)
        self.weight = StringVar()
        self.your_weight = Entry(input_frame, textvariable=self.weight)
        self.your_weight.grid(row=1, column=1)

        old_label = Label(input_frame, text="Your old (year)", fg='#000000', font = tkFont.Font(family = "Cursive", size = 10), \
                          bg="#a8cf38").grid(row=2, column=0)
        self.old = StringVar()
        self.your_old = Entry(input_frame, textvariable=self.old)
        self.your_old.grid(row=2, column=1)

        button_frame = Frame(bg="#a8cf38")
        button_frame.place(x=170, y=450)

        #make botton to calculate bmr TDEE
        self.calculate = Button(button_frame, text="Calculate",command=self.bmr, fg="#FF0066", bg="#FFFF99", font = tkFont.Font(family = "Latha", size = 12))
        self.calculate.grid(row=0, column=0, pady = 5, padx=10)

        #botton to reset
        self.reset = Button(button_frame, text="Reset", command=self.reset, fg="#FF0066", bg="#FFFF99", font = tkFont.Font(family = "Latha", size = 12), state='disabled')
        self.reset.grid(row=0, column=1, padx=10)
          
                        
        #About me Menu
        self.menubar=Menu(nGui)
        self.filemenu = Menu(self.menubar ,tearoff = 0)
        self.filemenu.add_command(label='Creator', font = tkFont.Font(family = "Latha", size = 8),command = self.new_win)
        self.filemenu.add_command(label='Special Thanks', font = tkFont.Font(family = "Latha", size = 8),command = self.mThanks)
        self.menubar.add_cascade(label='About me', font = tkFont.Font(family = "Latha", size = 8),menu=self.filemenu)
        
        # Help Menu
        self.helpmenu = Menu(self.menubar,tearoff = 0)
        self.helpmenu.add_command(label='Help Docs', font = tkFont.Font(family = "Latha", size = 8),command = self.help_docs)
        self.helpmenu.add_command(label='About', font = tkFont.Font(family = "Latha", size = 8),command = self.mAbout)
        self.menubar.add_cascade(label='Help', font = tkFont.Font(family = "Latha", size = 8),menu=self.helpmenu)
        
        # label presen who design
        mlabel3 = Label(text='Faculty of Information Technology,King Mongkut\'s Institute of Technology Ladkrabang', fg='#FFFFFF', bg="#a8cf38",\
                        font = tkFont.Font(family = "Monospace", size = 9)).pack(side = 'bottom')
         
    def bmr(self):
        try:
            your_sex = int(self.v.get())
            self.your_height1 = float(self.height.get())
            self.your_weight1 = float(self.weight.get())
            self.your_old1 = int(self.old.get())
            if your_sex == 0:
                self.your_bmr = 66 + (13.7*self.your_weight1) + (5*self.your_height1) - (6.8*self.your_old1)
                self.bmr_label = Label(text="Your BMR is " + str(self.your_bmr)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium", \
                                                                                                                                        size = 12))
                self.bmr_label.place(x=130, y=505)
            elif your_sex == 1:
                self.your_bmr = 665 + (9.6*self.your_weight1) + (1.8*self.your_height1) - (4.7*self.your_old1)
                self.bmr_label = Label(text="Your BMR is " + str(self.your_bmr) +" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium", \
                                                                                                                                         size = 12))
                self.bmr_label.place(x=130, y=505)

            if self.values.get() == 'Always':
                self.your_tdee = self.your_bmr * 1.2
                self.tdee_label =Label(text="Your TDEE is " + str(self.your_tdee)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium",\
                                                                                                                                          size = 12))
                self.tdee_label.place(x=130, y=530)
            elif self.values.get() == 'Sometimes':
                self.your_tdee = self.your_bmr * 1.55
                self.tdee_label =Label(text="Your TDEE is " + str(self.your_tdee)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium",\
                                                                                                                                          size = 12))
                self.tdee_label.place(x=130, y=530)
            elif self.values.get() == 'Never':
                self.your_tdee = self.your_bmr * 1.9
                self.tdee_label =Label(text="Your TDEE is " + str(self.your_tdee)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium",\
                                                                                                                                          size = 12))
                self.tdee_label.place(x=130, y=530)
            self.lost =Label(text="If you want to lost weigt you should eat : " + str(self.your_tdee - 500)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium",\
                                                                                                                                          size = 12))
            self.lost.place(x=40, y=565)
            self.gain =Label(text="If you want to gain weigt you should eat : " + str(self.your_tdee + 500)+" kilocalorie. ", fg ='#FF3366', bg="#a8cf38", font = tkFont.Font(family = "Franklin Gothic Medium",\
                                                                                                                                          size = 12))
            self.gain.place(x=40, y=590)

            self.calculate.config(state='disabled', fg="#FF0066", bg="#FFFF99")
            self.reset.config(state='active', fg="#FF0066", bg="#FFFF99")
        except:
            tkMessageBox.showerror(title='ERROR', message='Please input all or Type of input is number only!')

       
    def mAbout(self):
        tkMessageBox.showinfo(title='About',message='This is project of freshy of ITKMITL in PSIT subject')
        return
   
    def mThanks(self):
        tkMessageBox.showinfo(title='Special Thanks',message='    SPECIAL THANKS \n ||| Chotipat Pornavalai |||')
        return

    #Reset Function
    def reset(self):
        self.bmr_label.place_forget()
        self.tdee_label.place_forget()
        self.height = StringVar()
        self.your_height.config(textvariable=self.height)
        self.weight = StringVar()
        self.your_weight.config(textvariable=self.weight)
        self.old = StringVar()
        self.your_old.config(textvariable=self.old)
        self.lost.place_forget()
        self.gain.place_forget()

        self.calculate.config(state='active', fg="#FF0066", bg="#FFFF99")
        self.reset.config(state='disabled', fg="#FF0066", bg="#FFFF99")

    #Creator
    def new_win(self):
        self.n_win = Toplevel()
        self.n_win.geometry('500x340+500+300') #windowsize
        self.photo = PhotoImage(file = "profile.gif")
        self.label = Label(self.n_win,image =self.photo, bg="#a8cf38")
        self.label.image = self.photo
        self.label.place(x=0,y=0)

    #Help
    def help_docs(self):
        self.help_docs = Toplevel()
        self.help_docs.geometry('479x519+500+300') #windowsize
        
        self.photo = PhotoImage(file = "help.gif")
        self.label = Label(self.help_docs,image =self.photo, bg="#FFFFFF")
        self.label.image = self.photo
        self.label.place(x=0,y=0)
        
        mlabel3 = Label(self.help_docs, text='\n This application help you to find your BMR and  TDEE \n select your sex and how offen do you work out \n input your height, weight and your old \n Let\'s calculate your callories!', \
                        fg='#a8cf38',bg = '#FFFFFF', font = tkFont.Font(family = "Monospace", size = 14)).pack(side = 'top')


nGui = Tk() #makewindow

app = Apps(nGui)

nGui.geometry('500x650+500+300') #windowsize
nGui.title('love fitt')

nGui.config(menu=app.menubar,background = '#a8cf38')
nGui.mainloop()
