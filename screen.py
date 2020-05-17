from tkinter  import *
from tkinter.ttk import *
import main_window
from sqlite3 import connect
from time import *
from tkinter import filedialog


class Screen(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.state("zoomed")
        self.style=Style()
        self.title("Files")
        self.resizable(FALSE,False)


        self.style.configure("Header.TFrame",background="Black")
        self.style.configure("label1.TLabel",background="Black",foreground="gold",font=("colonna mt",45))
        self.style.configure("label3.TLabel", background="Black", foreground="gold", font=("Times new roman", 45))
        self.style.configure("Button.TLabel",background="Black",foreground="cyan",font=("colonna mt",15))
        self.style.configure("Button1.TLabel", background="Black", foreground="light green", font=("chiller", 15))

        self.frame=Frame(self,style="Header.TFrame")
        self.frame.pack(side=TOP,fill=BOTH,expand=TRUE)


        self.label_txt1=Label(self.frame,text="",style="label1.TLabel")
        self.label_txt1.place(relx=.08,rely=.3)

        self.label_txt2=Label(self.frame,text="",style="label3.TLabel")
        self.label_txt2.place(relx=.35,rely=.3)

        self.button=Button(self.frame,text="Exit",
                           command=self.exit,style="Button.TLabel")
        self.button.place(relx=.95,rely=.9)


        self.button1=Button(self.frame,text="Update New File : CLICK HERE",
                           command=self.open_me,style="Button1.TLabel")
        self.button1.place(relx=.8,rely=.1)


        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        accounts = cur.fetchall()
        print(accounts)
        print(len(accounts))
        x = accounts[0]
        j=x[4]
        print(x)
        h=0
        while True:
         for i in range(len(accounts)):
             if h==0:
                 self.label_txt1["text"] = "Files Name :"
                 self.update()
                 sleep(1)
                 h+=1
             else:
               self.label_txt2["text"]=accounts[i][j]
               self.update()
               sleep(1)
               h+=1
         else:
             h=0
    def exit(self):
        self.destroy()
        main_window.Home()
    def open_me(self):

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        accounts = cur.fetchall()
        print(accounts)
        print(len(accounts))
        x = accounts[0]
        if  x[4]==0:
          songs = filedialog.askopenfilename(filetypes=(("Audio Files",".mp3"), ("All Files", "*.*")))
          y = songs.split("/")
          jk = y[len(y) - 1]
          print(jk)

          cur.execute("""insert into Storer(Audio)
                     values('{0}')""".format(jk))
          con.commit()
        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        accounts = cur.fetchall()
        print(accounts)
        print(len(accounts))
        x = accounts[0]

        if x[4]==1:
            songs = filedialog.askopenfilename(filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
            y = songs.split("/")
            jk = y[len(y) - 1]
            cur.execute("""insert into Storer(Text)
                                values('{0}')""".format(jk))
            con.commit()


        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        accounts = cur.fetchall()
        print(accounts)
        print(len(accounts))
        x = accounts[0]

        if x[4]==2:
            songs = filedialog.askopenfilename(filetypes=(("Video Files", ".mp4"), ("All Files", "*.*")))
            y = songs.split("/")
            jk = y[len(y) - 1]
            cur.execute("""insert into Storer(Video)
                                values('{0}')""".format(jk))
            con.commit()

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        accounts = cur.fetchall()
        print(accounts)
        print(len(accounts))
        x = accounts[0]

        if x[4]==3:
            songs = filedialog.askopenfilename(filetypes=(("Photos Files",".jpg,.png"), ("All Files", "*.*")))
            y = songs.split("/")
            jk = y[len(y) - 1]
            cur.execute("""insert into Storer(Photo)
                                values('{0}')""".format(jk))
            con.commit()
