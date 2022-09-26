import xlsxwriter

workbook = xlsxwriter.Workbook('FormatEg.xlsx')
worksheet =  workbook.add_worksheet()



test1 = (
    ['Leo',   27],
    ['Aries', 22],
    ['Jhon',  23],
)

row = 0
col = 0

for name, age in (test1):
    worksheet.write(row, col,     name)
    worksheet.write(row, col + 1, age)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B3)')

workbook.close()