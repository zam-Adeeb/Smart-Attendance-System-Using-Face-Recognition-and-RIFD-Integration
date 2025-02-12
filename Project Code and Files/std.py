from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
import cv2
import tkinter as tk
from tkcalendar import Calendar
import re
from tkinter import filedialog
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import numpy as np

class STD:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x920+0+0")
        self.root.title("Face Recognition System")

        # var
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_cour=StringVar()
        self.var_yer=StringVar()
        self.var_bth=StringVar()
        self.var_id=StringVar()
        self.var_sec=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_pho=StringVar()
        self.var_add=StringVar()
        self.var_r1=StringVar()
        self.var_search = StringVar()
        self.var_filter = StringVar()

        img=Image.open("images/bg2.jpg")
        img=img.resize((1540,920),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)

        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,width=1540,height=920)

        fl1=Label(bg,text="Student Management System",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl1.place(x=0,y=0,width=1540,height=55)

        main_frame=Frame(bg,bd=2,bg="white")
        main_frame.place(x=20,y=65,width=1490,height=760)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        Left_frame.place(x=10,y=10,width=600,height=700)

        fl2=Label(Left_frame,text="Student Form",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl2.place(x=10,y=10,width=575,height=55)

        CC_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        CC_frame.place(x=20,y=80,width=565,height=150)

        # dept
        Dept_l=Label(CC_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        Dept_l.grid(row=0,column=0,padx=10)

        dep=ttk.Combobox(CC_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep["values"]=("Select Department","CSE","ISE","ECE","EEE","Physics","Chemistry")
        dep.current(0)
        dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        C_l=Label(CC_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        C_l.grid(row=0,column=2,padx=10)
        
        CC_l=ttk.Combobox(CC_frame,textvariable=self.var_cour,font=("times new roman",12,"bold"),width=20,state="readonly")
        CC_l["values"]=("Select Course","B.E","MTech")
        CC_l.current(0)
        CC_l.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # #year
        # Y_l=Label(CC_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        # Y_l.grid(row=1,column=2,padx=10)
        
        # yer_l=ttk.Combobox(CC_frame,textvariable=self.var_yer,font=("times new roman",12,"bold"),width=20,state="readonly")
        # yer_l["values"]=("Select Year","1st","2nd","3rd","4th")
        # yer_l.current(0)
        # yer_l.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # CC_l = ttk.Combobox(CC_frame, textvariable=self.var_cour, font=("times new roman", 12, "bold"), width=20, state="readonly")
        # CC_l["values"] = ("Select Course", "B.E", "MTech")
        # CC_l.current(0)
        # CC_l.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        CC_l.bind("<<ComboboxSelected>>", self.update_years)  # Bind selection event

        # Year Label
        Y_l = Label(CC_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        Y_l.grid(row=1, column=2, padx=10)

        # Year Dropdown
        self.yer_l = ttk.Combobox(CC_frame, textvariable=self.var_yer, font=("times new roman", 12, "bold"), width=20, state="readonly")
        self.yer_l["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        self.yer_l.current(0)
        self.yer_l.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # batch
        B_l=Label(CC_frame,text="Select Batch",font=("times new roman",12,"bold"),bg="white")
        B_l.grid(row=1,column=0,padx=10)
        
        Bec_l=ttk.Combobox(CC_frame,textvariable=self.var_bth,font=("times new roman",12,"bold"),width=20,state="readonly")
        Bec_l["values"]=("Select Batch","2018-Batch","2019-Batch","2020-Batch","2021-Batch","2022-Batch","2023-Batch","2024-Batch")
        Bec_l.current(0)
        Bec_l.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # details
        Cs_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Cs_frame.place(x=20,y=250,width=565,height=240)

        usn_l=Label(Cs_frame,text="USN",font=("times new roman",12,"bold"),bg="white")
        usn_l.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.usn_in=ttk.Entry(Cs_frame,textvariable=self.var_usn,width=22,font=("times new roman",12,"bold"))
        self.usn_in.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        self.usn_in.bind("<FocusOut>", self.validate_usn)

        n_l=Label(Cs_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        n_l.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        self.n_in=ttk.Entry(Cs_frame,textvariable=self.var_name,width=22,font=("times new roman",12,"bold"))
        self.n_in.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        self.n_in.bind("<FocusOut>", self.validate_name)

        id_l=Label(Cs_frame,text="ID No",font=("times new roman",12,"bold"),bg="white")
        id_l.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        self.id_in=ttk.Entry(Cs_frame,textvariable=self.var_id,width=22,font=("times new roman",12,"bold"))
        self.id_in.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        self.id_in.bind("<FocusOut>", self.validate_id)

        Sc_l=Label(Cs_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        Sc_l.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        Sc_in=ttk.Combobox(Cs_frame,textvariable=self.var_sec,width=20,font=("times new roman",12,"bold"))
        Sc_in["values"]=("Select Section","A","B","C")
        Sc_in.current(0)
        Sc_in.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        G_l=Label(Cs_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        G_l.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        G_in=ttk.Combobox(Cs_frame,textvariable=self.var_gen,width=20,font=("times new roman",12,"bold"))
        G_in["values"]=("Select Gender","Male","Female")
        G_in.current(0)
        G_in.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        P_l=Label(Cs_frame,text="Phone",font=("times new roman",12,"bold"),bg="white")
        P_l.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        self.P_in=ttk.Entry(Cs_frame,textvariable=self.var_pho,width=22,font=("times new roman",12,"bold"))
        self.P_in.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        self.P_in.bind("<FocusOut>", self.validate_phone)

        Dob_l=Label(Cs_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        Dob_l.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        # Dob_in=ttk.Entry(Cs_frame,textvariable=self.var_dob,width=22,font=("times new roman",12,"bold"))
        # Dob_in.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        self.dob_btn = ttk.Button(Cs_frame, text="Select DOB", command=self.open_calendar)
        self.dob_btn.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Display Selected DOB
        self.dob_display = Label(Cs_frame, textvariable=self.var_dob, font=("times new roman", 12, "bold"), bg="white", relief=RIDGE, width=20, anchor="w")
        self.dob_display.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        A_l=Label(Cs_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        A_l.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        A_in=ttk.Entry(Cs_frame,textvariable=self.var_add,width=22,font=("times new roman",12,"bold"))
        A_in.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        # button

        B_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        B_frame.place(x=20,y=500,width=565,height=190)

        b1=ttk.Radiobutton(B_frame,width=17,variable=self.var_r1,text="Take Photo Sample",value="Yes")
        b1.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        b2=ttk.Radiobutton(B_frame,width=17,variable=self.var_r1,text="No Photo Sample",value="No")
        b2.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        b3=Button(B_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b3.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        b4=Button(B_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b4.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        b5=Button(B_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b5.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        b6=Button(B_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b6.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        b7=Button(B_frame,command=self.gen_data,text="Take Photo",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b7.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        b8=Button(B_frame,text="Update Photo",command=self.gen_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b8.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        b9=Button(B_frame,text="Return Home",width=17,command=self.des,font=("times new roman",12,"bold"),bg="blue",fg="white")
        b9.grid(row=3,column=1,padx=10,pady=2,sticky=W)

        # Right
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,)
        Right_frame.place(x=640,y=10,width=820,height=700)

        fl3=Label(Right_frame,text="Student Database",font=("times new roman",35,"bold"),bg="navy",fg="white")
        fl3.place(x=10,y=10,width=800,height=55)

        SS_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        SS_frame.place(x=10,y=80,width=800,height=80)

        # S_l=Label(SS_frame,text="Search: ",font=("times new roman",12,"bold"),bg="white")
        # S_l.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        S_in=ttk.Entry(SS_frame,textvariable=self.var_search,width=22,font=("times new roman",12,"bold"))
        S_in.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        SS_l=ttk.Combobox(SS_frame,textvariable=self.var_filter,font=("times new roman",12,"bold"),width=20,state="readonly")
        SS_l["values"]=("Select","USN","Name","Dept","Course")
        SS_l.current(0)
        SS_l.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        b10=Button(SS_frame,text="Search",command=self.search,width=15,font=("times new roman",12,"bold"),bg="lightgray",fg="black")
        b10.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        b11=Button(SS_frame,text="Show all",command=self.fetch_data,width=15,font=("times new roman",12,"bold"),bg="lightgray",fg="black")
        b11.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # Table
        T_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        T_frame.place(x=10,y=180,width=800,height=500)

        sr_x=ttk.Scrollbar(T_frame,orient=HORIZONTAL)
        sr_y=ttk.Scrollbar(T_frame,orient=VERTICAL)
        self.st=ttk.Treeview(T_frame,columns=("Id","Name","USN","Dept","Course","Year","Batch","Section","Gender","DOB","Phone","Address","Photo"),xscrollcommand=sr_x.set,yscrollcommand=sr_y.set)
        sr_x.pack(side=BOTTOM,fill=X)
        sr_y.pack(side=RIGHT,fill=Y)
        sr_x.config(command=self.st.xview)
        sr_y.config(command=self.st.yview)

        self.st.heading("Id",text="ID")
        self.st.heading("Name",text="Name")
        self.st.heading("USN",text="USN")
        self.st.heading("Dept",text="Dept.")
        self.st.heading("Course",text="Course")
        self.st.heading("Year",text="Year")
        self.st.heading("Batch",text="Batch")
        self.st.heading("Section",text="Section")
        self.st.heading("Gender",text="Gender")
        self.st.heading("DOB",text="DOB")
        self.st.heading("Phone",text="Phone")
        self.st.heading("Address",text="Address")
        self.st.heading("Photo",text="Photo")
        self.st["show"]="headings"
        
        self.st.pack(fill=BOTH,expand=1)
        self.st.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def update_years(self, event):
        # Get the selected course
        selected_course = self.var_cour.get()

        # Update year values based on the selected course
        if selected_course == "MTech":
            self.yer_l["values"] = ("Select Year", "1st", "2nd")
        else:
            self.yer_l["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        self.yer_l.current(0)  # Reset to "Select Year"

    def open_calendar(self):
        # Create a new window for the calendar
        cal_win = Toplevel(self.root)
        cal_win.title("Select Date of Birth")

        # Calendar widget
        cal = Calendar(cal_win, selectmode="day", date_pattern="dd/mm/yyyy")  # Adjust date pattern as needed
        cal.pack(pady=20)

        # Save and Close Button
        def save_date():
            self.var_dob.set(cal.get_date())  # Set selected date to the variable
            cal_win.destroy()  # Close the calendar window

        save_btn = ttk.Button(cal_win, text="Select", command=save_date)
        save_btn.pack(pady=10)

    def validate_usn(self, event=None):
        usn = self.var_usn.get()
        pattern = r"^[1-4][A-Z]{2}\d{2}[A-Z]{2}\d{3}$"
        if not re.match(pattern, usn):
            messagebox.showerror("Validation Error", "Invalid USN! Format should be: 1DB21CS005",parent=self.root)

    def validate_name(self, event=None):
        name = self.var_name.get()
        pattern = r"^[A-Za-z ]+$"
        if not re.match(pattern, name):
            messagebox.showerror("Validation Error", "Invalid Name! Only letters (A-Z, a-z) are allowed.",parent=self.root)

    def validate_id(self, event=None):
        id_no = self.var_id.get()
        pattern = r"^\d+$"
        if not re.match(pattern, id_no):
            messagebox.showerror("Validation Error", "Invalid ID No.! Only numeric digits are allowed.",parent=self.root)

    def validate_phone(self, event=None):
        phone = self.var_pho.get()
        pattern = r"^\d{10}$"
        if not re.match(pattern, phone):
            messagebox.showerror("Validation Error", "Invalid Phone Number! Must be a 10-digit numeric value.",parent=self.root)

    def des(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recongnition","Are you sure",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return

        # fun
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_cour.get()=="Select Course" or self.var_yer.get()=="Select Year" or self.var_bth.get()=="Select Batch":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
                my_cur=conn.cursor()
                my_cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_usn.get(),
                    self.var_dept.get(),
                    self.var_cour.get(),
                    self.var_yer.get(),
                    self.var_bth.get(),
                    self.var_sec.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_pho.get(),
                    self.var_add.get(),
                    self.var_r1.get()
                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # fetah data
    # def fetch_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
    #     my_cur=conn.cursor()
    #     my_cur.execute("select * from student")
    #     data=my_cur.fetchall()

    #     if len(data)!=0:
    #         self.st.delete(*self.st.get_children())
    #         for i in data:
    #             self.st.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
        my_cur = conn.cursor()

        # Fetch and sort data alphabetically
        my_cur.execute("SELECT * FROM student ORDER BY Name ASC")
        data = my_cur.fetchall()

        if len(data) != 0:
            self.st.delete(*self.st.get_children())
            for record in data:
                self.st.insert("", "end", values=record)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.st.focus()
        cont=self.st.item(cursor_focus)
        data=cont["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_usn.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_cour.set(data[4]),
        self.var_yer.set(data[5]),
        self.var_bth.set(data[6]),
        self.var_sec.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_pho.set(data[10]),
        self.var_add.set(data[11]),
        self.var_r1.set(data[12])

    def search(self):
        try:
            self.db_connection = mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
            self.cursor = self.db_connection.cursor()

            search_term = self.var_search.get()
            filter_option = self.var_filter.get()

            if filter_option == "Select" or not search_term:
                messagebox.showerror("Input Error", "Please select a valid filter and enter a search term",parent=self.root)
                return

            query = f"SELECT * FROM student WHERE {filter_option} LIKE %s"
            conn = self.db_connection
            if conn:
                cursor = conn.cursor()
                cursor.execute(query, ('%' + search_term + '%',))  # Use wildcard search
                rows = cursor.fetchall()

                if not rows:
                    messagebox.showinfo("No Data", "No matching data found!",parent=self.root)
                    return

                self.st.delete(*self.st.get_children())  # Clear previous data

                for row in rows:
                    self.st.insert("", "end", values=row)

                conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}",parent=self.root)

    # update
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_cour.get()=="Select Course" or self.var_yer.get()=="Select Year" or self.var_bth.get()=="Select Batch":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
                upda=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if upda>0:
                        my_cur=conn.cursor()
                        my_cur.execute("update student set Name=%s,usn=%s,Dept=%s,Course=%s,year=%s,batch=%s,section=%s,gender=%s,DOB=%s,Phone=%s,Address=%s,Photo=%s where sid=%s",(
                            self.var_name.get(),
                            self.var_usn.get(),
                            self.var_dept.get(),
                            self.var_cour.get(),
                            self.var_yer.get(),
                            self.var_bth.get(),
                            self.var_sec.get(),
                            self.var_gen.get(),
                            self.var_dob.get(),
                            self.var_pho.get(),
                            self.var_add.get(),
                            self.var_r1.get(),
                            self.var_id.get()
                        ))
                else:
                    if not upda:
                        return
                messagebox.showinfo("Success","Student details has been Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # delete
    # def delete_data(self):
    #     if self.var_id.get()=="":
    #         messagebox.showerror("Error","Student id is required",parent=self.root)
    #     else:
    #         try:
    #             det=messagebox.askyesno("Delete","Do you want to delete this student details?",parent=self.root)
    #             if det>0:
    #                 conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
    #                 my_cur=conn.cursor()
    #                 sql="delete from student where sid=%s"
    #                 val=(self.var_id.get(),)
    #                 my_cur.execute(sql,val)
    #             else:
    #                 if not det:
    #                     return
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
            my_cur = conn.cursor()

            # Delete the student
            my_cur.execute("DELETE FROM student WHERE sid=%s", (self.var_id.get(),))

            # Remove associated photos
            # data_dir = "data"
            # files = [f for f in os.listdir(data_dir) if f.startswith(f"user.{self.var_id.get()}.")]
            # for file in files:
            #     os.remove(os.path.join(data_dir, file))

            # # Re-index student IDs
            # my_cur.execute("SET @count = 0")
            # my_cur.execute("UPDATE student SET sid = @count:= @count + 1")
            # my_cur.execute("ALTER TABLE student AUTO_INCREMENT = 1")

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete", "Successfully deleted", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            
    # reset
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_usn.set("")
        self.var_dept.set("Select Department")
        self.var_cour.set("Select Course")
        self.var_yer.set("Select Year")
        self.var_bth.set("Select Batch")
        self.var_sec.set("Select Section")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_pho.set("")
        self.var_add.set("")
        self.var_r1.set("")

    # photo
    # def gen_data(self):
    #     if self.var_dept.get()=="Select Department" or self.var_cour.get()=="Select Course" or self.var_yer.get()=="Select Year" or self.var_bth.get()=="Select Batch":
    #         messagebox.showerror("Error","All Fields are required",parent=self.root)
    #     else:
    #         try:
    #             conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="face_atd")
    #             my_cur=conn.cursor()
    #             my_cur.execute("select * from student")
    #             res=my_cur.fetchall()
    #             id=0
    #             for x in res:
    #                 id+=1
    #             my_cur.execute("update student set Name=%s,usn=%s,Dept=%s,Course=%s,year=%s,batch=%s,section=%s,gender=%s,DOB=%s,Phone=%s,Address=%s,Photo=%s where sid=%s",(
    #                         self.var_name.get(),
    #                         self.var_usn.get(),
    #                         self.var_dept.get(),
    #                         self.var_cour.get(),
    #                         self.var_yer.get(),
    #                         self.var_bth.get(),
    #                         self.var_sec.get(),
    #                         self.var_gen.get(),
    #                         self.var_dob.get(),
    #                         self.var_pho.get(),
    #                         self.var_add.get(),
    #                         self.var_r1.get(),
    #                         self.var_id.get()==id+1
    #                     ))
    #             conn.commit()
    #             self.fetch_data()
    #             self.reset_data()
    #             conn.close()

    #             #load file

    #             face_file=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #             def face_crop(img):
    #                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #                 faces=face_file.detectMultiScale(gray,1.3,5)
    #                 for (x,y,w,h) in faces:
    #                     face_crop=img[y:y+h,x:x+w]
    #                     return face_crop
    #             cap=cv2.VideoCapture(0)
    #             img_id=0
    #             while True:
    #                 ret,myframe=cap.read()
    #                 if face_crop(myframe) is not None:
    #                     img_id+=1
    #                     face=cv2.resize(face_crop(myframe),(450,450))
    #                     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    #                     fnp="data/user." +str(id)+ "." +str(img_id) +".jpg"
    #                     cv2.imwrite(fnp,face)
    #                     cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    #                     cv2.imshow("Face Cam",face)

    #                 if cv2.waitKey(1)==13 or int(img_id)==100:
    #                     break

    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result","Face Data Successfully Completed")

    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    from tkinter import filedialog

    def gen_data(self):
        if self.var_dept.get() == "Select Department" or self.var_cour.get() == "Select Course" or self.var_yer.get() == "Select Year" or self.var_bth.get() == "Select Batch":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="0000", database="face_atd")
                my_cur = conn.cursor()
                my_cur.execute("select * from student")
                id = self.var_id.get()

                if not id:
                    messagebox.showerror("Error", "No student selected!", parent=self.root)
                    return
                res = my_cur.fetchall()
                # id = 0
                # for x in res:
                #     id += 1
                print(f"Debug: id = {id}")

                # Database update
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Face detection file
                face_file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_file.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_crop = img[y:y + h, x:x + w]
                        return face_crop

                def save_faces(face, id, img_id):
                    """Save face data 100 times"""
                    fnp = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(fnp, face)
                    print(f"Saved: {fnp}")

                def capture_from_camera():
                    """Capture faces using the camera"""
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, myframe = cap.read()
                        if face_crop(myframe) is not None:
                            img_id += 1
                            face = cv2.resize(face_crop(myframe), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            save_faces(face, id, img_id)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Face Cam", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Face Data Successfully Completed",parent=self.root)

                def upload_image():
                    """Upload and process a single image"""
                    file_path = filedialog.askopenfilename(
                        title="Select Image",
                        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
                    )
                    if not file_path:
                        messagebox.showerror("Error", "No file selected",parent=self.root)
                        return
                    
                    img = cv2.imread(file_path)
                    img_id = 0
                    for _ in range(25):
                        if face_crop(img) is not None:
                            img_id += 1
                            face = cv2.resize(face_crop(img), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            save_faces(face, id, img_id)
                    messagebox.showinfo("Result", "Face Data Successfully Uploaded and Processed",parent=self.root)

                # Ask the user for the input method
                choice = messagebox.askquestion("Choose Input Method", "Do you want to use the camera? (Yes for Camera, No for Upload Image)",parent=self.root)

                if choice == "yes":
                    capture_from_camera()
                else:
                    upload_image()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=STD(root)
    root.mainloop()