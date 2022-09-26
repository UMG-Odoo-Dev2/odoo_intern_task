import xlsxwriter
workbook=xlsxwriter.Workbook('odoo.xlsx')
worksheet=workbook.add_worksheet()

col=1
head=['Name','Address','Phone Number','Email']
for i in range(65,70):
    worksheet.write(chr(i)+str(1),head[col-1])
    col+=1

workbook.close()