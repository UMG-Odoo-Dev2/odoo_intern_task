from datetime import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('Date.xlsx')
worksheet = workbook.add_worksheet('add_date')

# Add bold format
bold = workbook.add_format({'bold': True})

# Add number format
money = workbook.add_format({'num_format':'$#,##0'})

# Add Excel Date format
date_format = workbook.add_format({'num_format':'mmmm d yyyy'})

# Adjust the colum width
worksheet.set_column(1, 1, 15)

#Write some header data
worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Date', bold)
worksheet.write('C1', 'Salary', bold)

person = (
    ['Smith', '2022-09-20', 250000],
    ['Row', '2022-09-21', 450000],
    ['Blade', '2022-09-22', 350000],
)


row = 1
col = 0

for name, date_str, salary in (person):
    # Convert the date string into datetime obj
    date = datetime.strptime(date_str, "%Y-%m-%d")

    worksheet.write(row, col,     name               )
    worksheet.write(row, col + 1, date,   date_format)
    worksheet.write(row, col + 2, salary, money      )
    row += 1

worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 2, '=SUM(C2:C4)', money)

workbook.close()



