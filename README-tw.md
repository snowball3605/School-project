# 分數計算機
這只是一份學校功課

<img src="https://img.shields.io/badge/Python_3.13.5-blue" /> <img src="https://img.shields.io/badge/Tkinter-red" /> <img src="https://img.shields.io/badge/version-v1.0.0-green" /> <img src="https://img.shields.io/badge/install_size-26MB-blue" /> <img src="https://img.shields.io/badge/minzipped_size-24MB-blue" />

## 啟動方式
程式有分為"ui"和"non-ui"兩種使用方式，即是命令提示字元和使用者介面
以下是兩種使用方式

### non-ui 命令提示字元

第一步: ``` py start.py -f non-ui.py ``` 即可啟動

### ui 使用者介面

第一步: ``` py start.py -f ui.py ``` 即可啟動

## 使用限制

### 可輸入變量

- Enter student name: 
   - 只可以存在英文字符或空格
   - 不可留空
- Enter student ID:
   - 只可以輸入數字
   - 只能有9個字元
   - 不可留空
- Enter test marks:
   - 只可(包括)0-100(包括)之間
   - 不可留空
- Enter project marks:
   - 只可(包括)0-100(包括)之間
   - 不可留空
- Enter Workshop marks:
   - 只可(包括)0-100(包括)之間
   - 不可留空
- Enter Exam marks:
   - 只可(包括)0-100(包括)之間
   - 不可留空
- Do you want to enter another student record? [Y/y] for Yes, [N/n] for No:
   - 只可輸入<y/n/Y/N>
      - y/Y 表示想輸入另一個學生成績
      - n/N 表示不想輸入另一個學生成績

## 使用方式

### 命令提示字元

按照使用限制完成輸入後，完成每一個學生的輸入就會輸出以下數據

```` 
*************** Results ****************
Student name: [你的輸入]
Student ID: [你的輸入]
Test Mark: [你的輸入] ,Project Mark: [你的輸入] ,Workshop_Mark: [你的輸入] ,Exam Mark: [你的輸入]
Module Marks: [計算後結果] ,Module Grade: [計算後結果] , Remarks: [計算後結果]
[計算後結果]
*************** Results ****************
````

然後輸出
``` Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ```

當輸入Y/y時重複以上步驟

當輸入N/n時會輸出以下內容
```
There is/are [總共輸入人數] students' record(s) inputted, and the average marks is: [整體Module的分數除以人數]
Total number of A grade: [Module Grade取得A人數]
Total number of B grade: [Module Grade取得B人數]
Total number of C grade: [Module Grade取得C人數]
Total number of F grade: [Module Grade取得F人數]
```

### 使用者介面

按照使用限制輸入所有數據後,點擊Calculate 然後顯示:

```` 
*************** Results ****************
Student name: [你的輸入]
Student ID: [你的輸入]
Test Mark: [你的輸入] ,Project Mark: [你的輸入] ,Workshop_Mark: [你的輸入] ,Exam Mark: [你的輸入]
Module Marks: [計算後結果] ,Module Grade: [計算後結果] , Remarks: [計算後結果]
[計算後結果]
*************** Results ****************
````
然後可以繼續輸入，Total會顯示已經輸入多少次數據

完成所有數據的輸入後點擊Refresh就會顯示以下內容，而且刪除原本的數據
```
There is/are [總共輸入人數] students' record(s) inputted, and the average marks is: [整體Module的分數除以人數]
Total number of A grade: [Module Grade取得A人數]
Total number of B grade: [Module Grade取得B人數]
Total number of C grade: [Module Grade取得C人數]
Total number of F grade: [Module Grade取得F人數]
```

## 計算過程
``` CA Marks = Test Marks * 0.4 + Project Marks * 0.3 + Workshop Marks * 0.3 ```

``` Module Marks = (CA Marks * 0.5) + Exam Marks * 0.5 ```

如果CA Marks或Exam Marks<40時，Module Grade就會取得F

如果Module Marks >=40和<65時，Module Grade就會取得C

如果Module Marks >=65和<75時，Module Grade就會取得B

如果Module Marks >=75和<=100時，Module Grade就會取得A

## 版權
所有主要功能已於2025年10月17日完成

版權所有 © 2025 陳文淵（Raistey）保留所有權利

本服務僅為使用者提供資料處理，並非對使用者的行為負責。
因此，使用者應自行承擔風險，並對其儲存的內容負責。