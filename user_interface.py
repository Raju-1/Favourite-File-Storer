from tkinter import *
from tkinter.ttk import *
from time import *
from sqlite3 import *
from tkinter import messagebox
from tkinter import simpledialog
import main_window
import reset_password

class first_window(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.state("zoomed")
        self.title("starting_window")
        self.style=Style()

        self.style.configure("frame1.TFrame",background="black")
        self.style.configure("label1.TLabel",background="black",font=("colonna mt",50),foreground="red")
        self.style.configure("label2.TLabel", background="white",font=("chiller",40),foreground="light green")
        self.style.configure("Button.TButton", background="black",foreground="navy",font=("colonna mt",28))
        self.style.configure("label3.TLabel", background="black", font=("gigi",20), foreground="orange")

        self.frame1=Frame(self,style="frame1.TFrame",)
        self.frame1.pack(side=TOP,fill=BOTH,expand=TRUE)
        self.style.configure("Headerimg.TLabel", background="black")


class login(first_window):
    def __init__(self):
      first_window.__init__(self)

      self.img1 = PhotoImage(file="image1.png")

      self.label_img1 = Label(self.frame1, image=self.img1, style="Headerimg.TLabel")
      self.label_img1.place(relx=0.05, rely=.015)

      self.label1=Label(self.frame1,text="USER NAME : ",style="label3.TLabel")
      self.label1.place(relx=.69,rely=.45)

      self.entry1 = Entry(self.frame1, font=("book antiqua",15), width=22, style="entry.TEntry")
      self.entry1.place(relx=.82, rely=.45)
      self.entry1.insert(0,"Enter UserName Here")
      self.entry1.bind("<FocusIn>", self.func1)

      self.label2=Label(self.frame1,text=" PASSWORD :",style="label3.TLabel")
      self.label2.place(relx=.69,rely=.55)

      self.entry2 = Entry(self.frame1, font=("book antiqua",15), width=22,show="*")
      self.entry2.place(relx=.82, rely=.56)
      self.entry2.insert(0,"")
      self.entry2.bind("<FocusIn>", self.func2)

      self.forgot_password_button=Button(self.frame1,text="< < < Forget Password ? >>> "
                    ,command=self.forgot_password,style="label3.TLabel")
      self.forgot_password_button.place(relx=.75,rely=.67)

      self.button=Button(self.frame1,text="Continue",style="Button.TButton",command= self.click_continue)
      self.button.place(relx=.82,rely=.75)
      self.bind('<Return>', lambda event=None: self.button.invoke())

      con = connect("login.db")
      cur = con.cursor()
      cur.execute("select * from Login" )
      accounts = cur.fetchall()
      x = accounts[len(accounts) - 1]
      cur.execute(" update Login set count ='{0}' ".format(0))
      con.commit()


      con = connect("login.db")
      cur = con.cursor()
      cur.execute("select * from Login" )
      accounts = cur.fetchall()
      x = accounts[len(accounts) - 1]
      if x[3]!=1:
          cur.execute(" update Login set checker ='{0}' ".format(0))
          con.commit()
          l = []
          for i in range(59, -1, -1):
              l.append(i)

          self.style.configure("label_3.TLabel", background="black", font=("gigi", 90), foreground="cyan")
          label_of_timer = Label(self.frame1, text="- : Retry After 1 Min : -\n\n", style="label_3.TLabel")
          label_of_timer.place(relx=.1, rely=.35)

          self.style.configure("label_1.TLabel", background="black", font=("colonna mt", 180), foreground="red")

          label_timer = Label(self.frame1, style="label_1.TLabel")
          label_timer.place(relx=.53, rely=.57)

          for i in range(len(l) - 1, -1, -1):
              label_timer['text'] = i
              self.update()
              sleep(1)


          self.destroy()

          con = connect("login.db")
          cur = con.cursor()
          cur.execute("select * from Login")
          accounts = cur.fetchall()
          x = accounts[len(accounts) - 1]
          cur.execute(" update Login set checker ='{0}' ".format(1))
          con.commit()
          login()



    print("__name__ :", __name__)

    if __name__!="__main__" :
          con=connect("login.db")
          cur=con.cursor()
          cur.execute(" update Login set count ='{0}' ".format(0))
          con.commit()

    def func1(self,event):
        if self.entry1.get()=="Enter UserName Here":
            self.entry1.delete(0, END)


    def func2(self, event):
        if self.entry2.get() == "":
            self.entry2.delete(0, END)
            if self.entry1.get()=="":
               self.entry1.insert(0,"Enter UserName Here")

    def forgot_password(self):
           answer=simpledialog.askstring("Please answer correctly !",
                    "Write Your D.O.B without any Space",
                        parent=self,show="*")
           if answer is not None:
               if answer=="26061998":
                   self.destroy()
                   reset_password.reset_password()
               else:
                   messagebox.showerror("Error Message", "Incorrect ! Please Try Again")
           else:
               print("Please Try again")

    def click_continue(self,event = None):
        con = connect('login.db')
        cur = con.cursor()
        cur.execute("""select * from Login 
                where user_name = '{0}' and Password = '{1}'""".format(
            self.entry1.get(), self.entry2.get()))
        row = cur.fetchone()
        self.c = 0
        if row is not None:
            self.destroy()
            main_window.Home()

        else:
            con = connect('login.db')
            cur = con.cursor()
            cur.execute("select * from Login")
            accounts = cur.fetchall()
            x = accounts[len(accounts) - 1]
            if x[2]<3:
             self.c = x[2]+1
             messagebox.showerror("Error Message"," Incorrect username/password\n\nNote : Only 3 Attempts are Allowed\n\nYour Attempt :{0}".format(self.c))
             cur.execute(" update Login set count ='{0}' where count = '{1}' ".format(self.c,x[2]))
             con.commit()
             if self.c==3:
              con = connect('login.db')
              cur = con.cursor()
              cur.execute("select * from Login")
              accounts = cur.fetchall()
              x = accounts[len(accounts) - 1]
              #print(x[2])
              cur.execute(" update Login set count ='{0}' where count = '{1}' ".format(0,x[2]))
              cur.execute(" update Login set checker ='{0}' ".format(0))
              con.commit()
              retry=messagebox.askretrycancel("Too Many Attempts", "Incorrect username/password\n\n Note : If you Cancel You shall be quit from Window")
              if retry == True :
                 l=[]
                 for i in range(59,-1,-1):
                  l.append(i)

                 self.style.configure("label_3.TLabel", background="black", font=("gigi",90), foreground="cyan")
                 label_of_timer = Label(self.frame1,text="- : Retry After 1 Min : -\n\n",style="label_3.TLabel")
                 label_of_timer.place(relx=.1, rely=.35)

                 self.style.configure("label_1.TLabel", background="black", font=("colonna mt",180), foreground="red")

                 label_timer=Label(self.frame1,style="label_1.TLabel")
                 label_timer.place(relx=.53,rely=.57)


                 for i in range(len(l)-1,-1,-1):
                  label_timer['text']=i
                  self.update()
                  sleep(1)

                 self.destroy()
                 con = connect("login.db")
                 cur = con.cursor()
                 cur.execute("select * from Login")
                 accounts = cur.fetchall()
                 x = accounts[len(accounts) - 1]
                 cur.execute(" update Login set checker ='{0}' ".format(1))
                 con.commit()

                 login()
              else:
                  self.destroy()

                  con = connect("login.db")
                  cur = con.cursor()
                  cur.execute("select * from Login")
                  accounts = cur.fetchall()
                  x = accounts[len(accounts) - 1]
                  cur.execute(" update Login set checker ='{0}' ".format(1))
                  con.commit()


if __name__=="__main__":
  x1=login()
  x1.mainloop()
