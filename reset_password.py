from tkinter import *
from tkinter import messagebox
import user_interface
from tkinter.ttk import *
from sqlite3 import connect

class reset_password(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.style=Style()
        self.title("Reset Password")
        self.geometry("500x300+400+100")


        self.style.configure("frame.TFrame",background="black")

        self.style.configure("label.TLabel",font=("Book antiqua",15)
                             ,foreground="cyan",background="black")

        self.style.configure("label_button.TButton", font=("Time new roman",10)
                             , foreground="Black", background="light green")

        self.frame=Frame(self,style="frame.TFrame")
        self.frame.pack(side=TOP,fill=BOTH,expand=TRUE)

        self.img=PhotoImage(file="hide.png")
        self.label_img = Label(self.frame,image=self.img, style="label.TLabel")
        self.label_img.place(relx=0, rely=0)

        self.label1=Label(self.frame,text="New Password :",style="label.TLabel")
        self.label1.place(relx=.315,rely=.1)

        self.label2 = Label(self.frame, text="Confirm Password :",style="label.TLabel")
        self.label2.place(relx=.25, rely=.23)

        self.button=Button(self.frame,text="Set",
                           command=self.set,style="label_button.TButton")
        self.button.place(relx=.55,rely=.45)

        self.entry1 = Entry(self.frame, font=("book antiqua",13), width=10,show="*")
        self.entry1.place(relx=.62, rely=.1)

        self.entry2 = Entry(self.frame,show="*", font=("book antiqua",13), width=10)
        self.entry2.place(relx=.62, rely=.23)


    def set(self):
       if self.entry1.get()=="" and self.entry2.get()=="":
           messagebox.showwarning("Warning Message", "Password Cannot be Space \n Please Write Characters")

       else:
           if self.entry1.get() == self.entry2.get():
               messagebox.showinfo("Success Message", "Password Updated Successfully")
               con=connect("login.db")
               cur = con.cursor()
               cur.execute("select * from Login")
               accounts = cur.fetchall()
               x = accounts[len(accounts) - 1]
               print(x[1])
               cur.execute(" update Login set password ='{0}' where password = '{1}' ".format(self.entry1.get(), x[1]))
               con.commit()

               self.destroy()
               user_interface.login()
           else:
               messagebox.showerror("Error Message", "Password Not Matched\n\nPlease Try Again")

#X=reset_password()
#X.mainloop()