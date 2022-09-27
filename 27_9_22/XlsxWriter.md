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
    
### woorkbook.add_worksheet([name])
- To add a new worksheet to a workbook
### workbook.add_format()
- To create new Format objects which are used to apply formatting to a cell
### workbook.add_chart()
- To create a new chart object that can be inserted into a worksheet

                chart = workbook.add_chart({'type': 'column'})

        
- The properties that can be set are:<br>

        type    (required)
        subtype (optional)
        name    (optional)

- ***type*** - a required parameter and defines the type of chart that will be created<br>
        - The available types are: ***area, bar, column, doughnut, line, pie, radar, scatter, stock***

- ***subtype*** - used to define a chart subtype where available<br>

        workbook.add_chart({'type': 'bar', 'subtype': 'stacked'})

- ***name*** -  the name for the chart sheet. The name property is optional and if it isn’t supplied it will default to Chart1, Chart2, etc.

        chart = workbook.add_chart({'type': 'column', 'name': 'MyChart'})

### workbook.add_chartsheet()
- To add a new chartsheet to a workbook

### workbook.close()
- To close the Workbook object and write the XLSX file
### workbook.set_size()
- To set the size of a workbook window

        workbook.set_size(width, height)
### workbook.set_tab_ratio()
- To set the ratio between the worksheet tabs and the horizontal slider
- The tab ratio is between 0 and 100

        workbook.set_tab_ratio(tab_ratio)

### workbook.set_properties()
- To set the document properties such as Title, Author etc.
- The properties are all optional and should be passed in dictionary format
### workbook.set_custom_property()
- To set one or more custom document properties not covered by the standard properties in the `set_properties()`

        workbook.set_custom_property(name, value[, property_type]')

- Parameters:<br>	
        - name (string) – The name of the custom property.<br>
        - value – The value of the custom property (various types).<br>
        - property_type (string) – The type of the property. Optional.<br>
### workbook.define_name()
- T defined a name that can be used to represent a value, a single cell or a range of cells in a workbook. 
- These are sometimes referred to as a “Named Range”.
        
        