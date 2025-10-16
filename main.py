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
        else:
            return int(id)

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
    global Module, H_Module, c_a, c_b, c_c, c_f
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
