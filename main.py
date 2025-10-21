import string

Weight_Test_Marks = 0.4
Weight_Project_Marks = 0.3
Weight_Workshops_Marks = 0.3
Weight_CA_Marks = 0.5
Weight_Exam_Marks = 0.5

Module = 0
c = [0,0,0,0]
H_Module = 0
def Input_Name():
    while True:
        name = input("Enter student name: ")
        if not (any(char in string.punctuation for char in name)) and not (any(char.isdigit() for char in name)):
            return name
        else:
            print("Invalid name, please try again.")

def Input_ID():
    while True:
        try:
            id = input("Enter student ID: ")
            if len(id) != 9:
                print("Invalid ID, please try again.")
            else:
                return int(id)
        except:
            print("Invalid ID, please try again.2")

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
    global Module, H_Module, c
    Module = (CA * Weight_CA_Marks) + (Exam_Mark * Weight_Exam_Marks)
    H_Module += Module

    if CA < 40 or Exam_Mark < 40:
        c[3] += 1
        return f"Module Marks: {Module} ,Module Grade: F ,Remarks: Restudy\n Don't get discouraged, keep trying!"
    elif Module >= 40 and Module < 65:
        c[2] += 1
        return f"Module Marks: {Module} ,Module Grade: C ,Remarks: Pass with C grade\n Please be careful, you only qualified for a C."
    elif Module >= 65 and Module < 75:
        c[1] += 1
        return f"Module Marks: {Module} ,Module Grade: B ,Remarks: Pass with B grade\n Almost can get an A grade, work harder!"
    elif Module >= 75 and Module <= 100:
        c[0] += 1
        return f"Module Marks: {Module} ,Module Grade: A ,Remarks: Pass with A grade\n Well done!"
    else:
        return f"Invalid Module Grade\nPlease double-check the input marks"

if __name__ == '__main__':
    print("Please do not run this file directly, please run start.py")

# All major features completed on 17/10/2025
# Copyright © 2025 Chen Wenyuan(Raistey) All Rights Reserved
# This service only provides users with data processing and is not responsible for the user's behavior.
# Therefore, users should bear their own risks and are responsible for the content they store.