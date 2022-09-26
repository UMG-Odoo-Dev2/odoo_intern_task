import xlsxwriter

workbook= xlsxwriter.Workbook('chartsheet.xlsx')
worksheet = workbook.add_worksheet('First_Sheet')

chartsheet = workbook.add_chartsheet()
chart = workbook.add_chart({'type': 'column'})

data = [
   [10, 20, 30, 40, 50],
   [20, 40, 60, 80, 100],
   [30, 60, 90, 120, 150],
]
worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])
worksheet.write_column('C1', data[2]) 

chart.add_series({'values': '=First_Sheet!$A$1:$A$5'})
chart.add_series({'values': '=First_Sheet!$B$1:$B$5'})
chart.add_series({'values': '=First_Sheet!$C$1:$C$5'})
chartsheet.set_chart(chart)
chartsheet.activate()

workbook.close()