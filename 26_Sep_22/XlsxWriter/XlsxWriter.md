# XlsxWriter
- XlsxWriter is a Python module for writing files in the XLSX file format. It can be used to write text, numbers, and formulas to multiple worksheets. 
- It supports features such as formatting, images, charts, page setup, auto filters, conditional formatting and many others.
- Use this command to install xlsxwriter module: 
```
 pip install xlsxwriter 
 ```
- XlsxWriter has some advantages and disadvantages over the alternative Python modules for writing Excel files.
- ***Advantages:***
    - supports more Excel features than any of the alternative modules.
    - has a high degree of fidelity with files produced by Excel. (In most cases the files produced are 100% equivalent to files produced by Excel.)
    - has extensive documentation, example files and tests.
    - fast and can be configured to use very little memory even for very large output files.
- ***Disadvantages:***
    - It cannot read or modify existing Excel XLSX files.
### ***Note***
**XlsxWriter can only create new files. It cannot read or modify existing files.**  

> Adding formatting to the XLSX File
- We can pass formats(that we defined) as an optional third parameter to the worksheet.write() method to format the data in the cell:
```
write(row, column, token, [format])
```
Like this:
```
worksheet.write(row, 0, 'Total', bold)
```
- Instead of (row, col) we used the Excel 'A1' style notation.
```
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)
```
- Excel treats different types of input data, such as strings and numbers, differently although it generally does it transparently to the user. 
- XlsxWriter tries to emulate this in the worksheet.write() method by mapping Python data types to types that Excel supports.
- The write() method acts as a general alias for several more specific methods:
- ***write_string()***
- ***write_number()***
- ***write_blank()***
- ***write_formula()***
- ***write_datetime()***
- ***write_boolean()***
- ***write_url()***
# The Workbook Class
> Constructor
```
Workbook(filename[, options])
```
Create a new XlsxWriter Workbook object.
- Parameters:	
    - ***filename (string)*** – The name of the new Excel file to create.
    - ***options (dict)*** – Optional workbook parameters. See below.
- Return type:	
    - A Workbook object.

## Workbook Class
### ***add_worksheet()***: 
- Adds a new worksheet to a workbook.
    ```
        add_worksheet([name])
    ```
#### Parameters:	
- **name (string)** – Optional worksheet name, defaults to Sheet1, etc.
- **Return type** :	A worksheet object.
- **Raises:** - 
    - *DuplicateWorksheetName*– if a duplicate worksheet name is used.
    - *InvalidWorksheetName* – if an invalid worksheet name is used.
    - *ReservedWorksheetName* – if a reserved worksheet name is used.
### ***add_format()***: 
- Used to create new Format objects which are used to apply formatting to a cell.
### ***add_chart()***: 
- Creates a new chart object that can be inserted into a worksheet via the insert_chart() Worksheet method.
- The supported chart types are:
    - **area**: Creates an Area (filled line) style chart.
    - **bar**: Creates a Bar style (transposed histogram) chart.
    - **column**: Creates a column style (histogram) chart.
    - **line**: Creates a Line style chart.
    - **pie**: Creates a Pie style chart.
    - **doughnut**: Creates a Doughnut style chart.
    - **scatter**: Creates a Scatter style chart.
    - **stock**: Creates a Stock style chart.
    - **radar**: Creates a Radar style chart.