import string
import tkinter as tk
from tkinter import messagebox

import main

main_window = tk.Tk()
main_window.title("Mark Calculator")
main_window.geometry("450x500")

H_Test_Mark = 0
H_Project_Mark = 0
H_Workshop_Mark = 0
H_Exam_Mark = 0
i = 0

Name = tk.Entry(main_window)
ID = tk.Entry(main_window)
Test_Mark = tk.Entry(main_window)
Project_Mark = tk.Entry(main_window)
Workshop_Mark = tk.Entry(main_window)
Exam_Mark = tk.Entry(main_window)
number = tk.Label(main_window, text=i, font=("Arial", 14))
result_label = tk.Label(main_window, text="Result: ")

def Check(name, ID, test_mark, project_mark, workshop_mark, exam_mark):
    if not(not(any(char in string.punctuation for char in name)) and not (any(char.isdigit() for char in name))):
        return False
    if len(ID) != 9:
        return False
    try:
        ID = int(ID)
    except:
        return False
    if int(test_mark) < 0 or int(test_mark) > 100:
        return False
    if int(project_mark) < 0 or int(project_mark) > 100:
        return False
    if int(workshop_mark) < 0 or int(workshop_mark) > 100:
        return False
    if int(exam_mark) < 0 or int(exam_mark) > 100:
        return False
    return True


def calculate():
    if not (Check(Name.get(), ID.get(), Test_Mark.get(), Project_Mark.get(), Workshop_Mark.get(), Exam_Mark.get())):
        messagebox.showerror("Error", "Double-check your input.")
        return
    else:
        try:
            global H_Test_Mark, H_Project_Mark, H_Workshop_Mark, H_Exam_Mark, i
            text = (
                "*************** Results ****************\n"
                f"Student Name: {Name.get()}\n"
                f"Student ID: {ID.get()}\n"
                f"Test Mark: {int(Test_Mark.get())} ,Project Mark: {int(Project_Mark.get())} ,Workshop Mark: {int(Workshop_Mark.get())} ,Exam Mark: {int(Exam_Mark.get())}\n"
                f"{main.Calculate(int(Test_Mark.get()), int(Project_Mark.get()), int(Workshop_Mark.get()), int(Exam_Mark.get()))}\n"
                f"*************** Results ****************"
            )
            result_label.configure(text=text)
            H_Test_Mark += int(Test_Mark.get())
            H_Project_Mark += int(Project_Mark.get())
            H_Workshop_Mark += int(Workshop_Mark.get())
            H_Exam_Mark += int(Exam_Mark.get())
            delete()
        except Exception as e:
            print(e)
        else:
            i += 1
            number.configure(text=i, font=("Arial", 14))

def refresh():
    global H_Test_Mark, H_Project_Mark, H_Workshop_Mark, H_Exam_Mark, i
    text = (
        f"There is/are {i} students' record(s) inputted, and the average marks is: {main.H_Module / i}\n"
        f"Total number of A grade: {main.c[0]}\n"
        f"Total number of B grade: {main.c[1]}\n"
        f"Total number of C grade: {main.c[2]}\n"
        f"Total number of F grade: {main.c[3]}"
    )
    result_label.configure(text=text)
    i = 0
    number.configure(text=i, font=("Arial", 14))

def delete():
    Name.delete(0, tk.END)
    ID.delete(0, tk.END)
    Test_Mark.delete(0, tk.END)
    Project_Mark.delete(0, tk.END)
    Workshop_Mark.delete(0, tk.END)
    Exam_Mark.delete(0, tk.END)


def ui():
    label_number1 = tk.Label(main_window, text="Student Name:", font=("Arial", 11))
    label_number1.place(x=10, y=20, width=100, height=30)

    totle = tk.Label(main_window, text="Total:", font=("Arial", 14))
    totle.place(x=300, y=20, width=100, height=30)

    number.place(x=300, y=45, width=100, height=30)

    Name.place(x=10, y=50, width=100, height=30)

    label_number2 = tk.Label(main_window, text="Student ID:", font=("Arial", 11))
    label_number2.place(x=150, y=20, width=100, height=30)

    ID.place(x=150, y=50, width=100, height=30)

    label_number3 = tk.Label(main_window, text="Test Mark:", font=("Arial", 11))
    label_number3.place(x=10, y=90, width=100, height=30)

    Test_Mark.place(x=10, y=120, width=100, height=30)

    label_number4 = tk.Label(main_window, text="Project Mark:", font=("Arial", 11))
    label_number4.place(x=150, y=90, width=100, height=30)

    Project_Mark.place(x=150, y=120, width=100, height=30)

    label_number5 = tk.Label(main_window, text="Workshop Mark:", font=("Arial", 11))
    label_number5.place(x=10, y=160, width=100, height=30)

    Workshop_Mark.place(x=10, y=190, width=100, height=30)

    label_number6 = tk.Label(main_window, text="Exam Mark:", font=("Arial", 11))
    label_number6.place(x=150, y=160, width=100, height=30)

    Exam_Mark.place(x=150, y=190, width=100, height=30)

    result_label.place(x=10, y=280, width=420, height=120)

    calculate_button = tk.Button(main_window, text="Calculate", command=calculate)
    calculate_button.place(x=10, y=240, width=100, height=30)

    calculate_button = tk.Button(main_window, text="Refresh", command=refresh)
    calculate_button.place(x=150, y=240, width=100, height=30)

    main_window.mainloop()

if __name__ == '__main__':
    print("Please do not run this file directly, please run start.py")

# All major features completed on 17/10/2025
# Copyright © 2025 Chen Wenyuan(Raistey) All Rights Reserved
# This service only provides users with data processing and is not responsible for the user's behavior.
# Therefore, users should bear their own risks and are responsible for the content they store.