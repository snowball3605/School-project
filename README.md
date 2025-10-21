# Score Calculator
This is just a school assignment.

<img src="https://img.shields.io/badge/Python_3.13.5-blue" /> <img src="https://img.shields.io/badge/Tkinter-red" /> <img src="https://img.shields.io/badge/version-v1.0.0-green" /> <img src="https://img.shields.io/badge/install_size-26MB-blue" /> <img src="https://img.shields.io/badge/minzipped_size-24MB-blue" />


## Starting Method
The program can be used in two modes: "UI" and "non-UI"—the command prompt and the user interface.

Below are the two modes.

### Non-UI Command Prompt

Step 1: ``` py start.py -f non-ui.py ``` to start.

### UI User Interface

Step 1: ``` py start.py -f ui.py ``` to start.

## Usage Limitations

### Acceptable Variables

- Enter student name:
   - Only English characters or spaces are allowed.
   - Cannot be left blank.
- Enter student ID:
   - Only numbers are allowed.
   - Can only contain 9 characters.
   - Cannot be left blank.
- Enter test marks:
   - Can only be between 0 and 100 (inclusive).
   - Cannot be left blank.
- Enter project marks:
   - Can only be between 0 and 100 (inclusive).
   - Cannot be left blank
- Enter Workshop marks:
   - Can only be between 0 and 100 (inclusive)
   - Cannot be left blank
- Enter Exam marks:
   - Can only be between 0 and 100 (inclusive)
   - Cannot be left blank
- Do you want to enter another student record? [Y/y] for Yes, [N/n] for No:
   - Can only enter <y/n/Y/N>
      - y/Y indicates you want to enter another student's score
      - n/N indicates you do not want to enter another student's score

## Usage

### Command Prompt

After completing the input according to the usage restrictions, the following data will be output for each student.

````
*************** Results ****************
Student name: [your input]
Student ID: [your input]
Test Mark: [your input], Project Mark: [your input], Workshop Mark: [your input], Exam Mark: [your input]
Module Marks: [Calculated Result], Module Grade: [Calculated Result], Remarks: [Calculated Result]
[Calculated Result]
*************** Results ****************
````

Then output
``` Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ```

Repeat the above steps when Y/y is entered.

When N/n is entered, the following output is displayed.
```
There are/are [a total number of students entered] students' record(s), and the average score is: [overall module score divided by the number of students]
Total number of A grade: [number of students with an A grade in the module]
Total number of B grade: [number of students with a B grade in the module]
Total number of C grade: [number of students with a C grade in the module]
Total number of F grade: [number of students with an F grade in the module]
```

### User Interface

After entering all data according to the usage restrictions, click Calculate, and the display will be:

````
*************** Results ****************
Student name: [your input]
Student ID: [your input]
Test Mark: [your input], Project Mark: [your input], Workshop Mark: [your input], Exam Mark: [your input]
Module Marks: [calculated result], Module Grade: [calculated result], Remarks: [calculated result]
[calculated result]
*************** Results ****************
````
You can continue entering data. The Total field will display the number of times you have entered data.

After entering all data, click Refresh to display the following information and delete the previous data.
```
There are [a total number of students' records entered], and the average marks is: [the total number of students' scores divided by the number of students]
Total number of A grades: [the number of students who received an A grade in the module]
Total number of B grades: [the number of students who received a B grade in the module]
Total number of C grades: [the number of students who received a C grade in the module]
Total number of F grades: [the number of students who received a C grade in the module] [Number of students receiving an F grade]
```

## Calculation Process
``` CA Marks = Test Marks * 0.4 + Project Marks * 0.3 + Workshop Marks * 0.3 ```

``` Module Marks = (CA Marks * 0.5) + Exam Marks * 0.5 ```

If CA Marks or Exam Marks are <40, the module grade is F.

If Module Marks are >=40 and <65, the module grade is C.

If Module Marks are >=65 and <75, the module grade is B.

If Module Marks are >=75 and <100, the module grade is A.

## Copyright
All major features completed on 17/10/2025

Copyright © 2025 Chen Wenyuan(Raistey) All Rights Reserved

This service only provides users with data processing and is not responsible for the user's behavior.
Therefore, users should bear their own risks and are responsible for the content they store.