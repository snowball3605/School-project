import main

def non_ui():
    i = 0
    main.H_Test_Mark = 0
    main.H_Project_Mark = 0
    main.H_Workshop_Mark = 0
    main.H_Exam_Mark = 0
    global Module, sp
    while True:
        i += 1
        Name = main.Input_Name()
        ID = main.Input_ID()

        Test_Mark = main.Input_Test_Mark()
        Project_Mark = main.Input_Project_Mark()
        Workshop_Mark = main.Input_Workshop_Mark()
        Exam_Mark = main.Input_Exam_Mark()

        main.H_Test_Mark += Test_Mark
        main.H_Project_Mark += Project_Mark
        main.H_Workshop_Mark += Workshop_Mark
        main.H_Exam_Mark += Exam_Mark

        print("*************** Results ****************")
        print("Student name: ", Name)
        print("Student ID: ", ID)
        print("Test Mark: ", Test_Mark, " ,Project Mark: ", Project_Mark, " ,Workshop Mark: ", Workshop_Mark, " ,Exam Mark: ", Exam_Mark)
        print(main.Calculate(Test_Mark, Project_Mark, Workshop_Mark, Exam_Mark))
        print("*************** Results ****************")

        # sp = str(f"*************** Results ****************\nStudent name: {Name}\nStudent ID: {ID}\nTest Mark: {Test_Mark} ,Project Mark: {Project_Mark}, Workshop Mark: {Workshop_Mark} ,Exam Mark: {Exam_Mark}\n{Calculate(Test_Mark, Project_Mark, Workshop_Mark, Exam_Mark)}\n*************** Results ****************")


        loop = input("Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ")
        if loop == "N" or loop == "n":
            print(f"There is/are {i} students' record(s) inputted, and the average marks is: {main.H_Module / i}")
            print("Total number of A grade: ", main.c_a)
            print("Total number of B grade: ", main.c_b)
            print("Total number of C grade: ", main.c_c)
            print("Total number of F grade: ", main.c_f)
            return

if __name__ == '__main__':
    print("Please do not run this file directly, please run start.py")



# All major features completed on 17/10/2025
# Copyright © 2025 Chen Wenyuan(Raistey) All Rights Reserved
# This service only provides users with data processing and is not responsible for the user's behavior.
# Therefore, users should bear their own risks and are responsible for the content they store.