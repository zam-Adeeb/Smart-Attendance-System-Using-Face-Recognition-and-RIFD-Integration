from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import FRS
from reg import REG

class LOG:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1540x920+0+0")

        # Variables
        self.var_remember = IntVar()
        self.username = StringVar()
        self.password = StringVar()

        # Load saved credentials
        self.load_credentials()

        img = Image.open("images/bg_3.jpg")
        img = img.resize((1540, 920), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        main_frame = Frame(bg, bd=2, bg="#FCFCFC")
        main_frame.place(x=600, y=220, width=340, height=400)

#college logo
/*
        fl1=Label(bg,text="This project has been submitted for KSCST",font=("times new roman",16,"bold"),bg="navy",fg="white")
        fl1.place(x=0,y=805,width=1540,height=30)
        
        dbit=Image.open("images/dbit.jpg")
        dbit=dbit.resize((1540,90),Image.LANCZOS)
        self.i_dbit=ImageTk.PhotoImage(dbit)

        i_dbit=Button(bg,image=self.i_dbit)
        i_dbit.place(x=0,y=0,width=1540,height=90)  */

        img1 = Image.open("images/profile.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(img1)

        l1 = Label(image=self.img1, bg="black", borderwidth=0)
        l1.place(x=730, y=230, width=100, height=100)

        get_str = Label(main_frame, text="    Login     ", font=("times new roman", 18, "bold"), fg="white", bg="black")
        get_str.place(x=115, y=100)

        user_l = Label(main_frame, text="Username", font=("times new roman", 12, "bold"), fg="black", bg="#FCFCFC")
        user_l.place(x=10, y=155)

        self.txtuser = ttk.Entry(main_frame, textvariable=self.username, font=("times new roman", 18, "bold"))
        self.txtuser.place(x=90, y=155, width=230)

        pass_l = Label(main_frame, text="Password", font=("times new roman", 12, "bold"), fg="black", bg="#FCFCFC")
        pass_l.place(x=10, y=210)

        self.txtpass = ttk.Entry(main_frame, textvariable=self.password, font=("times new roman", 18, "bold"), show="*")
        self.txtpass.place(x=90, y=210, width=230)

        che = Checkbutton(main_frame, variable=self.var_remember, text="Remember me",
                          font=("times new roman", 12), fg="black", bg="#FCFCFC")
        che.place(x=10, y=260)

        # Login button
        logbtn = Button(main_frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                        relief=RIDGE, fg="white", bg="cyan2", activeforeground="white", activebackground="cyan2")
        logbtn.place(x=110, y=300, width=120, height=35)

        reg_l = Label(main_frame, text="Don't have an account?", font=("times new roman", 10), fg="black", bg="#FCFCFC")
        reg_l.place(x=80, y=350)

        albtn = Button(main_frame, text="Register", command=self.reg_win, font=("times new roman", 10, "bold"),
                       borderwidth=0, fg="black", bg="#FCFCFC", activeforeground="black", activebackground="#FCFCFC")
        albtn.place(x=225, y=350)

        passbtn = Button(main_frame, text="Forgot Password", command=self.forgot_password, font=("times new roman", 12),
                         borderwidth=0, fg="black", bg="#FCFCFC", activeforeground="black", activebackground="#FCFCFC")
        passbtn.place(x=200, y=260, width=120)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
                my_cur = conn.cursor()
                my_cur.execute("select * from register where Username=%s and Password=%s", (
                    self.username.get(),
                    self.password.get()
                ))
                row = my_cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
                else:
                    open_main = messagebox.askyesno("YesNO", "Access only Admin",parent=self.root)
                    if open_main:
                        self.save_credentials()
                        self.root.destroy()  # Close login window
                        root = Tk()
                        self.app = FRS(root)  # Open the main application
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def reg_win(self):
        self.new_window = Toplevel(self.root)
        self.app = REG(self.new_window)

    # def forgot_password(self):
    #     messagebox.showinfo("Forgot Password", "Feature under development!", parent=self.root)

    def forgot_password(self):
        def reset_password():
            if txt_new_pass.get() == "":
                messagebox.showerror("Error", "Password cannot be empty", parent=reset_win)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="0000",
                                                   database="face_atd")
                    my_cur = conn.cursor()
                    my_cur.execute("update register set Password=%s where Username=%s", (
                        txt_new_pass.get(),
                        self.txtuser.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Password reset successfully", parent=reset_win)
                    reset_win.destroy()
                except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=reset_win)

        reset_win = Toplevel(self.root)
        reset_win.title("Reset Password")
        reset_win.geometry("400x300+700+300")

        lbl_reset = Label(reset_win, text="Reset Password", font=("times new roman", 20, "bold"))
        lbl_reset.pack(pady=20)

        lbl_new_pass = Label(reset_win, text="New Password", font=("times new roman", 15))
        lbl_new_pass.pack(pady=10)

        txt_new_pass = Entry(reset_win, show="*", font=("times new roman", 15))
        txt_new_pass.pack(pady=10)

        btn_reset = Button(reset_win, text="Reset", command=reset_password, font=("times new roman", 15), bg="green",
                           fg="white")
        btn_reset.pack(pady=20)

    def save_credentials(self):
        if self.var_remember.get() == 1:
            with open("credentials.txt", "w") as f:
                f.write(f"{self.username.get()}\n{self.password.get()}")
        else:
            open("credentials.txt", "w").close()  # Clear saved credentials

    def load_credentials(self):
        try:
            with open("credentials.txt", "r") as f:
                lines = f.readlines()
                if len(lines) == 2:
                    self.username.set(lines[0].strip())
                    self.password.set(lines[1].strip())
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = Tk()
    obj = LOG(root)
    root.mainloop()
