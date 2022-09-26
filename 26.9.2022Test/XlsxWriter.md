XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX file format.

It can be used to write text, numbers, and formulas to multiple worksheets and it supports features such as formatting, images, charts, page setup, autofilters, conditional formatting and many others.

XlsxWriter has some advantages and disadvantages over the alternative Python modules for writing Excel files.

    Advantages:

   - It supports more Excel features than any of the alternative modules.
   - It has a high degree of fidelity with files produced by Excel. In most cases the files produced are 100% equivalent to files produced by Excel.
   - It has extensive documentation, example files and tests.
    It is fast and can be configured to use very little memory even for very large output files.

    Disadvantages:

   - It cannot read or modify existing Excel XLSX files.


   ### What is XLXS used for?
   XLSX/XLS files are used to store and manage data such as numbers,
 formulas, text, and drawing shapes. XLSX is part of Microsoft Office Open XML specification (also known as OOXML or OpenXML),
 and was introduced with Office 2007. XLSX is a zipped, XML-based file format

### How do I write an XLSX file?
Contents

- Step 1: Double click on the XLSX file.
- Step 2: Drag and drop the XLSX file onto an Excel window to open it.
- Step 3: “Open with” – open the XLSX file in Excel using the right-click menu.


### How do I write data into an XLSX file in Python?
Create Excel XLSX Files in Python

- Create a new object of Workbook class.
- Access the desired Worksheet in the workbook using Workbook. getWorksheets(). get(index) method.
- Put value in the desired cell using Worksheet. getCells(). get(“A1”). ...
- Save the workbook as . xlsx file using Workbook. save() method.

 ### What is XLSX stand for?
Microsoft Excel Open XML Spreadsheet


 ### How do I view XLSX files?
To read an XLSX file in R, first copy the data from Excel, then import data from the clipboard into R.

### How do I read an XLSX file in Python? 
You can read the file with the Python module named openpyxl.
 Download the openpyxl module, then use the Python import command to read the data from the XLSX file
 
 ## XlsxWriter down step
    cmd
    python -m venv filename
    cd filename
    cd Scripts
    activate
    pip install XlsxWriter

   