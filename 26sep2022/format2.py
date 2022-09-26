import xlsxwriter

workbook = xlsxwriter.Workbook('Adding Format.xlsx')
worksheet = workbook.add_worksheet('Format')

# Adding Bold Format
bold = workbook.add_format({'bold':True})

# Adding number format
money = workbook.add_format({'num_format':'$#,##0'})


# Some Header Data
worksheet.write('A1', 'Name', bold)
worksheet.write('B1', 'Salary', bold)

person = (
    ['Cave', 250000],
    ['Word', 300000],
    ['Adam', 400000],
)

row = 1
col = 0

for name, salary in (person):
    worksheet.write(row, col,     name)
    worksheet.write(row, col + 1, salary, money)
    row += 1

worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=SUM(B1:B3)', bold, money)

workbook.close()