from user_interface import *
import user_interface
import screen

class Home(first_window):
    def __init__(self):
        first_window.__init__(self)

        self.img1 = PhotoImage(file="video.png")
        self.button_img1 = Button(self.frame1, image=self.img1,
                                  style="Headerimg.TLabel",command=self.video)
        self.button_img1.place(relx=0.25, rely=.3)

        self.img2 = PhotoImage(file="Text.png")
        self.button_img2 = Button(self.frame1, image=self.img2,
                            style="Headerimg.TLabel",command=self.text)
        self.button_img2.place(relx=0.55, rely=.3)

        self.img3 = PhotoImage(file="music.png")
        self.button_img3 = Button(self.frame1, image=self.img3,
                            style="Headerimg.TLabel",command=self.audio)
        self.button_img3.place(relx=0.25, rely=.6)

        self.img4 = PhotoImage(file="photo.png")
        self.button_img4 = Button(self.frame1, image=self.img4,
                        style="Headerimg.TLabel",command=self.photo)
        self.button_img4.place(relx=0.5, rely=.6)

        self.img5 = PhotoImage(file="exit.png")
        self.button_img5 = Button(self.frame1, image=self.img5, style="Headerimg.TLabel"
                    ,command=self.exit)
        self.button_img5.place(relx=0.95, rely=.5)

        canvas = Canvas(self.frame1, width=1366, height=200, bg="black",
                        highlightthickness=0)
        canvas.place(relx=.0,rely=.0)

        self.l_img1 = PhotoImage(file="title.png")
        self.label_img1 = Label(canvas, image=self.l_img1, style="Headerimg.TLabel")
        self.label_img1.place(relx=0.2, rely=.05)
        l = canvas.create_window(100, 100, window=self.label_img1)

        xspeed =5
        yspeed = 0

        while True:

            canvas.move(l, xspeed, yspeed)
            pos = canvas.coords(l)
            print(pos)
            print(pos[0])
            if pos[0] >= 970:
                xspeed = -xspeed
            if pos[0] == 400:
                xspeed =5

            self.update()
            sleep(.1)


    def exit(self):
        self.destroy()
        user_interface.login()

    def video(self):

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        cur.execute(" update Storer set count ='{0}' ".format(2))
        con.commit()
        self.destroy()
        screen.Screen()

    def text(self):

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        cur.execute(" update Storer set count ='{0}' ".format(1))
        con.commit()
        self.destroy()
        screen.Screen()

    def audio(self):

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        cur.execute(" update Storer set count ='{0}' ".format(0))
        con.commit()
        self.destroy()
        screen.Screen()
    def photo(self):

        con = connect("storer.db")
        cur = con.cursor()
        cur.execute("select * from Storer")
        cur.execute(" update Storer set count ='{0}' ".format(3))
        con.commit()
        self.destroy()
        screen.Screen()



#x=Home()
#x.mainloop()