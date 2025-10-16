import string

Weight_Test_Marks = 0.4
Weight_Project_Marks = 0.3
Weight_Workshops_Marks = 0.3
Weight_CA_Marks = 0.5
Weight_Exam_Marks = 0.5




Module = 0
c_a = 0
c_b = 0
c_c = 0
c_f = 0
input_field1 = ""
input_field2 = ""
input_field3 = ""
input_field4 = ""
input_field5 = ""
input_field6 = ""
H_Module = 0
def Input_Name():
    while True:
        name = input("Enter student name: ")
        if not(any(char in string.punctuation for char in name)) and not(any(char.isdigit() for char in name)):
            return name
        else:
            print("Invalid name, please try again.")

def Input_ID():
    while True:
        try:
            id = int(input("Enter student ID: "))
        except:
            print("Invalid ID, please try again.")
        else:
            return id

def Input_Test_Mark():
    while True:
        try:
            mark = int(input("Enter test marks: "))
            if mark < 0 or mark > 100:
                print("Invalid mark, please try again. Reason: More than 100 or less than 0")
            else:
                return mark
        except:
            print("Invalid mark, please try again.")

def Input_Project_Mark():
    while True:
        try:
            mark = int(input("Enter project marks: "))
            if mark < 0 or mark > 100:
                print("Invalid mark, please try again. Reason: More than 100 or less than 0")
            else:
                return mark
        except:
            print("Invalid mark, please try again.")

def Input_Workshop_Mark():
    while True:
        try:
            mark = int(input("Enter Workshop marks: "))
            if mark < 0 or mark > 100:
                print("Invalid mark, please try again. Reason: More than 100 or less than 0")
            else:
                return mark
        except:
            print("Invalid mark, please try again.")

def Input_Exam_Mark():
    while True:
        try:
            mark = int(input("Enter Exam marks: "))
            if mark < 0 or mark > 100:
                print("Invalid mark, please try again. Reason: More than 100 or less than 0")
            else:
                return mark
        except:
            print("Invalid mark, please try again.")

def Calculate(Test_Mark, Project_Mark, Workshop_Mark, Exam_Mark):
    CA = (Test_Mark * Weight_Test_Marks) + (Project_Mark * Weight_Project_Marks) + (Workshop_Mark * Weight_Workshops_Marks)
    global Module
    global H_Module
    global c_a
    global c_b
    global c_c
    global c_f
    Module = (CA * Weight_CA_Marks) + (Exam_Mark * Weight_Exam_Marks)
    H_Module += Module

    if CA < 40 or Exam_Mark < 40:
        c_f += 1
        return f"Module Marks: {Module} ,Module Grade: F ,Remarks: Restudy\n Don't get discouraged, keep trying!"
    elif Module >= 40 and Module < 65:
        c_c += 1
        return f"Module Marks: {Module} ,Module Grade: C ,Remarks: Pass with C grade\n Please be careful, you only qualified for a C."
    elif Module >= 65 and Module < 75:
        c_b += 1
        return f"Module Marks: {Module} ,Module Grade: B ,Remarks: Pass with B grade\n Almost can get an A grade, work harder!"
    elif Module >= 75 and Module <= 100:
        c_a += 1
        return f"Module Marks: {Module} ,Module Grade: A ,Remarks: Pass with A grade\n Well done!"
    else:
        return f"Invalid Module Grade\nPlease double-check the input marks"

def UI(sp):
    import tkinter as tk
    from tkinter import messagebox

    global input_field1
    global input_field2
    global input_field3
    global input_field4
    global input_field5
    global input_field6
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Simple Calculator")
    main_window.geometry("300x400")  # Set window size to accommodate placed widgets

    # Create input field for the first number
    label_number1 = tk.Label(main_window, text="Student Name:")
    label_number1.place(x=10, y=20, width=100, height=30)

    input_field1 = tk.Entry(main_window)
    input_field1.place(x=10, y=50, width=100, height=30)

    label_number2 = tk.Label(main_window, text="Student ID:")
    label_number2.place(x=150, y=20, width=100, height=30)

    input_field2 = tk.Entry(main_window)
    input_field2.place(x=150, y=50, width=100, height=30)

    ## Marks
    label_number3 = tk.Label(main_window, text="Test Mark:")
    label_number3.place(x=10, y=90, width=100, height=30)

    input_field3 = tk.Entry(main_window)
    input_field3.place(x=10, y=120, width=100, height=30)

    label_number4 = tk.Label(main_window, text="Project Mark:")
    label_number4.place(x=150, y=90, width=100, height=30)

    input_field4 = tk.Entry(main_window)
    input_field4.place(x=150, y=120, width=100, height=30)

    label_number5 = tk.Label(main_window, text="Workshop Mark:")
    label_number5.place(x=10, y=160, width=100, height=30)

    input_field5 = tk.Entry(main_window)
    input_field5.place(x=10, y=190, width=100, height=30)

    label_number6 = tk.Label(main_window, text="Exam Mark:")
    label_number6.place(x=150, y=160, width=100, height=30)

    input_field6 = tk.Entry(main_window)
    input_field6.place(x=150, y=190, width=100, height=30)

    result_label = tk.Label(main_window, text="Result: ")
    result_label.place(x=10, y=270, width=200, height=30)


    calculate_button = tk.Button(main_window, text="Calculate", command=lambda: (
        result_label.config(text=sp)
    ))
    calculate_button.place(x=10, y=240, width=100, height=30)

    main_window.mainloop()

def Main():
    i = 0
    H_Test_Mark = 0
    H_Project_Mark = 0
    H_Workshop_Mark = 0
    H_Exam_Mark = 0
    global Module
    global sp
    while True:
        i += 1
        Name = input_field1
        ID = input_field2

        Test_Mark = input_field3
        Project_Mark = input_field4
        Workshop_Mark = input_field5
        Exam_Mark = input_field6

        H_Test_Mark += int(Test_Mark)
        H_Project_Mark += int(Project_Mark)
        H_Workshop_Mark += int(Workshop_Mark)
        H_Exam_Mark += int(Exam_Mark)

        #print("*************** Results ****************")
        #print("Student name: ", Name)
        #print("Student ID: ", ID)
        #print("Test Mark: ", Test_Mark, " ,Project Mark: ", Project_Mark, " ,Workshop Mark: ", Workshop_Mark, " ,Exam Mark: ", Exam_Mark)
        #print(Calculate(Test_Mark, Project_Mark, Workshop_Mark, Exam_Mark))
        #print("*************** Results ****************")

        sp = str(f"*************** Results ****************\nStudent name: {Name}\nStudent ID: {ID}\nTest Mark: {Test_Mark} ,Project Mark: {Project_Mark}, Workshop Mark: {Workshop_Mark} ,Exam Mark: {Exam_Mark}\n{Calculate(Test_Mark, Project_Mark, Workshop_Mark, Exam_Mark)}\n*************** Results ****************")

        UI(sp)
        loop = input("Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ")
        if loop == "N" or loop == "n":
            print(f"There is/are {i} students' record(s) inputted, and the average marks is: {H_Module / i}")
            print("Total number of A grade: ", c_a)
            print("Total number of B grade: ", c_b)
            print("Total number of C grade: ", c_c)
            print("Total number of F grade: ", c_f)
            return




if __name__ == '__main__':
    Main()
