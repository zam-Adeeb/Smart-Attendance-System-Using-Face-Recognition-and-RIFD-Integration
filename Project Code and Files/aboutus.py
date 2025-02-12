from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class US:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x920+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        img = Image.open("images/bg.jpg")
        img = img.resize((1540, 920), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, width=1540, height=920)

        # Title
        fl1 = Label(bg, text="About Us", font=("times new roman", 35, "bold"), bg="navy", fg="white")
        fl1.place(x=0, y=90, width=1540, height=55)

#college logo
/*
        fl1 = Label(bg, text="This project has been submitted for KSCST", font=("times new roman", 16, "bold"), bg="navy", fg="white")
        fl1.place(x=0, y=800, width=1540, height=40)

        dbit = Image.open("images/dbit.jpg")
        dbit = dbit.resize((1540, 90), Image.LANCZOS)
        self.i_dbit = ImageTk.PhotoImage(dbit)

        i_dbit = Button(bg, image=self.i_dbit)
        i_dbit.place(x=0, y=0, width=1540, height=90) */

        # Scrollable Frame
        scroll_canvas = Canvas(bg, bg="white")
        scroll_canvas.place(x=20, y=145, width=1490, height=650)  # Reduced height to fit all elements

        scrollbar = Scrollbar(bg, orient=VERTICAL, command=scroll_canvas.yview)
        scrollbar.place(x=1510, y=145, height=650)

        scroll_canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = Frame(scroll_canvas, bg="white")
        scroll_canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Update scrollable region dynamically
        def update_scroll_region(event=None):
            scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))

        content_frame.bind("<Configure>", update_scroll_region)

        # Project Description
        project_description = (
            "We, the final-year students of the CSE Department at Don Bosco Institute of Technology, "
            "proudly present our project, an Smart Attendance System using Face Recognition and RFID. This project "
            "was developed as part of our academic curriculum and submitted for KSCST. Our primary goal was "
            "to create an efficient, secure, and user-friendly attendance system that combines cutting-edge "
            "technologies like AI, facial recognition, and IoT components."
            "\n\nThe system emphasizes real-world utility, ensuring high accuracy and security while being "
            "easily adaptable for various institutions. Our team worked collaboratively, dedicating ourselves "
            "to building a modular system that incorporates the latest advancements in technology."
        )
        dev_lab = Label(content_frame, text=project_description, font=("times new roman", 17, "bold"), bg="white", 
                        wraplength=1400, justify="center")
        dev_lab.pack(pady=10)

        # Team Member Contributions
        team_info = [
            {
                "name": "ADEEB AHMED",
                "role": "Core Algorithm Development",
                "description": "ADEEB specialized in the design and implementation of core algorithms for the system, "
                                "focusing on facial recognition. He worked on developing and optimizing AI models for face detection, "
                                "liveness detection, and recognition, ensuring accurate identification. His contribution also extended "
                                "to the integration of advanced AI algorithms for attendance data analysis, reporting, and system security.\n\n"
            },
            {
                "name": "ABHISHEK H",
                "role": "RFID Integration and Hardware Interface",
                "description": "ABHISHEK contributed significantly to the IoT aspects of the project, focusing on RFID technology. "
                                "He ensured seamless integration of RFID readers and cards with the system, facilitating hybrid attendance "
                                "marking. His expertise in hardware interfacing ensured reliable communication between the system’s hardware "
                                "and software components.\n\n"
            },
            {
                "name": "BALAJI M",
                "role": "User Experience and Interface Design",
                "description": "BALAJI focused on creating an intuitive user interface (UI) and overall user experience (UX). He designed "
                                "administrator and user-friendly dashboards for managing attendance data. His focus on UX ensured a seamless "
                                "navigation experience, making the system accessible to all stakeholders, including students, faculty, and administrators."
            },
            {
                "name": "DHANU KUMAR N T",
                "role": "Database Architecture and Data Management",
                "description": "DHANU designed and managed the system’s robust database architecture. He developed efficient data schemas, "
                                "ensuring the system could handle real-time data storage, retrieval, and management securely. His work ensured "
                                "that attendance records were stored accurately and remained tamper-proof, addressing both security and scalability concerns.\n\n"
            },
        ]

        for member in team_info:
            frame = Frame(content_frame, bg="white", bd=2, relief=RIDGE)
            frame.pack(fill=X, padx=20, pady=10)

            # Team Member Image
            img_path = f"images/{member['name'].split()[0].lower()}.jpg"
            img = Image.open(img_path).resize((100, 120), Image.LANCZOS)
            member_img = ImageTk.PhotoImage(img)

            img_label = Label(frame, image=member_img, bg="white")
            img_label.image = member_img
            img_label.pack(side=LEFT, padx=10, pady=10)

            # Team Member Info
            text = f"{member['name']} ({member['role']}):\n\n{member['description']}"
            text_label = Label(frame, text=text, font=("times new roman", 18, "bold"), bg="white", justify="left", wraplength=1250)
            text_label.pack(side=LEFT, padx=10)

        # Ensure scrollability
        scroll_canvas.update_idletasks()


if __name__ == "__main__":
    root = Tk()
    obj = US(root)
    root.mainloop()
