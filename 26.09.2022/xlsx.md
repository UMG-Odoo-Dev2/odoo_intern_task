# **XLSXWriter** 
- a Python module for writing files in the Excel.
- can be used to write text, numbers, and formulas to multiple worksheets.
- supports features such as formatting, images, charts, page setup, autofilters, conditional formatting and many others.
### **Advantages:**
- supports more Excel features than any of the alternative modules.
- has a high degree of fidelity with files produced by Excel.
- has extensive documentation, example files and tests.
- is fast and can be configured to use very little memory even for very large output files.

### **Disadvantages:**
- file format or extension is not valid so it cannot read or modify existing Excel XLSX files.
- can only create new files.

## **Installing XlsxWrite**

There are several ways to do this, in that
- first install XlsxWriter module using PIP.<br>

    `$ pip install xlsxwriter `

 ## **Creating XLSX file**
 - first import the module
 
    `import xlsxwriter`<br>
- to create a new workbook object use the workbook() constructor<br>

    `wb= xlsxwriter.Workbook(filename, [,options])`

 ### **Create Worksheet**
 - use to addd a new worksheet add_worksheet() method<br>
    `ws = workbook.add_worksheet() ` **# default sheet1**
 - can specify the worksheet name <br>
  `ws = workbook.add_worksheet('data')` <br>
- The worksheet name must be a valid Excel worksheet name:<br>
    1) It must be less than 32 characters.
    2) It cannot contain any of the characters: [ ] : * ? / \.
    3) It cannot begin or end with an apostrophe.<br>
    `error for above 3: InvalidWorksheetName`

    4) You cannot use the same, case insensitive, name for more than one worksheet<br>
    `error: DuplicateWorksheetName`
    5) should not use the Excel reserved name “History”.
- write() method use the worksheet object to write data.<br>
    `worksheet.write(row, col, some_data)`

- close() method use to close the excel file.<br>
    `workbook.close()`

- add a bold format to use highlight cell <br>
    `bold = workbook.add_format({'bold': True})`

- add a number format for cells with money<br>
    `money = workbook.add_format({'num_format':'$#,##0'})`

- Write some data headers.<br>
    `worksheet.write('A1', 'Item', bold)`
- Add an Excel date format.<br>
    `date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})`<br>
### **To specify the data type:**

- write_string()
- write_number()
- write_blank()
- write_formula()
- write_datetime()
- write_boolean()
- write_url()






