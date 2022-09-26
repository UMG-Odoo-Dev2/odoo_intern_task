# Xlsx Writer
- a Python module for writing files in the Excel 2007+ XLSX file format</br>
- can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel</br>

## Advantages
- supports more Excel features than any of the alternative modules</br>
- has a high degree of fidelity with files produced by Excel<br>
- has extensive documentation<br>
- fast and can be configured to use very little memory even for very large output files<br>

## Disadvantages
- cannot read or modify existing Excel XLSX files because the fileformat or extension is not valid<br>

## Installing XlsxWriter
The first step is to install the XlsxWriter module.One of several ways is using PIP.<br>

    $ pip install XlsxWriter

## Creating a Xlsx File
- import the module
- create a new workbook object using the Workbook() constructor

        import xlsxwriter  
        workbook=xlsxwriter.Workbook(filename.xlsx [,options]) 
- XlsxWriter can only create new files and cannot read or modify existing files.
- add a new worksheet via the add_worksheet() method and default worksheet names are Sheet1, Sheet2, etc.<br>
- The worksheet name must be a valid Excel worksheet name
    - must be less than 32 characters
    - cannot contain any of the characters: [ ] : * ? / \
    - cannot begin or end with an apostrophe
    - cannot use the same, case insensitive, name for more than one worksheet
    - should not use the Excel reserved name “History”<br>

            worksheet = workbook.add_worksheet([name])
- use the worksheet object to write data via the write() method<br>

        worksheet.write(row, col, some_data)
- close the Excel file via the close() method<br>

        workbook.close()
- to add a bold format to use to highlight cells<br>

        bold = workbook.add_format({'bold': True})
- to add a number format for cells with money<br>

        money = workbook.add_format({'num_format': '$#,##0'})
- to format the data in the cell<br>

        wordsheet.write(row, column, token, [format])

#### To control over the type of data ,we can use specific methods of write()

    write_string()
    write_number()
    write_blank()
    write_formula()
    write_datetime()
    write_boolean()
    write_url()

