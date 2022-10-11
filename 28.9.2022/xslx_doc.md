# XlsxWriter
- a Python library to write files in the Excel 2007+ XLSX file format
- It can be used to write text, numbers and formulas to multiple worksheets.
- It supports features such as formatting, images, charts, page setup, autofilters, conditional formatting and many others.
- It can only create new files.
- It cannot read or modify existing Excel XLSX files.
- The first step is to install the XLSX module.
- By using PIP,
```
pip install XlsxWriter
```
- To work with XlsxWriter in Python, need to import XlsxWriter module before using it
```
import xlsxwriter
```
- Create a new workbook object using ` workbook()` constructor
```
# one, non-optional argument
workbook=xlsxwriter.workbook('Employee.xlsx')
```
- The workbook object is used to add a new worksheet via `add_worksheet()` method
- By default worksheet names in a spreadsheet will be Sheet1, Sheet2, etc. But a worksheet name can be specified.
```
worksheet=workbook.add_worksheet() # default to Sheet1
worksheet=workbook.add_worksheet('Employee.xlsx') # Employee
worksheet=workbook.add_worksheet() #default to Sheet3
```
- The worksheet object is used to write data via `write()` method.
```
worksheet.write(0,0,"Hello") # (row,col,data)
```
- Throughout XlsxWriter, rows and columns are zero indexed.
- The first cell in a worksheet, *A1* ,is (0,0).
- Finally, close the Excel file via `close()` method.
```
workbook.close()
```

