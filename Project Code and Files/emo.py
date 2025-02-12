from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import Message ,Text
from tkinter import filedialog
from datetime import datetime
import mysql.connector
import cv2
import os
import csv
import pandas as pd
import google.generativeai as ai

# AI Chatbot Configuration
API_KEY = ''
ai.configure(api_key=API_KEY)

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("800x600")

        # File Upload Button
        btn_upload = Button(self.root, text="Upload Files and Compare", font=("times new roman", 16, "bold"), bg="blue", fg="white", command=self.compare_files)
        btn_upload.pack(pady=20)

        # AI Chatbot Integration
        chat_frame = Frame(self.root, bd=2, relief=RIDGE)
        chat_frame.place(x=10, y=100, width=760, height=450)

        chat_label = Label(chat_frame, text="AI Chatbot", font=("times new roman", 16, "bold"), bg="lightgray")
        chat_label.pack(fill=X)

        self.chatbox = Text(chat_frame, font=("times new roman", 14), wrap=WORD)
        self.chatbox.pack(fill=BOTH, expand=1)

        self.chat_entry = Entry(self.root, font=("times new roman", 14))
        self.chat_entry.place(x=10, y=560, width=700, height=30)

        send_btn = Button(self.root, text="Send", font=("times new roman", 14), bg="green", fg="white", command=self.chat_with_ai)
        send_btn.place(x=720, y=560, width=70, height=30)

    def compare_files(self):
        try:
            # Ask for CSV file (Face Registration Attendance)
            csv_file_path = filedialog.askopenfilename(title="Select Face Registration CSV File",
                                                    filetypes=[("CSV files", "*.csv")])
            if not csv_file_path:
                messagebox.showerror("Error", "No CSV file selected!",parent=self.root)
                return

            # Ask for Excel file (RFID Attendance)
            excel_file_path = filedialog.askopenfilename(title="Select RFID Excel File",
                                                        filetypes=[("Excel files", "*.xlsx")])
            if not excel_file_path:
                messagebox.showerror("Error", "No Excel file selected!",parent=self.root)
                return

            # Read CSV file
            face_data = pd.read_csv(csv_file_path)

            # Read Excel file
            rfid_data = pd.read_excel(excel_file_path)

            # # Select only the required columns
            required_columns_cvs = ['ID', 'Name', 'USN', 'Dept','Time', 'Date','Status']
            required_columns_ecel = ['Number']
            required_columns = ['Name', 'USN', 'Time', 'Date','Number','Status']

            # Ensure the required columns exist in both files
            face_data = face_data[required_columns_cvs]
            rfid_data = rfid_data[required_columns_ecel]

            # Concatenate the two datasets
            combined_data = pd.concat([face_data, rfid_data])

            # Remove duplicate entries
            final_data = combined_data.drop_duplicates(subset=required_columns)

            final_data['Number'] = final_data['Number'].fillna('').astype(str).str.strip()  # Clean up the 'Number' column
            final_data = final_data.dropna(how='all')  # Drop rows with all empty values
            final_data.reset_index(drop=True, inplace=True) 

            if 'Number' in final_data.columns:
                final_data = final_data.drop(columns=['Number'])

            # Save the final file with current date and time
            now = datetime.now()
            filename = now.strftime("Final_Attendance_%Y%m%d_%H%M%S.csv")
            save_path = os.path.join("final", filename)

            # Ensure the directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Write the final data to a CSV file
            final_data.to_csv(save_path, index=False)

            # Show success message
            messagebox.showinfo("Success", f"Final attendance file created successfully:\n{save_path}")

        except KeyError as e:
            messagebox.showerror("Error", f"Failed to compare files: Missing columns {str(e)}",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Failed to compare files: {str(ex)}",parent=self.root)

    def chat_with_ai(self):
        try:
            user_message = self.chat_entry.get().strip()
            if not user_message:
                return

            self.chatbox.insert(END, f"You: {user_message}\n")
            self.chat_entry.delete(0, END)

            # AI Chatbot Response
            model = ai.GenerativeModel("gemini-pro")
            chat = model.start_chat()
            response = chat.send_message(user_message)

            self.chatbox.insert(END, f"Chatbot: {response.text}\n")

            # If the user asks to compare files
            if "compare files" in user_message.lower():
                self.compare_files()

        except Exception as e:
            self.chatbox.insert(END, f"Error: {str(e)}\n")

if __name__ == "__main__":
    root = Tk()
    app = AttendanceApp(root)
    root.mainloop()
